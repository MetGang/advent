import re as __re

from ..classes import UnaryFn as __UnaryFn

def split(pattern: str, limit: int = 0) -> __UnaryFn:
    """_"""
    def __inner(s: str) -> str:
        return (item for item in __re.split(pattern, s, limit))
    return __UnaryFn(__inner)

def replace(pattern: str, new: str) -> __UnaryFn:
    """Return string with all occurrences matching `pattern` replaced by `new`"""
    def __inner(s: str) -> str:
        return __re.sub(pattern, new, s)
    return __UnaryFn(__inner)

def find_all(pattern: str) -> __UnaryFn:
    """_"""
    def __inner(s: str) -> str:
        return (item for item in __re.findall(pattern, s))
    return __UnaryFn(__inner)
