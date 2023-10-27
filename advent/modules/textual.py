from collections.abc import Iterable as __Iterable

from ..classes import UnaryFn as __UnaryFn

__all__ = [
    'join',
    'trim',
    'trim_left',
    'trim_right',
    'split',
    'replace',
    'contains',
    'starts_with',
    'ends_with',
]

def join(connector: str) -> __UnaryFn:
    """Concatenate iterable of strings with given `connector`"""
    def __inner(iterable: __Iterable[str]) -> str:
        return connector.join(iterable)
    return __UnaryFn(__inner)

def trim() -> __UnaryFn:
    """Return string with leading and trailing whitespace removed"""
    def __inner(s: str) -> str:
        return s.strip()
    return __UnaryFn(__inner)

def trim_left() -> __UnaryFn:
    """Return string with leading whitespace removed"""
    def __inner(s: str) -> str:
        return s.lstrip()
    return __UnaryFn(__inner)

def trim_right() -> __UnaryFn:
    """Return string with trailing whitespace removed"""
    def __inner(s: str) -> str:
        return s.rstrip()
    return __UnaryFn(__inner)

def split(separator: str, limit: int = -1) -> __UnaryFn:
    """Return generator of the substrings in the string split by `separator` up to the `limit` without empty splits"""
    def __inner(s: str) -> str:
        return (item for item in s.split(separator, limit))
    return __UnaryFn(__inner)

def replace(old: str, new: str) -> __UnaryFn:
    """Return string with all occurrences of substring `old` replaced by `new`"""
    def __inner(s: str) -> str:
        return s.replace(old, new)
    return __UnaryFn(__inner)

def substring(position: int, size: int) -> __UnaryFn:
    """Return substring starting at `position` with given `size`"""
    def __inner(s: str) -> str:
        return s[position:position + size]
    return __UnaryFn(__inner)

def contains(substring: str) -> __UnaryFn:
    """Check whether string contains given `substring`"""
    def __inner(s: str) -> str:
        return substring in s
    return __UnaryFn(__inner)

def starts_with(substring: str) -> __UnaryFn:
    """Check whether string starts with given `substring`"""
    def __inner(s: str) -> str:
        return s.startswith(substring)
    return __UnaryFn(__inner)

def ends_with(substring: str) -> __UnaryFn:
    """Check whether string ends with given `substring`"""
    def __inner(s: str) -> str:
        return s.endswith(substring)
    return __UnaryFn(__inner)
