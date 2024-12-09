from ..classes import AnyFn as __AnyFn
from ..classes import BinaryFn as __BinaryFn
from ..classes import NullaryFn as __NullaryFn
from ..classes import UnaryFn as __UnaryFn

__all__ = [
    'train',
]

def train(f: __AnyFn, g: __BinaryFn, h: __AnyFn) -> __AnyFn:
    """Apply results of `f` and `h` to the binary function `g`"""
    match [ f, h ]:
        case [ __NullaryFn(), __NullaryFn() ]:
            return __NullaryFn(lambda: g(f(), h()))
        case [ __UnaryFn(), __UnaryFn() ]:
            return __UnaryFn(lambda a: g(f(a), h(a)))
        case [ __BinaryFn(), __BinaryFn() ]:
            return __BinaryFn(lambda a, b: g(f(a, b), h(a, b)))
    return None
