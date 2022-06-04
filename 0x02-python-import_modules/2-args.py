#!/usr/bin/python3
if __name__ == "__main__":
    import sys
<<<<<<< HEAD
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
=======
    total = len(sys.argv)
    if total <= 1:
        print("0 arguments.")
    else:
        if total == 2:
            print("{:d} argument:".format(total - 1))
        else:
            print("{:d} arguments:".format(total - 1))
        for i in range(1, total):
            print("{:d}: {}".format(i, sys.argv[i]))
>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
