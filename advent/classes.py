from __future__ import annotations

from typing import Any as __Any
from typing import Callable as __Callable
from typing import Union as __Union

__all__ = [
    'Undefined',
    'UNDEFINED',
    'NullaryFn',
    'UnaryFn',
    'BinaryFn',
]

class Undefined(): pass
UNDEFINED = Undefined()

class NullaryFn():
    __slots__ = ('name', 'fn')

    def __init__(self, name: str, fn: __Callable[[], __Any]) -> None:
        self.name = name
        self.fn = fn

    def __or__(self, other: UnaryFn) -> NullaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return NullaryFn(f'{self.name} | {other.name}', lambda: other.fn(self.fn()))

    def __call__(self) -> __Any:
        return self.fn()

    def __str__(self) -> str:
        return f'NullaryFn({self.name})'

class UnaryFn():
    __slots__ = ('name', 'fn')

    def __init__(self, name: str, fn: __Callable[[__Any], __Any]) -> None:
        self.name = name
        self.fn = fn

    def __or__(self, other: UnaryFn) -> UnaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return UnaryFn(f'{self.name} | {other.name}', lambda arg: other.fn(self.fn(arg)))

    def __rshift__(self, rhs: __Any) -> NullaryFn:
        return NullaryFn(f'{self.name} >> {rhs}', lambda: self.fn(rhs))

    def __call__(self, arg: __Any) -> __Any:
        return self.fn(arg)

    def __str__(self) -> str:
        return f'UnaryFn({self.name})'

class BinaryFn():
    __slots__ = ('name', 'fn')

    def __init__(self, name: str, fn: __Callable[[__Any, __Any], __Any]) -> None:
        self.name= name
        self.fn = fn

    def __or__(self, other: UnaryFn) -> BinaryFn:
        assert type(other) == UnaryFn, f'Cannot pipe {self} into {other}'
        return BinaryFn(f'{self.name} | {other.name}', lambda lhs, rhs: other.fn(self.fn(lhs, rhs)))

    def __lshift__(self, lhs: __Any) -> UnaryFn:
        return UnaryFn(f'{self.name} << {lhs}', lambda arg: self.fn(lhs, arg))

    def __rshift__(self, rhs: __Any) -> UnaryFn:
        return UnaryFn(f'{self.name} >> {rhs}', lambda arg: self.fn(arg, rhs))

    def __call__(self, lhs: __Any, rhs: __Any) -> __Any:
        return self.fn(lhs, rhs)

    def __str__(self) -> str:
        return f'BinaryFn({self.name})'

AnyFn = __Union[NullaryFn, UnaryFn, BinaryFn]
