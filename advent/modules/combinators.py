import inspect as __inspect
from typing import Any as __Any
from typing import Callable as __Callable
from typing import Union as __Union

from ..classes import AnyFn as __AnyFn
from ..classes import BinaryFn as __BinaryFn
from ..classes import NullaryFn as __NullaryFn
from ..classes import UnaryFn as __UnaryFn

__all__ = [
    'train',
]

def train(f: __Union[__Callable[[], __Any], __Callable[[__Any], __Any], __Callable[[__Any, __Any], __Any]], g: __Callable[[__Any, __Any], __Any], h: __Union[__Callable[[], __Any], __Callable[[__Any], __Any], __Callable[[__Any, __Any], __Any]]) -> __AnyFn:
    """Apply results of `f` and `h` to the binary function `g`"""
    f_arity = len(__inspect.signature(f).parameters)
    h_arity = len(__inspect.signature(h).parameters)
    match [ f_arity, h_arity ]:
        case [ 0, 0 ]:
            return __NullaryFn(lambda: g(f(), h()))
        case [ 1, 1 ]:
            return __UnaryFn(lambda a: g(f(a), h(a)))
        case [ 2, 2 ]:
            return __BinaryFn(lambda a, b: g(f(a, b), h(a, b)))
    return None
