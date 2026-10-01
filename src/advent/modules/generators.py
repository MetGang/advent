import builtins
import itertools
from pathlib import Path
from typing import Any

from ..classes import NullaryFn

__all__ = [
    'iterate',
    'range',
    'irange',
    'infinite_range',
    'read_input',
    'read_file',
    'read_file_lines',
]

def iterate(iterable: Any) -> NullaryFn:
    """
    Return an iterator for the given `iterable`.

    >>> list(iterate([1, 2, 3])())
    [1, 2, 3]
    """
    def __inner():
        return iter(iterable)
    return NullaryFn(__inner)

def range(begin: int, end: int, step: int = 1) -> NullaryFn:
    """
    Return a generator for the half-open [`begin`, `end`) range.

    >>> list(range(1, 5)())
    [1, 2, 3, 4]
    >>> list(range(5, 0, -2)())
    [5, 3, 1]
    """
    def __inner():
        return builtins.range(begin, end, step)
    return NullaryFn(__inner)

def irange(first: int, last: int, step: int = 1) -> NullaryFn:
    """
    Return a generator for the inclusive [`first`, `last`] range.

    >>> list(irange(1, 5)())
    [1, 2, 3, 4, 5]
    >>> list(irange(5, 1, -2)())
    [5, 3, 1]
    """
    stop = last + (1 if step > 0 else -1)
    def __inner():
        return builtins.range(first, stop, step)
    return NullaryFn(__inner)

def infinite_range(first: int = 0, step: int = 1) -> NullaryFn:
    """
    Return an infinite range generator.

    >>> list(itertools.islice(infinite_range(2, 3)(), 4))
    [2, 5, 8, 11]
    """
    def __inner():
        return itertools.count(first, step)
    return NullaryFn(__inner)

def read_input(prompt: str = '') -> NullaryFn:
    """
    Return content typed by the user.

    >>> from unittest.mock import patch
    >>> with patch('builtins.input', return_value='answer'):
    ...     read_input('Answer: ')()
    'answer'
    """
    def __inner():
        return input(prompt)
    return NullaryFn(__inner)

def read_file(path: Path | str, encoding: str = 'utf-8') -> NullaryFn:
    """
    Return content of the file designated by `path`.

    >>> from unittest.mock import mock_open, patch
    >>> with patch('builtins.open', mock_open(read_data='hello')):
    ...     read_file('example.txt')()
    'hello'
    """
    def __inner():
        with open(path, 'r', encoding=encoding) as file:
            return file.read()
    return NullaryFn(__inner)

def read_file_lines(path: Path | str, encoding: str = 'utf-8') -> NullaryFn:
    """
    Return lines of the file designated by `path`.

    >>> from unittest.mock import mock_open, patch
    >>> with patch('builtins.open', mock_open(read_data='one\\ntwo\\n')):
    ...     read_file_lines('example.txt')()
    ['one', 'two']
    """
    def __inner():
        with open(path, 'r', encoding=encoding) as file:
            return file.read().splitlines()
    return NullaryFn(__inner)
