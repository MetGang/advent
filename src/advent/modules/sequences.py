import builtins
import collections
import functools
import itertools
import operator
from collections import defaultdict
from collections.abc import Iterable, Mapping, Reversible, Sequence, Sized
from functools import cmp_to_key
from typing import Any, Callable

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
    """
    Apply `mapper` to each element.

    >>> list(map(lambda x: x * 2)([1, 2, 3]))
    [2, 4, 6]
    >>> list(map({'a': 1, 'b': 2})(['a', 'b']))
    [1, 2]
    """
    if callable(mapper):
        def __inner_callable(arg: Iterable):
            return builtins.map(mapper, arg)
        return UnaryFn(__inner_callable)
    def __inner_mapping(arg: Iterable):
        return builtins.map(lambda item: mapper[item], arg)
    return UnaryFn(__inner_mapping)

def filter(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Keep elements for which `predicate` returns true.

    >>> list(filter(lambda x: x % 2 == 0)([1, 2, 3, 4]))
    [2, 4]
    """
    def __inner(arg: Iterable):
        return builtins.filter(predicate, arg)
    return UnaryFn(__inner)

def filter_not(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Keep elements for which `predicate` returns false.

    >>> list(filter_not(lambda x: x % 2 == 0)([1, 2, 3, 4]))
    [1, 3]
    """
    def __inner(arg: Iterable):
        return itertools.filterfalse(predicate, arg)
    return UnaryFn(__inner)

def partition(size: int) -> UnaryFn:
    """
    Return elements in groups of given `size`, discarding extra elements.

    >>> list(partition(2)([1, 2, 3, 4, 5]))
    [(1, 2), (3, 4)]
    """
    def __inner(arg: Iterable):
        its = [iter(arg)] * size
        return zip(*its)
    return UnaryFn(__inner)

def padded_partition(size: int, fill_value: Any = None) -> UnaryFn:
    """
    Return elements in groups of given `size`, padding missing elements.

    >>> list(padded_partition(2)([1, 2, 3]))
    [(1, 2), (3, None)]
    """
    def __inner(arg: Iterable):
        its = [iter(arg)] * size
        return itertools.zip_longest(*its, fillvalue=fill_value)
    return UnaryFn(__inner)

def split_every(size: int) -> UnaryFn:
    """
    Return elements in groups of given `size`.

    >>> list(split_every(2)([1, 2, 3, 4, 5]))
    [(1, 2), (3, 4), (5,)]
    """
    def __inner(arg: Iterable):
        it = iter(arg)
        while piece := tuple(itertools.islice(it, size)):
            yield piece
    return UnaryFn(__inner)

def group_by(selector: Callable[[Any], Any]) -> UnaryFn:
    """
    Return elements grouped by the value returned by `selector`.

    >>> list(group_by(lambda x: x % 2)([1, 2, 3, 4]))
    [(1, 3), (2, 4)]
    """
    def __inner(arg: Iterable):
        groups = defaultdict(list)
        for item in arg:
            groups[selector(item)].append(item)
        for item in groups.values():
            yield tuple(item)
    return UnaryFn(__inner)

def take(count: int) -> UnaryFn:
    """
    Return the first `count` elements.

    >>> list(take(2)([1, 2, 3]))
    [1, 2]
    """
    def __inner(arg: Iterable):
        return itertools.islice(arg, count)
    return UnaryFn(__inner)

def take_every(step: int) -> UnaryFn:
    """
    Return every Nth element, starting from the Nth.

    >>> list(take_every(2)([1, 2, 3, 4, 5]))
    [2, 4]
    """
    def __inner(arg: Iterable):
        for i, item in builtins.enumerate(arg, 1):
            if i % step == 0:
                yield item
    return UnaryFn(__inner)

def take_while(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Take elements while `predicate` returns true.

    >>> list(take_while(lambda x: x < 3)([1, 2, 3, 1]))
    [1, 2]
    """
    return UnaryFn(lambda arg: itertools.takewhile(predicate, arg))

def drop(count: int) -> UnaryFn:
    """
    Return all but the first `count` elements.

    >>> list(drop(2)([1, 2, 3, 4]))
    [3, 4]
    """
    def __inner(arg: Iterable):
        return itertools.islice(arg, count, None)
    return UnaryFn(__inner)

def drop_every(step: int) -> UnaryFn:
    """
    Return elements excluding every Nth element.

    >>> list(drop_every(2)([1, 2, 3, 4, 5]))
    [1, 3, 5]
    """
    def __inner(arg: Iterable):
        for i, item in builtins.enumerate(arg, 1):
            if i % step != 0:
                yield item
    return UnaryFn(__inner)

def drop_while(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Drop elements while `predicate` returns true.

    >>> list(drop_while(lambda x: x < 3)([1, 2, 3, 1]))
    [3, 1]
    """
    return UnaryFn(lambda arg: itertools.dropwhile(predicate, arg))

def compress(mask: Iterable[bool]) -> UnaryFn:
    """
    Filter elements corresponding to true values in `mask`.

    >>> list(compress([True, False, True])(['a', 'b', 'c']))
    ['a', 'c']
    """
    return UnaryFn(lambda arg: itertools.compress(arg, mask))

def distinct() -> UnaryFn:
    """
    Return distinct elements while preserving order.

    >>> list(distinct()([1, 2, 1, 3, 2]))
    [1, 2, 3]
    """
    def __inner(arg: Iterable):
        cache = set()
        for item in arg:
            if item not in cache:
                cache.add(item)
                yield item
    return UnaryFn(__inner)

def sort_by(key_fn: Callable[[Any], Any] = lambda x: x) -> UnaryFn:
    """
    Sort an iterable using a key function.

    >>> sort_by(lambda x: -x)([1, 3, 2])
    [3, 2, 1]
    """
    return UnaryFn(lambda iterable: sorted(iterable, key=key_fn))

def sort_with(comparator: Callable[[Any, Any], bool]) -> UnaryFn:
    """
    Sort an iterable using a binary comparator.

    >>> sort_with(lambda a, b: a < b)([3, 1, 2])
    [1, 2, 3]
    """
    key = cmp_to_key(lambda a, b: -1 if comparator(a, b) else (1 if comparator(b, a) else 0))
    return UnaryFn(lambda iterable: sorted(iterable, key=key))

def reverse() -> UnaryFn:
    """
    Return elements in reversed order.

    >>> list(reverse()([1, 2, 3]))
    [3, 2, 1]
    """
    def __inner(arg: Reversible):
        try:
            return builtins.reversed(arg)
        except TypeError:
            return builtins.reversed(list(arg))
    return UnaryFn(__inner)

def cycle() -> UnaryFn:
    """
    Return elements indefinitely.

    >>> list(itertools.islice(cycle()([1, 2]), 5))
    [1, 2, 1, 2, 1]
    """
    def __inner(arg: Iterable):
        return itertools.cycle(arg)
    return UnaryFn(__inner)

def enumerate(start: int = 0) -> UnaryFn:
    """
    Return index-element pairs.

    >>> list(enumerate(1)(['a', 'b']))
    [(1, 'a'), (2, 'b')]
    """
    def __inner(arg: Iterable):
        return builtins.enumerate(arg, start)
    return UnaryFn(__inner)

def reduce(reducer: Callable[[Any, Any], Any], init: Any = _UNDEFINED) -> UnaryFn:
    """
    Reduce all elements with `reducer`.

    >>> reduce(lambda a, b: a + b)([1, 2, 3])
    6
    >>> reduce(lambda a, b: a + b, 10)([1, 2, 3])
    16
    """
    def __inner(arg: Iterable):
        if init is _UNDEFINED:
            return functools.reduce(reducer, arg)
        return functools.reduce(reducer, arg, init)
    return UnaryFn(__inner)

def scan(reducer: Callable[[Any, Any], Any], init: Any = _UNDEFINED) -> UnaryFn:
    """
    Reduce each prefix with `reducer`.

    >>> list(scan(lambda a, b: a + b)([1, 2, 3]))
    [1, 3, 6]
    >>> list(scan(lambda a, b: a + b, 10)([1, 2, 3]))
    [10, 11, 13, 16]
    """
    def __inner(arg: Iterable):
        if init is _UNDEFINED:
            return itertools.accumulate(arg, reducer)
        return itertools.accumulate(arg, reducer, initial=init)
    return UnaryFn(__inner)

def prefixes() -> UnaryFn:
    """
    Return all non-empty prefixes.

    >>> list(prefixes()([1, 2, 3]))
    [(1,), (1, 2), (1, 2, 3)]
    """
    def __inner(arg: Iterable):
        seq = tuple(arg)
        for size in builtins.range(1, len(seq) + 1):
            yield seq[:size]
    return UnaryFn(__inner)

def suffixes() -> UnaryFn:
    """
    Return all non-empty suffixes.

    >>> list(suffixes()([1, 2, 3]))
    [(1, 2, 3), (2, 3), (3,)]
    """
    def __inner(arg: Iterable):
        seq = tuple(arg)
        for i in builtins.range(len(seq)):
            yield seq[i:]
    return UnaryFn(__inner)

def replicate(mask: Iterable[int]) -> UnaryFn:
    """
    Replicate each element by its corresponding count.

    >>> list(replicate([2, 0, 1])(['a', 'b', 'c']))
    ['a', 'a', 'c']
    """
    def __inner(arg: Iterable):
        it = iter(arg)
        for times in mask:
            item = next(it)
            for _ in builtins.range(times):
                yield item
    return UnaryFn(__inner)

def contains(value: Any) -> UnaryFn:
    """
    Check whether a sequence contains `value`.

    >>> contains(2)([1, 2, 3])
    True
    >>> contains(4)([1, 2, 3])
    False
    """
    def __inner(arg: Iterable):
        return builtins.any(value == item for item in arg)
    return UnaryFn(__inner)

def contains_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Check whether any element satisfies `predicate`.

    >>> contains_if(lambda x: x > 2)([1, 2, 3])
    True
    """
    def __inner(arg: Iterable):
        return builtins.any(predicate(item) for item in arg)
    return UnaryFn(__inner)

def count(value: Any) -> UnaryFn:
    """
    Count elements equal to `value`.

    >>> count(2)([1, 2, 2, 3])
    2
    """
    def __inner(arg: Iterable):
        return builtins.sum(1 for item in arg if item == value)
    return UnaryFn(__inner)

def count_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Count elements satisfying `predicate`.

    >>> count_if(lambda x: x % 2 == 0)([1, 2, 3, 4])
    2
    """
    def __inner(arg: Iterable):
        return builtins.sum(1 for item in arg if predicate(item))
    return UnaryFn(__inner)

def index(value: Any, invalid_idx: Any = -1) -> UnaryFn:
    """
    Return the index of the first matching element.

    >>> index('b')(['a', 'b', 'c'])
    1
    >>> index('x', None)(['a', 'b', 'c'])
    """
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if value == v:
                return i
        return invalid_idx
    return UnaryFn(__inner)

def index_if(predicate: Callable[[Any], bool], invalid_idx: Any = -1) -> UnaryFn:
    """
    Return the index of the first matching element.

    >>> index_if(lambda x: x > 2)([1, 2, 3])
    2
    """
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if predicate(v):
                return i
        return invalid_idx
    return UnaryFn(__inner)

def indices(value: Any) -> UnaryFn:
    """
    Return indices of all matching elements.

    >>> list(indices('a')(['a', 'b', 'a']))
    [0, 2]
    """
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if value == v:
                yield i
    return UnaryFn(__inner)

def indices_if(predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Return indices of all elements satisfying `predicate`.

    >>> list(indices_if(lambda x: x % 2 == 0)([1, 2, 3, 4]))
    [1, 3]
    """
    def __inner(arg: Iterable):
        for i, v in builtins.enumerate(arg):
            if predicate(v):
                yield i
    return UnaryFn(__inner)

def sum(init: int = 0) -> UnaryFn:
    """
    Return the sum of all elements.

    >>> sum()([1, 2, 3])
    6
    >>> sum(10)([1, 2, 3])
    16
    """
    return reduce(operator.add, init)

def product(init: int = 1) -> UnaryFn:
    """
    Return the product of all elements.

    >>> product()([2, 3, 4])
    24
    >>> product(10)([2, 3])
    60
    """
    return reduce(operator.mul, init)

def min() -> UnaryFn:
    """
    Return the minimum element.

    >>> min()([3, 1, 2])
    1
    """
    def __inner(arg: Iterable):
        return builtins.min(arg)
    return UnaryFn(__inner)

def max() -> UnaryFn:
    """
    Return the maximum element.

    >>> max()([1, 3, 2])
    3
    """
    def __inner(arg: Iterable):
        return builtins.max(arg)
    return UnaryFn(__inner)

def all() -> UnaryFn:
    """
    Return true if all elements are truthy.

    >>> all()([True, 1, 'yes'])
    True
    >>> all()([True, 0, 'yes'])
    False
    """
    def __inner(arg: Iterable):
        return builtins.all(arg)
    return UnaryFn(__inner)

def any() -> UnaryFn:
    """
    Return true if any element is truthy.

    >>> any()([False, 0, 1])
    True
    >>> any()([False, 0])
    False
    """
    def __inner(arg: Iterable):
        return builtins.any(arg)
    return UnaryFn(__inner)

def none() -> UnaryFn:
    """
    Return true if no elements are truthy.

    >>> none()([False, 0, None])
    True
    >>> none()([False, 1])
    False
    """
    def __inner(arg: Iterable):
        return not builtins.any(arg)
    return UnaryFn(__inner)

def first() -> UnaryFn:
    """
    Return the first element.

    >>> first()([1, 2, 3])
    1
    >>> first()([])
    """
    def __inner(arg: Iterable):
        if isinstance(arg, Sequence):
            return arg[0] if arg else None
        return next(iter(arg), None)
    return UnaryFn(__inner)

def last() -> UnaryFn:
    """
    Return the last element.

    >>> last()([1, 2, 3])
    3
    >>> last()([])
    """
    def __inner(arg: Iterable):
        if isinstance(arg, Sequence):
            return arg[-1] if arg else None
        item = None
        for item in arg:
            pass
        return item
    return UnaryFn(__inner)

def pick(idx: int) -> UnaryFn:
    """
    Return the element at `idx`.

    >>> pick(1)(['a', 'b', 'c'])
    'b'
    >>> pick(5)(['a', 'b', 'c'])
    """
    def __inner(arg: Iterable):
        try:
            return tuple(arg)[idx]
        except IndexError:
            return None
    return UnaryFn(__inner)

def head() -> UnaryFn:
    """
    Return the first element.

    >>> head()([1, 2, 3])
    1
    """
    return first()

def tail() -> UnaryFn:
    """
    Return all but the first element.

    >>> list(tail()([1, 2, 3]))
    [2, 3]
    """
    def __inner(arg: Iterable):
        return itertools.islice(arg, 1, None)
    return UnaryFn(__inner)

def edges() -> UnaryFn:
    """
    Return the first and last elements.

    >>> edges()([1, 2, 3])
    (1, 3)
    >>> edges()([])
    (None, None)
    """
    def __inner(arg: Iterable):
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
    """
    Return the number of elements.

    >>> tally()([1, 2, 3])
    3
    >>> tally()(iter([1, 2, 3]))
    3
    """
    def __inner(arg: Iterable):
        if isinstance(arg, Sized):
            return len(arg)
        return builtins.sum(1 for _ in arg)
    return UnaryFn(__inner)

def sliding(size: int) -> UnaryFn:
    """
    Return sliding windows of the given `size`.

    >>> list(sliding(2)([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    """
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
    """
    Apply `mapper` to each sliding window.
    """
    return sliding(size) | map(mapper)

def sliding_filter(size: int, predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Filter each sliding window.
    """
    return sliding_map(size, filter(predicate))

def sliding_filter_not(size: int, predicate: Callable[[Any], bool]) -> UnaryFn:
    """
    Filter out matching elements from each sliding window.
    """
    return sliding_map(size, filter_not(predicate))

def sliding_reduce(size: int, reducer: Callable[[Any, Any], Any]) -> UnaryFn:
    """
    Reduce each sliding window.
    """
    return sliding_map(size, reduce(reducer))

def sliding_scan(size: int, reducer: Callable[[Any, Any], Any]) -> UnaryFn:
    """
    Scan each sliding window.
    """
    return sliding_map(size, scan(reducer))

def permutations(size: int) -> UnaryFn:
    """
    Return permutations of the given `size`.

    >>> list(permutations(2)([1, 2, 3]))
    [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    """
    def __inner(arg: Iterable):
        return itertools.permutations(arg, size)
    return UnaryFn(__inner)

def combinations(size: int) -> UnaryFn:
    """
    Return combinations of the given `size`.

    >>> list(combinations(2)([1, 2, 3]))
    [(1, 2), (1, 3), (2, 3)]
    """
    def __inner(arg: Iterable):
        return itertools.combinations(arg, size)
    return UnaryFn(__inner)
