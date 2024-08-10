import builtins as __builtins
import functools as __functools
import itertools as __itertools
from collections import defaultdict as __defaultdict
from collections.abc import Iterable as __Iterable
from collections.abc import Reversible as __Reversible
from collections.abc import Sequence as __Sequence
from typing import Any as __Any
from typing import Callable as __Callable
from typing import Sized as __Sized
from typing import Union as __Union

from ..classes import UnaryFn as __UnaryFn
from ..utility import comparator_to_key as __comparator_to_key
from . import operators as __op

__UNDEFINED = object()

__all__ = [
    'map',
    'filter',
    'filter_not',
    'partition',
    'padded_partition',
    'split_every',
    'group_by',
    'take',
    'drop',
    'distinct',
    'sort',
    'reverse',
    'cycle',
    'enumerate',
    'reduce',
    'scan',
    'prefixes',
    'suffixes',
    'count',
    'count_if',
    'index',
    'index_if',
    'indices',
    'indices_if',
    'sum',
    'product',
    'min',
    'max',
    'all',
    'any',
    'none',
    'first',
    'last',
    'pick',
    'head',
    'tail',
    'tally',
    'sliding',
    'sliding_map',
    'sliding_filter',
    'sliding_filter_not',
    'sliding_reduce',
    'sliding_scan',
]

def map(mapper: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Apply `mapper` to each element"""
    def __inner(arg: __Iterable):
        return __builtins.map(mapper, arg)
    return __UnaryFn(__inner)

def filter(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Keep elements for which `predicate` returns true"""
    def __inner(arg: __Iterable):
        return __builtins.filter(predicate, arg)
    return __UnaryFn(__inner)

def filter_not(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Keep elements for which `predicate` returns false"""
    def __inner(arg: __Iterable):
        return __itertools.filterfalse(predicate, arg)
    return __UnaryFn(__inner)

def partition(size: int) -> __UnaryFn:
    """Return elements in groups of given `size`, discard extra elements"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return zip(*its)
    return __UnaryFn(__inner)

def padded_partition(size: int, fill_value: __Any = None) -> __UnaryFn:
    """Return elements in groups of given `size`, fill missing elements with `fill_value`"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return __itertools.zip_longest(*its, fillvalue = fill_value)
    return __UnaryFn(__inner)

def split_every(size: int) -> __UnaryFn:
    """Return elements in groups of given `size`, return remaining elements in smaller group"""
    def __inner(arg: __Iterable):
        it = iter(arg)
        while piece := tuple(__itertools.islice(it, size)):
            yield piece
    return __UnaryFn(__inner)

def group_by(selector: __Callable[[__Any], __Any]):
    """Return elements in groups for which `selector` returns the same value"""
    def __inner(arg: __Iterable):
        groups = __defaultdict(list)
        for item in arg:
            groups[selector(item)].append(item)
        for item in groups.values():
            yield tuple(item)
    return __UnaryFn(__inner)

def take(count: int) -> __UnaryFn:
    """Return first `count` elements"""
    def __inner(arg: __Iterable):
        return __itertools.islice(arg, None, count)
    return __UnaryFn(__inner)

def drop(count: int) -> __UnaryFn:
    """Return all but first `count` elements"""
    def __inner(arg: __Iterable):
        return __itertools.islice(arg, count, None)
    return __UnaryFn(__inner)

def distinct() -> __UnaryFn:
    """Return distinct (unique) elements"""
    def __inner(arg: __Iterable):
        cache = set()
        for item in arg:
            if item not in cache:
                cache.add(item)
                yield item
    return __UnaryFn(__inner)

def sort(comparator: __Callable[[__Any, __Any], bool]) -> __UnaryFn:
    """Return elements sorted with given `comparator`"""
    def __inner(arg: __Iterable):
        return sorted(arg, key = __comparator_to_key(comparator))
    return __UnaryFn(__inner)

def reverse() -> __UnaryFn:
    """Return elements in reversed order"""
    def __inner(arg: __Reversible):
        return __builtins.reversed(arg)
    return __UnaryFn(__inner)

def cycle() -> __UnaryFn:
    """Return elements indefinitely"""
    def __inner(arg: __Iterable):
        return __itertools.cycle(arg)
    return __UnaryFn(__inner)

def enumerate(start: int = 0) -> __UnaryFn:
    """Return (index, element) pair for each element"""
    def __inner(arg: __Iterable):
        return __builtins.enumerate(arg, start)
    return __UnaryFn(__inner)

def reduce(reducer: __Callable[[__Any, __Any], __Any], init: __Any = __UNDEFINED) -> __UnaryFn:
    """Reduce all elements with `reducer` and optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __functools.reduce(reducer, arg)
        else:
            return __functools.reduce(reducer, arg, init)
    return __UnaryFn(__inner)

def scan(reducer: __Callable[[__Any, __Any], __Any], init: __Any = __UNDEFINED) -> __UnaryFn:
    """Reduce each prefix with `reducer` and optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __itertools.accumulate(arg, reducer)
        else:
            return __itertools.accumulate(arg, reducer, initial = init)
    return __UnaryFn(__inner)

def prefixes() -> __UnaryFn:
    """Return all prefixes"""
    def __inner(arg: __Sequence):
        for size in __builtins.range(1, len(arg) + 1):
            yield tuple(__itertools.islice(arg, None, size))
    return __UnaryFn(__inner)

def suffixes() -> __UnaryFn:
    """Return all suffixes"""
    def __inner(arg: __Sequence):
        for size in __builtins.range(len(arg), 0, -1):
            yield tuple(__itertools.islice(arg, None, size))
    return __UnaryFn(__inner)

def count(value: __Any) -> __UnaryFn:
    """Return number of elements that are equal to given `value`"""
    def __inner(arg: __Iterable):
        return __builtins.sum(1 for item in arg if item == value)
    return __UnaryFn(__inner)

def count_if(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return number of elements that satisfy given `predicate`"""
    def __inner(arg: __Iterable):
        return __builtins.sum(1 for item in arg if predicate(item))
    return __UnaryFn(__inner)

def index(value: __Any, invalid_idx: __Any = -1) -> __UnaryFn:
    """Return index of the first element that is equal to given `value`, `invalid_idx` otherwise"""
    def __inner(arg: __Iterable):
        for i, v in __builtins.enumerate(arg):
            if value == v:
                return i
        return invalid_idx
    return __UnaryFn(__inner)

def index_if(predicate: __Callable[[__Any], bool], invalid_idx: __Any = -1) -> __UnaryFn:
    """Return index of the first element that satisfies given `predicate`, `invalid_idx` otherwise"""
    def __inner(arg: __Iterable):
        for i, v in __builtins.enumerate(arg):
            if predicate(v):
                return i
        return invalid_idx
    return __UnaryFn(__inner)

def indices(value: __Any) -> __UnaryFn:
    """Return indices of all elements that are equal to given `value`"""
    def __inner(arg: __Iterable):
        for i, v in __builtins.enumerate(arg):
            if value == v:
                yield i
    return __UnaryFn(__inner)

def indices_if(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return indices of all elements that satisfy given `predicate`"""
    def __inner(arg: __Iterable):
        for i, v in __builtins.enumerate(arg):
            if predicate(v):
                yield i
    return __UnaryFn(__inner)

def sum(init: int = 0) -> __UnaryFn:
    """Return sum of all elements with optional `init` value"""
    return reduce(__op.add, init)

def product(init: int = 1) -> __UnaryFn:
    """Return product of all elements with optional `init` value"""
    return reduce(__op.mul, init)

def min() -> __UnaryFn:
    """Return minimum element"""
    def __inner(arg: __Iterable):
        return __builtins.min(arg)
    return __UnaryFn(__inner)

def max() -> __UnaryFn:
    """Return maximum element"""
    def __inner(arg: __Iterable):
        return __builtins.max(arg)
    return __UnaryFn(__inner)

def all() -> __UnaryFn:
    """Return true if all elements are truthy"""
    def __inner(arg: __Iterable):
        return __builtins.all(arg)
    return __UnaryFn(__inner)

def any() -> __UnaryFn:
    """Return true if any element is truthy"""
    def __inner(arg: __Iterable):
        return __builtins.any(arg)
    return __UnaryFn(__inner)

def none() -> __UnaryFn:
    """Return true if none element is truthy"""
    def __inner(arg: __Iterable):
        return not __builtins.any(arg)
    return __UnaryFn(__inner)

def first() -> __UnaryFn:
    """Return first element"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[0]
        except:
            for item in arg:
                return item
    return __UnaryFn(__inner)

def last() -> __UnaryFn:
    """Return last element"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[-1]
        except:
            for item in arg:
                pass
            return item
    return __UnaryFn(__inner)

def pick(index: int) -> __UnaryFn:
    """Return nth element"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[index]
        except:
            for i, v in __builtins.enumerate(arg):
                if i == index:
                    return v
    return __UnaryFn(__inner)

def head() -> __UnaryFn:
    """Return head (first) element"""
    return first()

def tail() -> __UnaryFn:
    """Return tail (all but first) elements"""
    def __inner(arg: __Iterable):
        return __itertools.islice(arg, 1, None)
    return __UnaryFn(__inner)

def tally() -> __UnaryFn:
    """Return tally (element count)"""
    def __inner(arg: __Union[__Sized, __Iterable]):
        try:
            return len(arg)
        except:
            return __builtins.sum(1 for _ in arg)
    return __UnaryFn(__inner)

def sliding(size: int) -> __UnaryFn:
    """Return sliding windows of given `size`"""
    def __inner(arg: __Sequence):
        for i in __builtins.range(len(arg) - size + 1):
            yield tuple(__itertools.islice(arg, i, i + size))
    return __UnaryFn(__inner)

def sliding_map(size: int, mapper: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Return `sliding` combined with `map`"""
    return sliding(size) | map(mapper)

def sliding_filter(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding_map` combined with `filter`"""
    return sliding_map(size, filter(predicate))

def sliding_filter_not(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding_map` combined with `filter_not`"""
    return sliding_map(size, filter_not(predicate))

def sliding_reduce(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding_map` combined with `reduce`"""
    return sliding_map(size, reduce(reducer))

def sliding_scan(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding_map` combined with `scan`"""
    return sliding_map(size, scan(reducer))
