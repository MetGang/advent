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
    """
    Concatenate an iterable of strings with a given connector.

    >>> join(', ')(['apple', 'banana', 'cherry'])
    'apple, banana, cherry'
    >>> join('-')([])
    ''
    """
    def __inner(iterable: Iterable[str]) -> str:
        return connector.join(iterable)
    return UnaryFn(__inner)

def trim(chars: str | None = None) -> UnaryFn:
    """
    Return string with leading and trailing characters removed.

    >>> trim()('  hello  ')
    'hello'
    >>> trim('-')('---hello---')
    'hello'
    """
    def __inner(s: str) -> str:
        return s.strip(chars)
    return UnaryFn(__inner)

def trim_left(chars: str | None = None) -> UnaryFn:
    """
    Return string with leading characters removed.

    >>> trim_left()('  hello  ')
    'hello  '
    >>> trim_left('-')('---hello---')
    'hello---'
    """
    def __inner(s: str) -> str:
        return s.lstrip(chars)
    return UnaryFn(__inner)

def trim_right(chars: str | None = None) -> UnaryFn:
    """
    Return string with trailing characters removed.

    >>> trim_right()('  hello  ')
    '  hello'
    >>> trim_right('-')('---hello---')
    '---hello'
    """
    def __inner(s: str) -> str:
        return s.rstrip(chars)
    return UnaryFn(__inner)

def split(limit: int = -1) -> UnaryFn:
    """
    Return substrings split by whitespace.

    >>> split()('one two  three')
    ['one', 'two', 'three']
    >>> split(1)('one two three')
    ['one', 'two three']
    """
    def __inner(s: str) -> list[str]:
        return s.split(None, limit)
    return UnaryFn(__inner)

def split_by(separator: str, limit: int = -1) -> UnaryFn:
    """
    Return substrings split by a separator.

    >>> split_by(',')('one,two,three')
    ['one', 'two', 'three']
    >>> split_by(',', 1)('one,two,three')
    ['one', 'two,three']
    """
    def __inner(s: str) -> list[str]:
        return s.split(separator, limit)
    return UnaryFn(__inner)

def replace(old: str, new: str, count: int = -1) -> UnaryFn:
    """
    Return string with occurrences replaced.

    >>> replace('cat', 'dog')('cat and cat')
    'dog and dog'
    >>> replace('cat', 'dog', 1)('cat and cat')
    'dog and cat'
    """
    def __inner(s: str) -> str:
        return s.replace(old, new, count)
    return UnaryFn(__inner)

def substring(position: int, size: int | None = None) -> UnaryFn:
    """
    Return a substring starting at position.

    >>> substring(2)('abcdef')
    'cdef'
    >>> substring(2, 3)('abcdef')
    'cde'
    """
    def __inner(s: str) -> str:
        if size is None:
            return s[position:]
        return s[position:position + size]
    return UnaryFn(__inner)

def contains(sub: str) -> UnaryFn:
    """
    Check whether a string contains a substring.

    >>> contains('ell')('hello')
    True
    >>> contains('xyz')('hello')
    False
    """
    def __inner(s: str) -> bool:
        return sub in s
    return UnaryFn(__inner)

def starts_with(prefix: str | tuple[str, ...]) -> UnaryFn:
    """
    Check whether a string starts with a prefix.

    >>> starts_with('he')('hello')
    True
    >>> starts_with(('hi', 'he'))('hello')
    True
    """
    def __inner(s: str) -> bool:
        return s.startswith(prefix)
    return UnaryFn(__inner)

def ends_with(suffix: str | tuple[str, ...]) -> UnaryFn:
    """
    Check whether a string ends with a suffix.

    >>> ends_with('lo')('hello')
    True
    >>> ends_with(('en', 'lo'))('hello')
    True
    """
    def __inner(s: str) -> bool:
        return s.endswith(suffix)
    return UnaryFn(__inner)

def is_space() -> UnaryFn:
    """
    Check whether a string contains only whitespace.

    >>> is_space()('   ')
    True
    >>> is_space()(' x ')
    False
    """
    def __inner(s: str) -> bool:
        return s.isspace()
    return UnaryFn(__inner)

def is_alnum() -> UnaryFn:
    """
    Check whether a string contains only alphanumeric characters.

    >>> is_alnum()('abc123')
    True
    >>> is_alnum()('abc 123')
    False
    """
    def __inner(s: str) -> bool:
        return s.isalnum()
    return UnaryFn(__inner)

def is_alpha() -> UnaryFn:
    """
    Check whether a string contains only alphabetic characters.

    >>> is_alpha()('hello')
    True
    >>> is_alpha()('hello2')
    False
    """
    def __inner(s: str) -> bool:
        return s.isalpha()
    return UnaryFn(__inner)

def is_upper() -> UnaryFn:
    """
    Check whether a string is uppercase.

    >>> is_upper()('HELLO')
    True
    >>> is_upper()('Hello')
    False
    """
    def __inner(s: str) -> bool:
        return s.isupper()
    return UnaryFn(__inner)

def is_lower() -> UnaryFn:
    """
    Check whether a string is lowercase.

    >>> is_lower()('hello')
    True
    >>> is_lower()('Hello')
    False
    """
    def __inner(s: str) -> bool:
        return s.islower()
    return UnaryFn(__inner)

def is_digit() -> UnaryFn:
    """
    Check whether a string contains only digits.

    >>> is_digit()('12345')
    True
    >>> is_digit()('12.5')
    False
    """
    def __inner(s: str) -> bool:
        return s.isdigit()
    return UnaryFn(__inner)

def is_ascii() -> UnaryFn:
    """
    Check whether a string contains only ASCII characters.

    >>> is_ascii()('hello!')
    True
    >>> is_ascii()('café')
    False
    """
    def __inner(s: str) -> bool:
        return s.isascii()
    return UnaryFn(__inner)
