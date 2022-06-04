#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
=======
    from sys import argv
    num_args = len(argv)
    total = 0
    for i in range(1, num_args):
        total += int(argv[i])
    print("{:d}".format(total))
>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
