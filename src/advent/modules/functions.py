from typing import Any, Callable

from ..classes import UnaryFn

__all__ = [
    'to',
    'apply',
    'partial',
    'identity',
]

def to(T: type) -> UnaryFn:
    """Return a unary function that casts its argument to `T`"""
    return UnaryFn(T)

def apply(fn: Callable[[Any], Any]) -> UnaryFn:
    """Return a unary function that applies `fn` to its argument"""
    def __inner(arg: Any) -> Any:
        return fn(arg)
    return UnaryFn(__inner)

def partial(fn: Callable[[Any], Any], projector: Callable[[Any], Any]) -> UnaryFn:
    """Return a unary function that applies `fn` parameterized by `projector(arg)` to `arg`"""
    def __inner(arg: Any) -> Any:
        return fn(projector(arg))(arg)
    return UnaryFn(__inner)

def identity() -> UnaryFn:
    """Return a unary function that returns its argument unchanged"""
    def __inner(arg: Any) -> Any:
        return arg
    return UnaryFn(__inner)
