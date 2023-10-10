import builtins as __builtins
import itertools as __itertools
from pathlib import Path as __Path
from typing import Any as __Any
from typing import Union as __Union

from .classes import NullaryFn as __NullaryFn

__all__ = [
    'iterate',
    'range',
    'infinite_range',
    'read_file',
]

def iterate(any: __Any) -> __NullaryFn:
    """Return iterator for given `any` argument"""
    def __inner():
        return __builtins.iter(any)
    return __NullaryFn(__inner)

def range(begin: int, end: int, step: int = 1) -> __NullaryFn:
    """Return generator for [ `begin`, `end` ) range with given `step`"""
    def __inner():
        return __builtins.range(begin, end, step)
    return __NullaryFn(__inner)

def infinite_range(first: int = 0, step: int = 1) -> __NullaryFn:
    """Return generator for [ `first`, ∞ ) range with given `step`"""
    def __inner():
        return __itertools.count(first, step)
    return __NullaryFn(__inner)

def read_input() -> __NullaryFn:
    """Return content typed by the user"""
    def __inner():
        return input()
    return __NullaryFn(__inner)

def read_file(path: __Union[__Path, str]) -> __NullaryFn:
    """Return content of the file designated by given `path`"""
    def __inner():
        with open(path, 'r') as file:
            return file.read()
    return __NullaryFn(__inner)
