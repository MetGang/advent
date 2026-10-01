from typing import Any, Callable

from ..classes import UnaryFn

__all__ = [
    'to',
    'apply',
    'partial',
    'identity',
]

def to(T: type) -> UnaryFn:
    """
    Return a unary function that casts its argument to `T`.

    >>> to(int)('42')
    42
    >>> to(str)(123)
    '123'
    """
    return UnaryFn(T)

def apply(fn: Callable[[Any], Any]) -> UnaryFn:
    """
    Return a unary function that applies `fn` to its argument.

    >>> apply(str)(123)
    '123'
    >>> apply(len)('hello')
    5
    """
    def __inner(arg: Any) -> Any:
        return fn(arg)
    return UnaryFn(__inner)

def partial(fn: Callable[[Any], Any], projector: Callable[[Any], Any]) -> UnaryFn:
    """
    Return a unary function that applies `fn` parameterized by `projector(arg)`.

    >>> add = lambda amount: lambda value: value + amount
    >>> partial(add, lambda value: value * 2)(3)
    9
    >>> partial(lambda prefix: lambda value: prefix + value, lambda _: 'Hi, ')('there')
    'Hi, there'
    """
    def __inner(arg: Any) -> Any:
        return fn(projector(arg))(arg)
    return UnaryFn(__inner)

def identity() -> UnaryFn:
    """
    Return a unary function that returns its argument unchanged.

    >>> identity()('hello')
    'hello'
    >>> identity()(42)
    42
    """
    def __inner(arg: Any) -> Any:
        return arg
    return UnaryFn(__inner)
