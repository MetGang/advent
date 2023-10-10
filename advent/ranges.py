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

from .classes import UnaryFn as __UnaryFn
from .utility import comparator_to_key as __comparator_to_key

__UNDEFINED = object()

__all__ = [
    'map',
    'filter',
    'filter_not',
    'split',
    'split_if',
    'split_every',
    'partition',
    'padded_partition',
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

def split(value: __Any, allow_empty: bool = False) -> __UnaryFn:
    """TODO"""
    def __inner(arg: __Iterable):
        buffer = []
        for item in arg:
            if item == value:
                if buffer or allow_empty:
                    yield tuple(buffer)
                    buffer.clear()
            else:
                buffer.append(item)
    return __UnaryFn(__inner)

def split_if(predicate: __Callable[[__Any], bool], allow_empty: bool = False) -> __UnaryFn:
    """TODO"""
    def __inner(arg: __Iterable):
        buffer = []
        for item in arg:
            if predicate(item):
                if buffer or allow_empty:
                    yield tuple(buffer)
                    buffer.clear()
            else:
                buffer.append(item)
    return __UnaryFn(__inner)

def split_every(size: int) -> __UnaryFn:
    """TODO"""
    def __inner(arg: __Iterable):
        it = iter(arg)
        while piece := tuple(__itertools.islice(it, size)):
            yield piece
    return __UnaryFn(__inner)

def partition(size: int) -> __UnaryFn:
    """Return iterator which yields groups of given `size` of the Iterable, discard extra elements"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return zip(*its)
    return __UnaryFn(__inner)

def padded_partition(size: int, fill_value: __Any) -> __UnaryFn:
    """Return iterator which yields groups of given `size` of the Iterable, fill missing elements with `fill_value`"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return __itertools.zip_longest(*its, fillvalue = fill_value)
    return __UnaryFn(__inner)

def group_by(selector: __Callable[[__Any], __Any]):
    """Return iterator which yields groups of elements for which `selector` returns the same value"""
    def __inner(arg: __Iterable):
        groups = __defaultdict(lambda: list())
        for item in arg:
            groups[selector(item)].append(item)
        for item in groups.values():
            yield tuple(item)
    return __UnaryFn(__inner)

def take(count: int) -> __UnaryFn:
    """Return iterator which yields only first `count` elements of the Iterable"""
    def __inner(iterable: __Iterable):
        return __itertools.islice(iterable, None, count)
    return __UnaryFn(__inner)

def drop(count: int) -> __UnaryFn:
    """Return iterator which yields all but first `count` elements of the Iterable"""
    def __inner(iterable: __Iterable):
        return __itertools.islice(iterable, count, None)
    return __UnaryFn(__inner)

def distinct() -> __UnaryFn:
    """Return generator with distinct (unique) elements of the Iterable"""
    def __inner(arg: __Iterable):
        cache = set()
        for item in arg:
            if item not in cache:
                cache.add(item)
                yield item
    return __UnaryFn(__inner)

def sort(comparator: __Callable[[__Any, __Any], bool]) -> __UnaryFn:
    """Return iterator which yields elements of the Iterable sorted with given `comparator`"""
    def __inner(arg: __Iterable):
        return sorted(arg, key = __comparator_to_key(comparator))
    return __UnaryFn(__inner)

def reverse() -> __UnaryFn:
    """Return iterator which yields elements of the Reversible in reverse order"""
    def __inner(arg: __Reversible):
        return __builtins.reversed(arg)
    return __UnaryFn(__inner)

def cycle() -> __UnaryFn:
    """Return iterator which yields elements of the Iterable indefinitely"""
    def __inner(arg: __Iterable):
        return __itertools.cycle(arg)
    return __UnaryFn(__inner)

def enumerate(start: int = 0) -> __UnaryFn:
    """Return iterator which yields (index, element) pair for each element of the Iterable"""
    def __inner(arg: __Iterable):
        return __builtins.enumerate(arg, start)
    return __UnaryFn(__inner)

def reduce(reducer: __Callable[[__Any, __Any], __Any], init: __Any = __UNDEFINED) -> __UnaryFn:
    """Reduce all elements of the Iterable with `reducer` and optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __functools.reduce(reducer, arg)
        else:
            return __functools.reduce(reducer, arg, init)
    return __UnaryFn(__inner)

def scan(reducer: __Callable[[__Any, __Any], __Any], init: __Any = __UNDEFINED) -> __UnaryFn:
    """Reduce each prefix of the Iterable with `reducer` and optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __itertools.accumulate(arg, reducer)
        else:
            return __itertools.accumulate(arg, reducer, initial = init)
    return __UnaryFn(__inner)

def prefixes() -> __UnaryFn:
    """Return generator which yields all prefixes of the Sequence"""
    def __inner(arg: __Sequence):
        for size in __builtins.range(1, len(arg) + 1):
            yield tuple(__itertools.islice(arg, None, size))
    return __UnaryFn(__inner)

def suffixes() -> __UnaryFn:
    """Return generator which yields all suffixes of the Sequence"""
    def __inner(arg: __Sequence):
        for size in __builtins.range(1, len(arg) + 1):
            yield tuple(__itertools.islice(arg, None, size))
    return __UnaryFn(__inner)

def count(value: __Any) -> __UnaryFn:
    """Return number of elements of the Iterable that are equal to given `value`"""
    def __inner(arg: __Iterable):
        return __builtins.sum(1 for item in arg if item == value)
    return __UnaryFn(__inner)

def count_if(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return number of elements of the Iterable that satisfy given `predicate`"""
    def __inner(arg: __Iterable):
        return __builtins.sum(1 for item in arg if predicate(item))
    return __UnaryFn(__inner)

def sum(init: int = 0) -> __UnaryFn:
    """Return sum of all elements of the Iterable with optional `init` value"""
    return __UnaryFn(reduce(lambda a, b: a + b, init))

def product(init: int = 1) -> __UnaryFn:
    """Return product of all elements of the Iterable with optional `init` value"""
    return __UnaryFn(reduce(lambda a, b: a * b, init))

def min() -> __UnaryFn:
    """Return minimum element from the Iterable"""
    def __inner(iterable: __Iterable):
        return __builtins.min(iterable)
    return __UnaryFn(__inner)

def max() -> __UnaryFn:
    """Return maximum element from the Iterable"""
    def __inner(iterable: __Iterable):
        return __builtins.max(iterable)
    return __UnaryFn(__inner)

def all() -> __UnaryFn:
    """Return true if all elements of the Iterable are truthy"""
    def __inner(iterable: __Iterable):
        return __builtins.all(iterable)
    return __UnaryFn(__inner)

def any() -> __UnaryFn:
    """Return true if any element of the Iterable is truthy"""
    def __inner(iterable: __Iterable):
        return __builtins.any(iterable)
    return __UnaryFn(__inner)

def none() -> __UnaryFn:
    """Return true if none element of the Iterable is truthy"""
    def __inner(iterable: __Iterable):
        return not __builtins.all(iterable)
    return __UnaryFn(__inner)

def first() -> __UnaryFn:
    """Return first element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[0]
        except:
            for item in arg:
                return item
    return __UnaryFn(__inner)

def last() -> __UnaryFn:
    """Return last element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[-1]
        except:
            for item in arg:
                pass
            return item
    return __UnaryFn(__inner)

def pick(index: int) -> __UnaryFn:
    """Return nth element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[index]
        except:
            for i, v in __builtins.enumerate(arg):
                if i == index:
                    return v
    return __UnaryFn(__inner)

def tally() -> __UnaryFn:
    """Return tally (element count) of the Iterable"""
    def __inner(arg: __Union[__Sized, __Iterable]):
        try:
            return len(arg)
        except:
            return __builtins.sum(1 for _ in arg)
    return __UnaryFn(__inner)

def sliding(size: int) -> __UnaryFn:
    """Return generator which yields sliding windows of given `size` of the Sequence"""
    def __inner(arg: __Sequence):
        for i in __builtins.range(len(arg) - size + 1):
            yield tuple(__itertools.islice(arg, i, i + size))
    return __UnaryFn(__inner)

def sliding_map(size: int, mapper: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Return `sliding` combined with `map` function"""
    return sliding(size) | map(mapper)

def sliding_filter(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding` combined with `filter` function"""
    return sliding_map(size, filter(predicate))

def sliding_filter_not(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding` combined with `filter_not` function"""
    return sliding_map(size, filter_not(predicate))

def sliding_reduce(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding` combined with `reduce` function"""
    return sliding_map(size, reduce(reducer))

def sliding_scan(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding` combined with `scan` function"""
    return sliding_map(size, scan(reducer))
