from itertools import takewhile


def fibonacci(first=1, second=2):
    '''yields fibonacci sequence'''
    x = first
    x_ = second
    yield first
    yield second
    while True:
        x__ = x + x_
        yield x__
        x = x_
        x_ = x__

if __name__ == '__main__':
    print(sum(n for n in takewhile(lambda n: n < 4000000, fibonacci()) if n % 2 == 0))
