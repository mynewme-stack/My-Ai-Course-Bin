# GCD/LCM of Multiple Integers
import math
from functools import reduce

integer = [1,3,4,6,8,9]

if not integer or 0 in integer:
    print("Given numbers are incorrect.")
else:

    total_gcd= reduce(math.gcd, integer)
    total_lcm= reduce(math.lcm, integer)
    print(f'GCD: {total_gcd}')
    print(f'LCM: {total_lcm}')
print(f'Numbers: {integer}')