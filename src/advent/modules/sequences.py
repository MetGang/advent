import builtins
import collections
import functools
import itertools
import operator
from collections import defaultdict
from collections.abc import Iterable, Mapping, Reversible, Sequence
from functools import cmp_to_key
from typing import Any, Callable, Sized

from ..classes import UnaryFn

__all__ = [
    'map',
    'filter',
    'filter_not',
    'partition',
    'padded_partition',
    'split_every',
    'group_by',
    'take',
    'take_every',
    'take_while',
    'drop',
    'drop_every',
    'drop_while',
    'compress',
    'distinct',
    'sort_by',
    'sort_with',
    'reverse',
    'cycle',
    'enumerate',
    'reduce',
    'scan',
    'prefixes',
    'suffixes',
    'replicate',
    'contains',
    'contains_if',
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
    'edges',
    'tally',
    'sliding',
    'sliding_map',
    'sliding_filter',
    'sliding_filter_not',
    'sliding_reduce',
    'sliding_scan',
    'permutations',
    'combinations',
]

_UNDEFINED = object()

def map(mapper: Callable[[Any], Any] | Mapping) -> UnaryFn:
    """Apply `mapper` to each element"""
    if callable(mapper):
        def __inner(arg: Iterable):
            return builtins.map(mapper, arg)
    else:
        def __inner(arg: Iterable):
            return builtins.map(lambda item: mapper[item], arg)
    return UnaryFn(__inner)

def filter(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Keep elements for which `predicate` returns true"""
    def __inner(arg: Iterable):
        return builtins.filter(predicate, arg)
    return UnaryFn(__inner)

def filter_not(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Keep elements for which `predicate` returns false"""
    def __inner(arg: Iterable):
        return itertools.filterfalse(predicate, arg)
    return UnaryFn(__inner)

def partition(size: int) -> UnaryFn:
    """Return elements in groups of given `size`, discard extra elements"""
    def __inner(arg: Iterable):
        its = [iter(arg)] * size
        return zip(*its)
    return UnaryFn(__inner)

def padded_partition(size: int, fill_value: Any = None) -> UnaryFn:
    """Return elements in groups of given `size`, fill missing elements with `fill_value`"""
    def __inner(arg: Iterable):
        its = [iter(arg)] * size
        return itertools.zip_longest(*its, fillvalue=fill_value)
    return UnaryFn(__inner)

def split_every(size: int) -> UnaryFn:
    """Return elements in groups of given `size`, return remaining elements in smaller group"""
    def __inner(arg: Iterable):
        it = iter(arg)
        while piece := tuple(itertools.islice(it, size)):
            yield piece
    return UnaryFn(__inner)

def group_by(selector: Callable[[Any], Any]) -> UnaryFn:
    """Return elements in groups for which `selector` returns the same value"""
    def __inner(arg: Iterable):
        groups = defaultdict(list)
        for item in arg:
            groups[selector(item)].append(item)
        for item in groups.values():
            yield tuple(item)
    return UnaryFn(__inner)

def take(count: int) -> UnaryFn:
    """Return first `count` elements"""
    def __inner(arg: Iterable):
        return itertools.islice(arg, count)
    return UnaryFn(__inner)

def take_every(step: int) -> UnaryFn:
    """Return every Nth element starting from the Nth"""
    def __inner(arg: Iterable):
        for i, item in builtins.enumerate(arg, 1):
            if i % step == 0:
                yield item
    return UnaryFn(__inner)

def take_while(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Take elements from the start while predicate evaluates to True"""
    return UnaryFn(lambda arg: itertools.takewhile(predicate, arg))

def drop(count: int) -> UnaryFn:
    """Return all but first `count` elements"""
    def __inner(arg: Iterable):
        return itertools.islice(arg, count, None)
    return UnaryFn(__inner)

def drop_every(step: int) -> UnaryFn:
    """Return elements excluding every Nth element"""
    def __inner(arg: Iterable):
        for i, item in builtins.enumerate(arg, 1):
            if i % step != 0:
                yield item
    return UnaryFn(__inner)

def drop_while(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Drop elements from the start while predicate evaluates to True"""
    return UnaryFn(lambda arg: itertools.dropwhile(predicate, arg))

def compress(mask: Iterable[bool]) -> UnaryFn:
    """Filter elements where corresponding value in `mask` is True"""
    return UnaryFn(lambda arg: itertools.compress(arg, mask))

def distinct() -> UnaryFn:
    """Return distinct (unique) elements preserving order"""
    def __inner(arg: Iterable):
        cache = set()
        for item in arg:
            if item not in cache:
                cache.add(item)
                yield item
    return UnaryFn(__inner)

def sort_by(key_fn: Callable[[Any], Any] = lambda x: x) -> UnaryFn:
    """Sort iterable using a key extraction function"""
    return UnaryFn(lambda iterable: sorted(iterable, key=key_fn))

def sort_with(comparator: Callable[[Any, Any], bool]) -> UnaryFn:
    """Sort iterable using a binary boolean predicate comparator"""
    key = cmp_to_key(lambda a, b: -1 if comparator(a, b) else (1 if comparator(b, a) else 0))
    return UnaryFn(lambda iterable: sorted(iterable, key=key))

def reverse() -> UnaryFn:
    """Return elements in reversed order"""
    def __inner(arg: Reversible):
        try:
            return builtins.reversed(arg)
        except TypeError:
            return builtins.reversed(list(arg))
    return UnaryFn(__inner)

def cycle() -> UnaryFn:
    """Return elements indefinitely"""
    def __inner(arg: Iterable):
        return itertools.cycle(arg)
    return UnaryFn(__inner)

def enumerate(start: int = 0) -> UnaryFn:
    """Return (index, element) pair for each element"""
    def __inner(arg: Iterable):
        return builtins.enumerate(arg, start)
    return UnaryFn(__inner)

def reduce(reducer: Callable[[Any, Any], Any], init: Any = _UNDEFINED) -> UnaryFn:
    """Reduce all elements with `reducer` and optional `init` value"""
    def __inner(arg: Iterable):
        if init is _UNDEFINED:
            return functools.reduce(reducer, arg)
        return functools.reduce(reducer, arg, init)
    return UnaryFn(__inner)

def scan(reducer: Callable[[Any, Any], Any], init: Any = _UNDEFINED) -> UnaryFn:
    """Reduce each prefix with `reducer` and optional `init` value"""
    def __inner(arg: Iterable):
        if init is _UNDEFINED:
            return itertools.accumulate(arg, reducer)
        return itertools.accumulate(arg, reducer, initial=init)
    return UnaryFn(__inner)

def prefixes() -> UnaryFn:
    """Return all non-empty prefixes"""
    def __inner(arg: Iterable):
        seq = tuple(arg)
        for size in builtins.range(1, len(seq) + 1):
            yield seq[:size]
    return UnaryFn(__inner)

def suffixes() -> UnaryFn:
    """Return all non-empty suffixes"""
    def __inner(arg: Iterable):
        seq = tuple(arg)
        for i in builtins.range(len(seq)):
            yield seq[i:]
    return UnaryFn(__inner)

def replicate(mask: Iterable[int]) -> UnaryFn:
    """Replicate each element in sequence by corresponding count in `mask`"""
    def __inner(arg: Iterable):
        it = iter(arg)
        for times in mask:
            item = next(it)
            for _ in builtins.range(times):
                yield item
    return UnaryFn(__inner)

def contains(value: Any) -> UnaryFn:
    """Check whether sequence contains given `value`"""
    def __inner(arg: Iterable):
        return builtins.any(value == item for item in arg)
    return UnaryFn(__inner)

def contains_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Check whether sequence contains an element satisfying `predicate`"""
    def __inner(arg: Iterable):
        return builtins.any(predicate(item) for item in arg)
    return UnaryFn(__inner)

def count(value: Any) -> UnaryFn:
    """Return number of elements that are equal to given `value`"""
    def __inner(arg: Iterable):
        return builtins.sum(1 for item in arg if item == value)
    return UnaryFn(__inner)

def count_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Return number of elements that satisfy given `predicate`"""
    def __inner(arg: Iterable):
        return builtins.sum(1 for item in arg if predicate(item))
    return UnaryFn(__inner)

def index(value: Any, invalid_idx: Any = -1) -> UnaryFn:
    """Return index of the first element that is equal to given `value`, `invalid_idx` otherwise"""
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if value == v:
                return i
        return invalid_idx
    return UnaryFn(__inner)

def index_if(predicate: Callable[[Any], bool], invalid_idx: Any = -1) -> UnaryFn:
    """Return index of the first element that satisfies given `predicate`, `invalid_idx` otherwise"""
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if predicate(v):
                return i
        return invalid_idx
    return UnaryFn(__inner)

def indices(value: Any) -> UnaryFn:
    """Return indices of all elements that are equal to given `value`"""
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if value == v:
                yield i
    return UnaryFn(__inner)

def indices_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """Return indices of all elements that satisfy given `predicate`"""
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if predicate(v):
                yield i
    return UnaryFn(__inner)

def sum(init: int = 0) -> UnaryFn:
    """Return sum of all elements with optional `init` value"""
    return reduce(operator.add, init)

def product(init: int = 1) -> UnaryFn:
    """Return product of all elements with optional `init` value"""
    return reduce(operator.mul, init)

def min() -> UnaryFn:
    """Return minimum element"""
    def __inner(arg: Iterable):
        return builtins.min(arg)
    return UnaryFn(__inner)

def max() -> UnaryFn:
    """Return maximum element"""
    def __inner(arg: Iterable):
        return builtins.max(arg)
    return UnaryFn(__inner)

def all() -> UnaryFn:
    """Return true if all elements are truthy"""
    def __inner(arg: Iterable):
        return builtins.all(arg)
    return UnaryFn(__inner)

def any() -> UnaryFn:
    """Return true if any element is truthy"""
    def __inner(arg: Iterable):
        return builtins.any(arg)
    return UnaryFn(__inner)

def none() -> UnaryFn:
    """Return true if no elements are truthy"""
    def __inner(arg: Iterable):
        return not builtins.any(arg)
    return UnaryFn(__inner)

def first() -> UnaryFn:
    """Return first element"""
    def __inner(arg: Iterable | Sequence):
        try:
            return arg[0]
        except (TypeError, LookupError):
            for item in arg:
                return item
            return None
    return UnaryFn(__inner)

def last() -> UnaryFn:
    """Return last element"""
    def __inner(arg: Iterable | Sequence):
        try:
            return arg[-1]
        except (TypeError, LookupError):
            item = None
            for item in arg:
                pass
            return item
    return UnaryFn(__inner)

def pick(idx: int) -> UnaryFn:
    """Return `idx` (nth) element"""
    def __inner(arg: Iterable | Sequence):
        try:
            return arg[idx]
        except (TypeError, LookupError):
            for i, v in builtins.enumerate(arg):
                if i == idx:
                    return v
            return None
    return UnaryFn(__inner)

def head() -> UnaryFn:
    """Return head (first) element"""
    return first()

def tail() -> UnaryFn:
    """Return tail (all but first) elements"""
    def __inner(arg: Iterable):
        return itertools.islice(arg, 1, None)
    return UnaryFn(__inner)

def edges() -> UnaryFn:
    """Return tuple of (first, last) elements"""
    def __inner(arg: Iterable | Sequence):
        try:
            return arg[0], arg[-1]
        except (TypeError, LookupError):
            it = iter(arg)
            try:
                first_item = last_item = next(it)
            except StopIteration:
                return None, None
            for last_item in it:
                pass
            return first_item, last_item
    return UnaryFn(__inner)

def tally() -> UnaryFn:
    """Return tally (element count)"""
    def __inner(arg: Iterable | Sized):
        try:
            return len(arg)
        except TypeError:
            return builtins.sum(1 for _ in arg)
    return UnaryFn(__inner)

def sliding(size: int) -> UnaryFn:
    """Return sliding windows of given `size`"""
    def __inner(arg: Iterable):
        it = iter(arg)
        window = collections.deque(itertools.islice(it, size), maxlen=size)
        if len(window) == size:
            yield tuple(window)
            for item in it:
                window.append(item)
                yield tuple(window)
    return UnaryFn(__inner)

def sliding_map(size: int, mapper: Callable[[Any], Any]) -> UnaryFn:
    """Return `sliding` combined with `map`"""
    return sliding(size) | map(mapper)

def sliding_filter(size: int, predicate: Callable[[Any], bool]) -> UnaryFn:
    """Return `sliding_map` combined with `filter`"""
    return sliding_map(size, filter(predicate))

def sliding_filter_not(size: int, predicate: Callable[[Any], bool]) -> UnaryFn:
    """Return `sliding_map` combined with `filter_not`"""
    return sliding_map(size, filter_not(predicate))

def sliding_reduce(size: int, reducer: Callable[[Any, Any], Any]) -> UnaryFn:
    """Return `sliding_map` combined with `reduce`"""
    return sliding_map(size, reduce(reducer))

def sliding_scan(size: int, reducer: Callable[[Any, Any], Any]) -> UnaryFn:
    """Return `sliding_map` combined with `scan`"""
    return sliding_map(size, scan(reducer))

def permutations(size: int) -> UnaryFn:
    """Return permutations of elements of given `size`"""
    def __inner(arg: Iterable):
        return itertools.permutations(arg, size)
    return UnaryFn(__inner)

def combinations(size: int) -> UnaryFn:
    """Return combinations of elements of given `size`"""
    def __inner(arg: Iterable):
        return itertools.combinations(arg, size)
    return UnaryFn(__inner)
