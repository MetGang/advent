from __future__ import annotations

from typing import Any as __Any
from typing import Callable as __Callable
from typing import Union as __Union

__all__ = [
    'NullaryFn',
    'UnaryFn',
    'BinaryFn',
    'AnyFn',
]

class NullaryFn():
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn) -> NullaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return NullaryFn(lambda: other.fn(self.fn()))

    def __call__(self) -> __Any:
        return self.fn()

class UnaryFn():
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[__Any], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn) -> UnaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return UnaryFn(lambda arg: other.fn(self.fn(arg)))

    def __rshift__(self, rhs: __Any) -> NullaryFn:
        return NullaryFn(lambda: self.fn(rhs))

    def __call__(self, arg: __Any) -> __Any:
        return self.fn(arg)

class BinaryFn():
    __slots__ = ('fn',)

    def __init__(self, fn: __Callable[[__Any, __Any], __Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn) -> BinaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return BinaryFn(lambda lhs, rhs: other.fn(self.fn(lhs, rhs)))

    def __lshift__(self, lhs: __Any) -> UnaryFn:
        return UnaryFn(lambda arg: self.fn(lhs, arg))

    def __rshift__(self, rhs: __Any) -> UnaryFn:
        return UnaryFn(lambda arg: self.fn(arg, rhs))

    def __call__(self, lhs: __Any, rhs: __Any) -> __Any:
        return self.fn(lhs, rhs)

AnyFn = __Union[NullaryFn, UnaryFn, BinaryFn]
