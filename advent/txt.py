import functools as __functools
from collections.abc import Iterable as __Iterable

from .classes import UnaryFn as __UnaryFn

__MODULE_NAME = 'txt'

__all__ = [
    'join',
    'trim',
    'trim_left',
    'trim_right',
    'split',
    'replace',
    'replace_many',
]

def join(connector: str) -> __UnaryFn:
    """Concatenate iterable of strings with given `connector`"""
    def __inner(iterable: __Iterable[str]) -> str:
        return connector.join(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.join', __inner)

def trim() -> __UnaryFn:
    """Return string with leading and trailing whitespace removed"""
    def __inner(s: str) -> str:
        return s.strip()
    return __UnaryFn(f'{__MODULE_NAME}.trim', __inner)

def trim_left() -> __UnaryFn:
    """Return string with leading whitespace removed"""
    def __inner(s: str) -> str:
        return s.lstrip()
    return __UnaryFn(f'{__MODULE_NAME}.trim_left', __inner)

def trim_right() -> __UnaryFn:
    """Return string with trailing whitespace removed"""
    def __inner(s: str) -> str:
        return s.rstrip()
    return __UnaryFn(f'{__MODULE_NAME}.trim_right', __inner)

def split(separator: str, limit: int = -1) -> __UnaryFn:
    """Return generator of the substrings in the string split by `separator` up to the `limit`"""
    def __inner(s: str) -> str:
        return (item for item in s.split(separator, limit))
    return __UnaryFn(f'{__MODULE_NAME}.split', __inner)

def replace(old: str, new: str) -> __UnaryFn:
    """Return string with all occurrences of substring `old` replaced by `new`"""
    def __inner(s: str) -> str:
        return s.replace(old, new)
    return __UnaryFn(f'{__MODULE_NAME}.replace', __inner)

def replace_many(olds: list[str], new: str) -> __UnaryFn:
    """Return string with all occurrences of substrings `olds` replaced by `new`"""
    def __inner(s: str) -> str:
        return __functools.reduce(lambda acc, x: acc.replace(x, new), olds, s)
    return __UnaryFn(f'{__MODULE_NAME}.replace_many', __inner)
