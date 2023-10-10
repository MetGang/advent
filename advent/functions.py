from typing import Any as __Any
from typing import Callable as __Callable

from .classes import UnaryFn as __UnaryFn

__all__ = [
    'to',
    'apply',
    'identity',
]

def to(T: type) -> __UnaryFn:
    """Return element casted to `T`"""
    return __UnaryFn(T)

def apply(callable: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Return result of `callable`(element)"""
    def __inner(arg: __Any):
        return callable(arg)
    return __UnaryFn(__inner)

def identity() -> __UnaryFn:
    """Return itself"""
    def __inner(arg: __Any):
        return arg
    return __UnaryFn(__inner)
