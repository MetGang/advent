from __future__ import annotations

from typing import Any as __Any
from typing import Callable as __Callable
from typing import TypeAlias as __TypeAlias
from typing import Union as __Union

__all__ = [
    'NullaryFn',
    'UnaryFn',
    'BinaryFn',
    'AnyFn',
]

class NullaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: __Union[UnaryFn, __Callable[[__Any], __Any]]) -> NullaryFn:
        return NullaryFn(lambda: other.__call__(self.__call__()))

    def __call__(self) -> __Any:
        return self.fn()

class UnaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[__Any], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: __Union[UnaryFn, __Callable[[__Any], __Any]]) -> UnaryFn:
        return UnaryFn(lambda arg: other.__call__(self.__call__(arg)))

    def __rshift__(self, rhs: __Any) -> NullaryFn:
        return NullaryFn(lambda: self.__call__(rhs))

    def __call__(self, arg: __Any) -> __Any:
        return self.fn(arg)

class BinaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[__Any, __Any], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: __Union[UnaryFn, __Callable[[__Any], __Any]]) -> BinaryFn:
        return BinaryFn(lambda lhs, rhs: other.__call__(self.__call__(lhs, rhs)))

    def __lshift__(self, lhs: __Any) -> UnaryFn:
        return UnaryFn(lambda arg: self.__call__(lhs, arg))

    def __rshift__(self, rhs: __Any) -> UnaryFn:
        return UnaryFn(lambda arg: self.__call__(arg, rhs))

    def __call__(self, lhs: __Any, rhs: __Any) -> __Any:
        return self.fn(lhs, rhs)

AnyFn: __TypeAlias = __Union[NullaryFn, UnaryFn, BinaryFn]
