#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
=======

if __name__ == "__main__":
    """Print the sum, difference, product, quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
