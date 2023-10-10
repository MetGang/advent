import functools as __functools
from typing import Any as __Any
from typing import Callable as __Callable

__all__ = [
    'comparator_to_key',
]

def comparator_to_key(comparator: __Callable[[__Any, __Any], bool]):
    def __inner(lhs, rhs):
        if comparator(lhs, rhs):
            return -1
        elif comparator(rhs, lhs):
            return 1
        else:
            return 0
    return __functools.cmp_to_key(__inner)
