def square(x):
    return x * x


def sum_of_squares(iterable):
    return sum(map(square, iterable))


def square_of_sum(iterable):
    return square(sum(iterable))

if __name__ == "__main__":
    print(square_of_sum(range(1, 101)) - sum_of_squares(range(1, 101)))
