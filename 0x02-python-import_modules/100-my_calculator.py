#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
=======
    from sys import argv
    from calculator_1 import *
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def add_():
        total = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, total))
        return total

    def sub_():
        total = sub(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, total))
        return total

    def mul_():
        total = mul(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, total))
        return total

    def div_():
        total = div(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, total))
        return total

    options = {
        "+": add_,
        "-": sub_,
        "*": mul_,
        "/": div_
    }
    options.get(op, not_found)()
>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
