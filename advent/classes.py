from __future__ import annotations

from typing import Any, Callable, TypeAlias

__all__ = [
    'NullaryFn',
    'UnaryFn',
    'BinaryFn',
    'AnyFn',
]

class NullaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: Callable[[], Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn | Callable[[Any], Any]) -> NullaryFn:
        return NullaryFn(lambda: other(self()))

    def __call__(self) -> Any:
        return self.fn()

    def __repr__(self) -> str:
        return f"NullaryFn({self.fn!r})"

class UnaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: Callable[[Any], Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn | Callable[[Any], Any]) -> UnaryFn:
        return UnaryFn(lambda arg: other(self(arg)))

    def __call__(self, arg: Any) -> Any:
        return self.fn(arg)

    def bind(self, rhs: Any) -> NullaryFn:
        return NullaryFn(lambda: self(rhs))

    def __repr__(self) -> str:
        return f"UnaryFn({self.fn!r})"

class BinaryFn:
    __slots__ = ('fn',)

    def __init__(self, fn: Callable[[Any, Any], Any]) -> None:
        self.fn = fn

    def __or__(self, other: UnaryFn | Callable[[Any], Any]) -> BinaryFn:
        return BinaryFn(lambda lhs, rhs: other(self(lhs, rhs)))

    def __call__(self, lhs: Any, rhs: Any) -> Any:
        return self.fn(lhs, rhs)

    def left(self, lhs: Any) -> UnaryFn:
        return UnaryFn(lambda arg: self(lhs, arg))

    def right(self, rhs: Any) -> UnaryFn:
        return UnaryFn(lambda arg: self(arg, rhs))

    def flip(self) -> BinaryFn:
        return BinaryFn(lambda lhs, rhs: self(rhs, lhs))

    def __repr__(self) -> str:
        return f"BinaryFn({self.fn!r})"

AnyFn: TypeAlias = NullaryFn | UnaryFn | BinaryFn
