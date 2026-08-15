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
    """Return iterator for given `iterable` argument"""
    def __inner():
        return iter(iterable)
    return NullaryFn(__inner)

def range(begin: int, end: int, step: int = 1) -> NullaryFn:
    """Return generator for half-open [ `begin`, `end` ) range with given `step`"""
    def __inner():
        return builtins.range(begin, end, step)
    return NullaryFn(__inner)

def irange(first: int, last: int, step: int = 1) -> NullaryFn:
    """Return generator for inclusive [ `first`, `last` ] range with given `step`"""
    stop = last + (1 if step > 0 else -1)
    def __inner():
        return builtins.range(first, stop, step)
    return NullaryFn(__inner)

def infinite_range(first: int = 0, step: int = 1) -> NullaryFn:
    """Return generator for infinite [ `first`, ∞ ) range with given `step`"""
    def __inner():
        return itertools.count(first, step)
    return NullaryFn(__inner)

def read_input(prompt: str = '') -> NullaryFn:
    """Return content typed by the user"""
    def __inner():
        return input(prompt)
    return NullaryFn(__inner)

def read_file(path: Path | str, encoding: str = 'utf-8') -> NullaryFn:
    """Return content of the file designated by given `path`"""
    def __inner():
        with open(path, 'r', encoding=encoding) as file:
            return file.read()
    return NullaryFn(__inner)

def read_file_lines(path: Path | str, encoding: str = 'utf-8') -> NullaryFn:
    """Return lines of the file designated by given `path`"""
    def __inner():
        with open(path, 'r', encoding=encoding) as file:
            return file.read().splitlines()
    return NullaryFn(__inner)
