from problem0003 import primes
from itertools import islice


def nth(iterable, n):
    '''return n-th element from given iterable
    >>> nth([1, 2, 3, 4], 2)
    2
    '''
    return next(islice(iterable, n-1, None))

if __name__ == '__main__':
    print(nth(primes(), 10001))
