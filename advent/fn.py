import builtins as __builtins
import functools as __functools
import itertools as __itertools
from collections.abc import Iterable as __Iterable
from collections.abc import Reversible as __Reversible
from collections.abc import Sequence as __Sequence
from typing import Any as __Any
from typing import Callable as __Callable
from typing import Sized as __Sized
from typing import Union as __Union

from .classes import UNDEFINED as __UNDEFINED
from .classes import UnaryFn as __UnaryFn
from .classes import Undefined as __Undefined

__MODULE_NAME = 'fn'

__all__ = [
    'to',
    'identity',
    'map',
    'filter',
    'filter_not',
    'reduce',
    'scan',
    'prefixes',
    'suffixes',
    'sliding',
    'sliding_map',
    'sliding_filter',
    'sliding_filter_not',
    'sliding_reduce',
    'sliding_scan',
    'partition',
    'padded_partition',
    'distinct',
    'sum',
    'product',
    'all',
    'any',
    'none',
    'min',
    'max',
    'take',
    'drop',
    'pick',
    'first',
    'last',
    'tally',
    'reverse',
    'cycle',
    'enumerate',
]

def to(T: type) -> __UnaryFn:
    """Return element/Iterable casted to `T`"""
    return __UnaryFn(f'{__MODULE_NAME}.to', T)

def identity() -> __UnaryFn:
    """Return itself"""
    def __inner(arg: __Any):
        return arg
    return __UnaryFn(f'{__MODULE_NAME}.identity', __inner)

def map(mapper: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Apply `mapper` to each element"""
    def __inner(arg: __Iterable):
        return __builtins.map(mapper, arg)
    return __UnaryFn(f'{__MODULE_NAME}.map', __inner)

def filter(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Keep elements for which `predicate` returns true"""
    def __inner(arg: __Iterable):
        return __builtins.filter(predicate, arg)
    return __UnaryFn(f'{__MODULE_NAME}.filter', __inner)

def filter_not(predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Keep elements for which `predicate` returns false"""
    def __inner(arg: __Iterable):
        return __itertools.filterfalse(predicate, arg)
    return __UnaryFn(f'{__MODULE_NAME}.filter_not', __inner)

def reduce(reducer: __Callable[[__Any, __Any], __Any], init: __Union[__Any, __Undefined] = __UNDEFINED) -> __UnaryFn:
    """Reduce all elements of the Iterable with `reducer` and with optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __functools.reduce(reducer, arg)
        else:
            return __functools.reduce(reducer, arg, init)
    return __UnaryFn(f'{__MODULE_NAME}.reduce', __inner)

def scan(reducer: __Callable[[__Any, __Any], __Any], init: __Union[__Any, __Undefined] = __UNDEFINED) -> __UnaryFn:
    """Reduce each prefix of the Iterable with `reducer` and with optional `init` value"""
    def __inner(arg: __Iterable):
        if init is __UNDEFINED:
            return __itertools.accumulate(arg, reducer)
        else:
            return __itertools.accumulate(arg, reducer, initial = init)
    return __UnaryFn(f'{__MODULE_NAME}.scan', __inner)

def prefixes() -> __UnaryFn:
    """Return generator which yields all prefixes as tuples of the Sequence"""
    def __inner(arg: __Sequence):
        return (
            tuple(__itertools.islice(arg, None, sz)) for sz in __builtins.range(1, len(arg) + 1)
        )
    return __UnaryFn(f'{__MODULE_NAME}.prefixes', __inner)

def suffixes() -> __UnaryFn:
    """Return generator which yields all suffixes as tuples of the Sequence"""
    def __inner(arg: __Sequence):
        return (
            tuple(__itertools.islice(arg, None, sz)) for sz in __builtins.range(len(arg) + 1, 0, -1)
        )
    return __UnaryFn(f'{__MODULE_NAME}.suffixes', __inner)

def sliding(size: int) -> __UnaryFn:
    """Return generator which yields sliding windows of given `size` as tuples of the Sequence"""
    def __inner(arg: __Sequence):
        return (
            tuple(__itertools.islice(arg, i, i + size)) for i in __builtins.range(len(arg) - size + 1)
        )
    return __UnaryFn(f'{__MODULE_NAME}.sliding', __inner)

def sliding_map(size: int, mapper: __Callable[[__Any], __Any]) -> __UnaryFn:
    """Return `sliding` function combined with `map` function"""
    return __UnaryFn(f'{__MODULE_NAME}.sliding_map', sliding(size) | map(mapper))

def sliding_filter(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding` function combined with `filter` function"""
    return __UnaryFn(f'{__MODULE_NAME}.sliding_filter', sliding_map(size, filter(predicate)))

def sliding_filter_not(size: int, predicate: __Callable[[__Any], bool]) -> __UnaryFn:
    """Return `sliding` function combined with `filter_not` function"""
    return __UnaryFn(f'{__MODULE_NAME}.sliding_filter_not', sliding_map(size, filter_not(predicate)))

def sliding_reduce(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding` function combined with `reduce` function"""
    return __UnaryFn(f'{__MODULE_NAME}.sliding_reduce', sliding_map(size, reduce(reducer)))

def sliding_scan(size: int, reducer: __Callable[[__Any, __Any], __Any]) -> __UnaryFn:
    """Return `sliding` function combined with `scan` function"""
    return __UnaryFn(f'{__MODULE_NAME}.sliding_scan', sliding_map(size, scan(reducer)))

def partition(size: int) -> __UnaryFn:
    """Return iterator which yields groups as tuples of given `size` of the Iterable, discard extra elements"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return zip(*its)
    return __UnaryFn(f'{__MODULE_NAME}.partition', __inner)

def padded_partition(size: int, fill_value: __Any) -> __UnaryFn:
    """Return iterator which yields groups as tuples of given `size` of the Iterable, fill missing elements with `fill_value`"""
    def __inner(arg: __Iterable):
        its = [ iter(arg) ] * size
        return __itertools.zip_longest(*its, fillvalue = fill_value)
    return __UnaryFn(f'{__MODULE_NAME}.padded_partition', __inner)

def distinct() -> __UnaryFn:
    """Return generator with distinct (unique) elemets of the Iterable"""
    def __inner(arg: __Iterable):
        return (item for item in set(arg))
    return __UnaryFn(f'{__MODULE_NAME}.distinct', __inner)

def sum(init: int = 0) -> __UnaryFn:
    """Return sum of all elements of the Iterable with optional `init` value"""
    return __UnaryFn(f'{__MODULE_NAME}.sum', reduce(lambda a, b: a + b, init))

def product(init: int = 1) -> __UnaryFn:
    """Return product of all elements of the Iterable with optional `init` value"""
    return __UnaryFn(f'{__MODULE_NAME}.product', reduce(lambda a, b: a * b, init))

def all() -> __UnaryFn:
    """Return true if all elements of the Iterable are truthy"""
    def __inner(iterable: __Iterable):
        return __builtins.all(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.all', __inner)

def any() -> __UnaryFn:
    """Return true if any element of the Iterable is truthy"""
    def __inner(iterable: __Iterable):
        return __builtins.any(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.any', __inner)

def none() -> __UnaryFn:
    """Return true if none element of the Iterable is truthy"""
    def __inner(iterable: __Iterable):
        return not __builtins.all(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.none', __inner)

def min() -> __UnaryFn:
    """Return minimum element from the Iterable"""
    def __inner(iterable: __Iterable):
        return __builtins.min(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.min', __inner)

def max() -> __UnaryFn:
    """Return maximum element from the Iterable"""
    def __inner(iterable: __Iterable):
        return __builtins.max(iterable)
    return __UnaryFn(f'{__MODULE_NAME}.max', __inner)

def take(count: int) -> __UnaryFn:
    """Return iterator which yields only first `count` elements of the Iterable"""
    def __inner(iterable: __Iterable):
        return __itertools.islice(iterable, None, count)
    return __UnaryFn(f'{__MODULE_NAME}.take', __inner)

def drop(count: int) -> __UnaryFn:
    """Return iterator which yields all but first `count` elements of the Iterable"""
    def __inner(iterable: __Iterable):
        return __itertools.islice(iterable, count, None)
    return __UnaryFn(f'{__MODULE_NAME}.drop', __inner)

def pick(index: int) -> __UnaryFn:
    """Return nth element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[index]
        except:
            for i, v in __builtins.enumerate(arg):
                if i == index:
                    return v
    return __UnaryFn(f'{__MODULE_NAME}.pick', __inner)

def first() -> __UnaryFn:
    """Return first element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[0]
        except:
            for item in arg:
                return item
    return __UnaryFn(f'{__MODULE_NAME}.first', __inner)

def last() -> __UnaryFn:
    """Return last element of the Iterable"""
    def __inner(arg: __Union[__Sequence, __Iterable]):
        try:
            return arg[-1]
        except:
            for item in arg:
                pass
            return item
    return __UnaryFn(f'{__MODULE_NAME}.last', __inner)

def tally() -> __UnaryFn:
    """Return tally (element count) of the Iterable"""
    def __inner(arg: __Union[__Sized, __Iterable]):
        try:
            return len(arg)
        except:
            return __builtins.sum(1 for _ in arg)
    return __UnaryFn(f'{__MODULE_NAME}.tally', __inner)

def reverse() -> __UnaryFn:
    """Return iterator which yields elements of the Reversible in reverse order"""
    def __inner(arg: __Reversible):
        return __builtins.reversed(arg)
    return __UnaryFn(f'{__MODULE_NAME}.reverse', __inner)

def cycle() -> __UnaryFn:
    """Return iterator which yields elements of the Iterable indefinitely"""
    def __inner(arg: __Iterable):
        return __itertools.cycle(arg)
    return __UnaryFn(f'{__MODULE_NAME}.cycle', __inner)

def enumerate(start: int = 0) -> __UnaryFn:
    """Return iterator which yields (index, element) pair for each element of the Iterable"""
    def __inner(arg: __Iterable):
        return __builtins.enumerate(arg, start)
    return __UnaryFn(f'{__MODULE_NAME}.enumerate', __inner)
