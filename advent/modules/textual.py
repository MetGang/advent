from collections.abc import Iterable

from ..classes import UnaryFn

__all__ = [
    'join',
    'trim',
    'trim_left',
    'trim_right',
    'split',
    'split_by',
    'replace',
    'substring',
    'contains',
    'starts_with',
    'ends_with',
    'is_space',
    'is_alnum',
    'is_alpha',
    'is_upper',
    'is_lower',
    'is_digit',
    'is_ascii',
]

def join(connector: str) -> UnaryFn:
    """Concatenate iterable of strings with given `connector`"""
    def __inner(iterable: Iterable[str]) -> str:
        return connector.join(iterable)
    return UnaryFn(__inner)

def trim(chars: str | None = None) -> UnaryFn:
    """Return string with leading and trailing characters (whitespace by default) removed"""
    def __inner(s: str) -> str:
        return s.strip(chars)
    return UnaryFn(__inner)

def trim_left(chars: str | None = None) -> UnaryFn:
    """Return string with leading characters (whitespace by default) removed"""
    def __inner(s: str) -> str:
        return s.lstrip(chars)
    return UnaryFn(__inner)

def trim_right(chars: str | None = None) -> UnaryFn:
    """Return string with trailing characters (whitespace by default) removed"""
    def __inner(s: str) -> str:
        return s.rstrip(chars)
    return UnaryFn(__inner)

def split(limit: int = -1) -> UnaryFn:
    """Return substrings of the string split by whitespaces up to the `limit` without empty splits"""
    def __inner(s: str) -> list[str]:
        return s.split(None, limit)
    return UnaryFn(__inner)

def split_by(separator: str, limit: int = -1) -> UnaryFn:
    """Return substrings of the string split by `separator` up to the `limit`"""
    def __inner(s: str) -> list[str]:
        return s.split(separator, limit)
    return UnaryFn(__inner)

def replace(old: str, new: str, count: int = -1) -> UnaryFn:
    """Return string with occurrences of substring `old` replaced by `new` up to `count` times"""
    def __inner(s: str) -> str:
        return s.replace(old, new, count)
    return UnaryFn(__inner)

def substring(position: int, size: int | None = None) -> UnaryFn:
    """Return substring starting at `position` with given `size` (or to the end if None)"""
    def __inner(s: str) -> str:
        if size is None:
            return s[position:]
        return s[position:position + size]
    return UnaryFn(__inner)

def contains(sub: str) -> UnaryFn:
    """Check whether string contains given substring `sub`"""
    def __inner(s: str) -> bool:
        return sub in s
    return UnaryFn(__inner)

def starts_with(prefix: str | tuple[str, ...]) -> UnaryFn:
    """Check whether string starts with given `prefix` (or tuple of prefixes)"""
    def __inner(s: str) -> bool:
        return s.startswith(prefix)
    return UnaryFn(__inner)

def ends_with(suffix: str | tuple[str, ...]) -> UnaryFn:
    """Check whether string ends with given `suffix` (or tuple of suffixes)"""
    def __inner(s: str) -> bool:
        return s.endswith(suffix)
    return UnaryFn(__inner)

def is_space() -> UnaryFn:
    """Check whether string is composed of whitespace characters"""
    def __inner(s: str) -> bool:
        return s.isspace()
    return UnaryFn(__inner)

def is_alnum() -> UnaryFn:
    """Check whether string is composed of alphanumeric characters"""
    def __inner(s: str) -> bool:
        return s.isalnum()
    return UnaryFn(__inner)

def is_alpha() -> UnaryFn:
    """Check whether string is composed of alpha characters"""
    def __inner(s: str) -> bool:
        return s.isalpha()
    return UnaryFn(__inner)

def is_upper() -> UnaryFn:
    """Check whether string is composed of uppercase characters"""
    def __inner(s: str) -> bool:
        return s.isupper()
    return UnaryFn(__inner)

def is_lower() -> UnaryFn:
    """Check whether string is composed of lowercase characters"""
    def __inner(s: str) -> bool:
        return s.islower()
    return UnaryFn(__inner)

def is_digit() -> UnaryFn:
    """Check whether string is composed of digit characters"""
    def __inner(s: str) -> bool:
        return s.isdigit()
    return UnaryFn(__inner)

def is_ascii() -> UnaryFn:
    """Check whether string is composed of ascii characters"""
    def __inner(s: str) -> bool:
        return s.isascii()
    return UnaryFn(__inner)
