import re as __re

from ..classes import UnaryFn as __UnaryFn

__all__ = [
    'regex_split',
    'regex_replace',
    'regex_find_all',
]

def regex_split(pattern: str, limit: int = 0) -> __UnaryFn:
    """_"""
    def __inner(s: str) -> str:
        return (item for item in __re.split(pattern, s, limit))
    return __UnaryFn(__inner)

def regex_replace(pattern: str, new: str) -> __UnaryFn:
    """Return string with all occurrences matching `pattern` replaced by `new`"""
    def __inner(s: str) -> str:
        return __re.sub(pattern, new, s)
    return __UnaryFn(__inner)

def regex_find_all(pattern: str) -> __UnaryFn:
    """_"""
    def __inner(s: str) -> str:
        return (item for item in __re.findall(pattern, s))
    return __UnaryFn(__inner)
