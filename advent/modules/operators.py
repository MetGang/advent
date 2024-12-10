import builtins as __builtins
import math as __math

from ..classes import BinaryFn as __BinaryFn
from ..classes import UnaryFn as __UnaryFn

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
    'inc',
    'dec',
    'add',
    'sub',
    'mul',
    'div',
    'idiv',
    'mod',
    'pow',
    'abs',
    'sign',
    'diff',
    'floor',
    'ceil',
    'min',
    'max',
    'lcm',
    'gcd',
    'even',
    'odd',
]

eq = __BinaryFn(lambda a, b: a == b)
"""Return `a == b`"""

ne = __BinaryFn(lambda a, b: a != b)
"""Return `a != b`"""

lt = __BinaryFn(lambda a, b: a < b)
"""Return `a < b`"""

le = __BinaryFn(lambda a, b: a <= b)
"""Return `a <= b`"""

gt = __BinaryFn(lambda a, b: a > b)
"""Return `a > b`"""

ge = __BinaryFn(lambda a, b: a >= b)
"""Return `a >= b`"""

logic_not = __UnaryFn(lambda a: not a)
"""Return `not a`"""

logic_or = __BinaryFn(lambda a, b: a or b)
"""Return `a or b`"""

logic_and = __BinaryFn(lambda a, b: a and b)
"""Return `a and b`"""

logic_xor = __BinaryFn(lambda a, b: (a and not b) or (not a and b))
"""Return `(a and not b) or (not a and b)`"""

bit_not = __UnaryFn(lambda a: ~a)
"""Return `~a`"""

bit_or = __BinaryFn(lambda a, b: a | b)
"""Return `a | b`"""

bit_and = __BinaryFn(lambda a, b: a & b)
"""Return `a & b`"""

bit_xor = __BinaryFn(lambda a, b: a ^ b)
"""Return `a ^ b`"""

bit_lsh = __BinaryFn(lambda a, b: a << b)
"""Return `a << b`"""

bit_rsh = __BinaryFn(lambda a, b: a >> b)
"""Return `a >> b`"""

plus = __UnaryFn(lambda a: +a)
"""Return `+a`"""

minus = __UnaryFn(lambda a: -a)
"""Return `-a`"""

inc = __UnaryFn(lambda a: a + 1)
"""Return `a + 1`"""

dec = __UnaryFn(lambda a: a - 1)
"""Return `a - 1`"""

add = __BinaryFn(lambda a, b: a + b)
"""Return `a + b`"""

sub = __BinaryFn(lambda a, b: a - b)
"""Return `a - b`"""

mul = __BinaryFn(lambda a, b: a * b)
"""Return `a * b`"""

div = __BinaryFn(lambda a, b: a / b)
"""Return `a / b`"""

idiv = __BinaryFn(lambda a, b: a // b)
"""Return `a // b`"""

mod = __BinaryFn(lambda a, b: a % b)
"""Return `a % b`"""

pow = __BinaryFn(lambda a, b: a ** b)
"""Return `a ** b`"""

abs = __UnaryFn(lambda a: __builtins.abs(a))
"""Return `abs(a)`"""

sign = __UnaryFn(lambda a: (a > 0) - (a < 0))
"""Return `(a > 0) - (a < 0)`"""

diff = __BinaryFn(lambda a, b: __builtins.abs(a - b))
"""Return `abs(a - b)`"""

floor = __UnaryFn(lambda a: __math.floor(a))
"""Return `math.floor(a)`"""

ceil = __UnaryFn(lambda a: __math.ceil(a))
"""Return `math.ceil(a)`"""

min = __BinaryFn(lambda a, b: __builtins.min(a, b))
"""Return `min(a, b)`"""

max = __BinaryFn(lambda a, b: __builtins.max(a, b))
"""Return `max(a, b)`"""

lcm = __BinaryFn(lambda a, b: __math.lcm(a, b))
"""Return `math.lcm(a, b)`"""

gcd = __BinaryFn(lambda a, b: __math.gcd(a, b))
"""Return `math.gcd(a, b)`"""

even = __UnaryFn(lambda a: a % 2 == 0)
"""Return `a % 2 == 0`"""

odd = __UnaryFn(lambda a: a % 2 != 0)
"""Return `a % 2 != 0`"""
