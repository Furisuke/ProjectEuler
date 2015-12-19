from problem0003 import primes
from itertools import takewhile

print(sum(takewhile(lambda x: x < 2000000, primes())))
