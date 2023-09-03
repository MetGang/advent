import builtins as __builtins
import itertools as __itertools
from pathlib import Path as __Path
from typing import Any as __Any
from typing import Union as __Union

from .classes import NullaryFn as __NullaryFn

__MODULE_NAME = 'gn'

__all__ = [
    'iterate',
    'range',
    'irange',
    'infinite_range',
    'read_file',
]

def iterate(any: __Any) -> __NullaryFn:
    """Return iterator for the given `any` argument"""
    def __inner():
        return __builtins.iter(any)
    return __NullaryFn(f'{__MODULE_NAME}.iterate', __inner)

def range(begin: int, end: int, step: int = 1) -> __NullaryFn:
    """Return generator for [ `begin`, `end` ) range with given `step`"""
    def __inner():
        return __builtins.range(begin, end, step)
    return __NullaryFn(f'{__MODULE_NAME}.range', __inner)

def irange(first: int, last: int, step: int = 1) -> __NullaryFn:
    """Return generator for [ `first`, `last` ] range with given `step`"""
    def __inner():
        return __builtins.range(first, last + 1, step)
    return __NullaryFn(f'{__MODULE_NAME}.irange', __inner)

def infinite_range(first: int = 0, step: int = 1) -> __NullaryFn:
    """Return generator for [ `first`, ∞ ) range with given `step`"""
    def __inner():
        return __itertools.count(first, step)
    return __NullaryFn(f'{__MODULE_NAME}.infinite_range', __inner)

def read_file(path: __Union[__Path, str]) -> __NullaryFn:
    """Return content of the file `path` as string"""
    def __inner():
        with open(path, 'r') as file:
            return file.read()
    return __NullaryFn(f'{__MODULE_NAME}.read_file', __inner)
