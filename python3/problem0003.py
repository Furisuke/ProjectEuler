from bisect import bisect
from math import sqrt


def primes():
    '''yield primes in ascending order'''
    known_primes = []
    n = 1
    while True:
        n += 1
        test_divisors = known_primes[:bisect(known_primes, sqrt(n))]
        for i in test_divisors:
            if n % i == 0:
                break
        else:
            known_primes.append(n)
            yield n


def factorize(n):
    '''
    >>> factorize(84)
    [2, 2, 3, 7]
    '''
    if n < 2:
        raise ValueError('factorize expects integer greater than 1')
    factors = []
    for d in primes():
        while n % d == 0:
            n = n / d
            factors.append(d)
            if n == 1:
                return factors

if __name__ == '__main__':
    print(factorize(600851475143)[-1])
