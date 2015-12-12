from collections import Counter
from functools import reduce

from problem0003 import factorize


def product(iterable, start=1):
    return reduce(lambda x, y: x * y, iterable, start)


def lcm(iterable):
    '''return least common multiple for the numbers in iterable'''
    factors = Counter()
    for n in iterable:
        factors |= Counter(factorize(n))
    return product(factors.elements())

if __name__ == '__main__':
    print(lcm(range(2, 21)))
