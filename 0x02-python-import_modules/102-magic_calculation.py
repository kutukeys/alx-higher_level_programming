#!/usr/bin/python3
<<<<<<< HEAD
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
=======


def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
<<<<<<< HEAD
    else:
        return (sub(a, b))
=======

    else:
        return(sub(a, b))
>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
