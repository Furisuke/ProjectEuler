from problem0005 import product
from itertools import count, dropwhile
from math import sqrt


def pythagorean_triplets():
    while True:
        for c in count(1):
            for a in range(1, c//2):
                b = sqrt(c*c - a*a)
                if b.is_integer():
                    yield (a, int(b), c)

if __name__ == '__main__':
    target = next(dropwhile(lambda t: sum(t) != 1000, pythagorean_triplets()))
    print(product(target))
