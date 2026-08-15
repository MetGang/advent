import builtins
import math
import operator

from ..classes import BinaryFn, UnaryFn

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

eq = BinaryFn(operator.eq)
"""Return `a == b`"""

ne = BinaryFn(operator.ne)
"""Return `a != b`"""

lt = BinaryFn(operator.lt)
"""Return `a < b`"""

le = BinaryFn(operator.le)
"""Return `a <= b`"""

gt = BinaryFn(operator.gt)
"""Return `a > b`"""

ge = BinaryFn(operator.ge)
"""Return `a >= b`"""

logic_not = UnaryFn(operator.not_)
"""Return `not a`"""

logic_or = BinaryFn(lambda a, b: a or b)
"""Return `a or b`"""

logic_and = BinaryFn(lambda a, b: a and b)
"""Return `a and b`"""

logic_xor = BinaryFn(lambda a, b: bool(a) != bool(b))
"""Return `bool(a) != bool(b)`"""

bit_not = UnaryFn(operator.invert)
"""Return `~a`"""

bit_or = BinaryFn(operator.or_)
"""Return `a | b`"""

bit_and = BinaryFn(operator.and_)
"""Return `a & b`"""

bit_xor = BinaryFn(operator.xor)
"""Return `a ^ b`"""

bit_lsh = BinaryFn(operator.lshift)
"""Return `a << b`"""

bit_rsh = BinaryFn(operator.rshift)
"""Return `a >> b`"""

plus = UnaryFn(operator.pos)
"""Return `+a`"""

minus = UnaryFn(operator.neg)
"""Return `-a`"""

inc = UnaryFn(lambda a: a + 1)
"""Return `a + 1`"""

dec = UnaryFn(lambda a: a - 1)
"""Return `a - 1`"""

add = BinaryFn(operator.add)
"""Return `a + b`"""

sub = BinaryFn(operator.sub)
"""Return `a - b`"""

mul = BinaryFn(operator.mul)
"""Return `a * b`"""

div = BinaryFn(operator.truediv)
"""Return `a / b`"""

idiv = BinaryFn(operator.floordiv)
"""Return `a // b`"""

mod = BinaryFn(operator.mod)
"""Return `a % b`"""

pow = BinaryFn(operator.pow)
"""Return `a ** b`"""

abs = UnaryFn(operator.abs)
"""Return `abs(a)`"""

sign = UnaryFn(lambda a: (a > 0) - (a < 0))
"""Return `(a > 0) - (a < 0)`"""

diff = BinaryFn(lambda a, b: builtins.abs(a - b))
"""Return `abs(a - b)`"""

floor = UnaryFn(math.floor)
"""Return `math.floor(a)`"""

ceil = UnaryFn(math.ceil)
"""Return `math.ceil(a)`"""

min = BinaryFn(builtins.min)
"""Return `min(a, b)`"""

max = BinaryFn(builtins.max)
"""Return `max(a, b)`"""

lcm = BinaryFn(math.lcm)
"""Return `math.lcm(a, b)`"""

gcd = BinaryFn(math.gcd)
"""Return `math.gcd(a, b)`"""

even = UnaryFn(lambda a: a % 2 == 0)
"""Return `a % 2 == 0`"""

odd = UnaryFn(lambda a: a % 2 != 0)
"""Return `a % 2 != 0`"""
