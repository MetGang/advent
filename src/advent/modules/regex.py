import re
from typing import Any

from ..classes import UnaryFn

__all__ = [
    'split',
    'replace',
    'find_all',
    'find_first',
    'find_last',
]

def split(pattern: str | re.Pattern[str], limit: int = 0) -> UnaryFn:
    """
    Return list of substrings split by occurrences matching `pattern`.

    >>> split(r',\\s*')('one, two,three')
    ['one', 'two', 'three']
    >>> split(r',', 1)('one,two,three')
    ['one', 'two,three']
    """
    def __inner(s: str) -> list[str | Any]:
        return re.split(pattern, s, maxsplit=limit)
    return UnaryFn(__inner)

def replace(pattern: str | re.Pattern[str], new: str) -> UnaryFn:
    """
    Return string with all occurrences matching `pattern` replaced by `new`.

    >>> replace(r'\\d+', '#')('item 12 costs 34')
    'item # costs #'
    >>> replace(r'cat', 'dog')('cat and cat')
    'dog and dog'
    """
    def __inner(s: str) -> str:
        return re.sub(pattern, new, s)
    return UnaryFn(__inner)

def find_all(pattern: str | re.Pattern[str]) -> UnaryFn:
    """
    Return list of all occurrences matching `pattern`.

    >>> find_all(r'\\d+')('a12b34')
    ['12', '34']
    >>> find_all(r'(\\w+)@(\\w+\\.\\w+)')('a@example.com')
    [('a', 'example.com')]
    """
    def __inner(s: str) -> list[Any]:
        return re.findall(pattern, s)
    return UnaryFn(__inner)

def find_first(pattern: str | re.Pattern[str]) -> UnaryFn:
    """
    Return first occurrence matching `pattern`, or None if not found.

    >>> find_first(r'\\d+')('a12b34')
    '12'
    >>> find_first(r'(\\w+)@(\\w+\\.\\w+)')('a@example.com')
    ('a', 'example.com')
    >>> find_first(r'xyz')('hello')
    """
    def __inner(s: str) -> Any:
        match = re.search(pattern, s)
        if not match:
            return None
        groups = match.groups()
        if not groups:
            return match.group(0)
        return groups[0] if len(groups) == 1 else groups
    return UnaryFn(__inner)

def find_last(pattern: str | re.Pattern[str]) -> UnaryFn:
    """
    Return last occurrence matching `pattern`, or None if not found.

    >>> find_last(r'\\d+')('a12b34')
    '34'
    >>> find_last(r'(\\w+)@(\\w+\\.\\w+)')('a@example.com b@test.org')
    ('b', 'test.org')
    >>> find_last(r'xyz')('hello')
    """
    def __inner(s: str) -> Any:
        matches = re.findall(pattern, s)
        return matches[-1] if matches else None
    return UnaryFn(__inner)
