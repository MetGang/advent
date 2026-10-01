import inspect
from typing import Any, Callable

from ..classes import AnyFn, BinaryFn, NullaryFn, UnaryFn

__all__ = [
    'train'
]

def train(f: Callable[..., Any], g: Callable[[Any, Any], Any], h: Callable[..., Any]) -> AnyFn:
    """Apply results of `f` and `h` to the binary function `g`.

    Examples:
        >>> inc = lambda x: x + 1
        >>> twice = lambda x: x * 2
        >>> combined = train(inc, lambda a, b: a + b, twice)
        >>> combined(3)
        10

        >>> left = lambda: 2
        >>> right = lambda: 3
        >>> product = train(left, lambda a, b: a * b, right)
        >>> product()
        6

        >>> f = lambda a, b: a + b
        >>> h = lambda a, b: a * b
        >>> paired = train(f, lambda x, y: x + y, h)
        >>> paired(5, 3)
        23
    """
    f_arity = len(inspect.signature(f).parameters)
    h_arity = len(inspect.signature(h).parameters)

    match [f_arity, h_arity]:
        case [0, 0]:
            return NullaryFn(lambda: g(f(), h()))
        case [1, 1]:
            return UnaryFn(lambda a: g(f(a), h(a)))
        case [2, 2]:
            return BinaryFn(lambda a, b: g(f(a, b), h(a, b)))
        case _:
            raise ValueError(f'Unsupported or mismatched arities for f ({f_arity}) and h ({h_arity})')
