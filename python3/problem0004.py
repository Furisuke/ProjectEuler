def is_palindrome(str):
    return str == str[::-1]


def find_largest_palindrome_product():
    max = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            product = x * y
            if product <= max:
                break
            elif is_palindrome(str(product)):
                max = product
    return max

if __name__ == "__main__":
    print(find_largest_palindrome_product())
