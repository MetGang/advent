import builtins as __builtins
import math as __math

from .classes import BinaryFn as __BinaryFn
from .classes import UnaryFn as __UnaryFn

__MODULE_NAME = 'op'

__all__ = [
    'eq',
    'ne',
    'lt',
    'le',
    'gt',
    'ge',
    'logic_not',
    'logic_or',
    'logic_and',
    'logic_xor',
    'bit_not',
    'bit_or',
    'bit_and',
    'bit_xor',
    'bit_lsh',
    'bit_rsh',
    'plus',
    'minus',
    'add',
    'sub',
    'mul',
    'div',
    'idiv',
    'mod',
    'pow',
    'abs',
    'floor',
    'ceil',
    'min',
    'max',
    'midpoint',
    'imidpoint',
    'lcm',
    'gcd',
    'sign',
    'factorial',
    'is_even',
    'is_odd',
    'is_prime',
]

eq = __BinaryFn(f'{__MODULE_NAME}.eq', lambda a, b: a == b)
"""Return `a == b`"""

ne = __BinaryFn(f'{__MODULE_NAME}.ne', lambda a, b: a != b)
"""Return `a != b`"""

lt = __BinaryFn(f'{__MODULE_NAME}.lt', lambda a, b: a < b)
"""Return `a < b`"""

le = __BinaryFn(f'{__MODULE_NAME}.le', lambda a, b: a <= b)
"""Return `a <= b`"""

gt = __BinaryFn(f'{__MODULE_NAME}.gt', lambda a, b: a > b)
"""Return `a > b`"""

ge = __BinaryFn(f'{__MODULE_NAME}.ge', lambda a, b: a >= b)
"""Return `a >= b`"""

logic_not = __UnaryFn(f'{__MODULE_NAME}.logic_not', lambda a: not a)
"""Return `not a`"""

logic_or = __BinaryFn(f'{__MODULE_NAME}.logic_or', lambda a, b: a or b)
"""Return `a or b`"""

logic_and = __BinaryFn(f'{__MODULE_NAME}.logic_and', lambda a, b: a and b)
"""Return `a and b`"""

logic_xor = __BinaryFn(f'{__MODULE_NAME}.logic_xor', lambda a, b: (a and not b) or (not a and b))
"""Return `(a and not b) or (not a and b)`"""

bit_not = __UnaryFn(f'{__MODULE_NAME}.bit_not', lambda a: ~a)
"""Return `~a`"""

bit_or = __BinaryFn(f'{__MODULE_NAME}.bit_or', lambda a, b: a | b)
"""Return `a | b`"""

bit_and = __BinaryFn(f'{__MODULE_NAME}.bit_and', lambda a, b: a & b)
"""Return `a & b`"""

bit_xor = __BinaryFn(f'{__MODULE_NAME}.bit_xor', lambda a, b: a ^ b)
"""Return `a ^ b`"""

bit_lsh = __BinaryFn(f'{__MODULE_NAME}.bit_lsh', lambda a, b: a << b)
"""Return `a << b`"""

bit_rsh = __BinaryFn(f'{__MODULE_NAME}.bit_rsh', lambda a, b: a >> b)
"""Return `a >> b`"""

plus = __UnaryFn(f'{__MODULE_NAME}.plus', lambda a: +a)
"""Return `+a`"""

minus = __UnaryFn(f'{__MODULE_NAME}.minus', lambda a: -a)
"""Return `-a`"""

add = __BinaryFn(f'{__MODULE_NAME}.add', lambda a, b: a + b)
"""Return `a + b`"""

sub = __BinaryFn(f'{__MODULE_NAME}.sub', lambda a, b: a - b)
"""Return `a - b`"""

mul = __BinaryFn(f'{__MODULE_NAME}.mul', lambda a, b: a * b)
"""Return `a * b`"""

div = __BinaryFn(f'{__MODULE_NAME}.div', lambda a, b: a / b)
"""Return `a / b`"""

idiv = __BinaryFn(f'{__MODULE_NAME}.idiv', lambda a, b: a // b)
"""Return `a // b`"""

mod = __BinaryFn(f'{__MODULE_NAME}.mod', lambda a, b: a % b)
"""Return `a % b`"""

pow = __BinaryFn(f'{__MODULE_NAME}.pow', lambda a, b: a ** b)
"""Return `a ** b`"""

abs = __UnaryFn(f'{__MODULE_NAME}.abs', lambda a: __builtins.abs(a))
"""Return `abs(a)`"""

floor = __UnaryFn(f'{__MODULE_NAME}.floor', lambda a: __math.floor(a))
"""Return `math.floor(a)`"""

ceil = __UnaryFn(f'{__MODULE_NAME}.ceil', lambda a: __math.ceil(a))
"""Return `math.ceil(a)`"""

min = __BinaryFn(f'{__MODULE_NAME}.min', lambda a, b: __builtins.min(a, b))
"""Return `min(a, b)`"""

max = __BinaryFn(f'{__MODULE_NAME}.max', lambda a, b: __builtins.max(a, b))
"""Return `max(a, b)`"""

midpoint = __BinaryFn(f'{__MODULE_NAME}.midpoint', lambda a, b: a + (b - a) / 2)
"""Return `a + (b - a) / 2`"""

imidpoint = __BinaryFn(f'{__MODULE_NAME}.imidpoint', lambda a, b: a + (b - a) // 2)
"""Return `a + (b - a) // 2`"""

lcm = __BinaryFn(f'{__MODULE_NAME}.lcm', lambda a, b: __math.lcm(a, b))
"""Return `math.lcm(a, b)`"""

gcd = __BinaryFn(f'{__MODULE_NAME}.gcd', lambda a, b: __math.gcd(a, b))
"""Return `math.gcd(a, b)`"""

sign = __UnaryFn(f'{__MODULE_NAME}.sign', lambda a: (a > 0) - (a < 0))
"""Return `(a > 0) - (a < 0)`"""

factorial = __UnaryFn(f'{__MODULE_NAME}.factorial', lambda a: __math.factorial(a))
"""Return `math.factorial(a)`"""

is_even = __UnaryFn(f'{__MODULE_NAME}.is_even', lambda a: a % 2 == 0)
"""Return `a % 2 == 0`"""

is_odd = __UnaryFn(f'{__MODULE_NAME}.is_even', lambda a: a % 2 == 1)
"""Return `a % 2 == 1`"""

def __is_prime(n):
    # https://stackoverflow.com/a/15285588
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

is_prime = __UnaryFn(f'{__MODULE_NAME}.is_prime', __is_prime)
"""Return `op.__is_prime(a)`"""
