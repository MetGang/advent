from .classes import AnyFn as __AnyFn
from .classes import BinaryFn as __BinaryFn
from .classes import NullaryFn as __NullaryFn
from .classes import UnaryFn as __UnaryFn

__MODULE_NAME = 'cb'

__all__ = [
    'flip',
    'train',
    'atop',
]

def flip(f: __BinaryFn) -> __BinaryFn:
    """Flip/switch arguments of binary function `f`"""
    return __BinaryFn(f'{__MODULE_NAME}.flip', lambda a, b: f(b, a))

def train(f: __AnyFn, g: __BinaryFn, h: __AnyFn) -> __AnyFn:
    """Apply results of `f` and `h` to binary function `g`"""
    assert type(f) == type(h), ''
    if type(f) == __NullaryFn:
        return __NullaryFn(f'{__MODULE_NAME}.ntrain', lambda: g(f(), h()))
    elif type(f) == __UnaryFn:
        return __UnaryFn(f'{__MODULE_NAME}.utrain', lambda a: g(f(a), h(a)))
    elif type(f) == __BinaryFn:
        return __BinaryFn(f'{__MODULE_NAME}.btrain', lambda a, b: g(f(a, b), h(a, b)))
    return None

def atop(f: __UnaryFn, g: __AnyFn) -> __AnyFn:
    """Apply result of `g` to unary function `f`"""
    if type(g) == __NullaryFn:
            return __NullaryFn(f'{__MODULE_NAME}.natop', lambda: f(g()))
    elif type(g) == __UnaryFn:
            return __UnaryFn(f'{__MODULE_NAME}.uatop', lambda a: f(g(a)))
    elif type(g) == __BinaryFn:
        return __BinaryFn(f'{__MODULE_NAME}.batop', lambda a, b: f(g(a, b)))
    return None
