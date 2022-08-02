# Example of mutual recursion with even/odd.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.


def is_even(n):
    return True if n == 0 else is_odd(n - 1)


def is_odd(n):
    return False if n == 0 else is_even(n - 1)


def is_even_thunked(n):
    return True if n == 0 else (lambda: is_odd_thunked(n - 1))


def is_odd_thunked(n):
    return False if n == 0 else (lambda: is_even_thunked(n - 1))


def trampoline(f, *args):
    v = f(*args)
    while callable(v):
        v = v()
    return v


if __name__ == '__main__':
    print(is_even(800))

    # If I try to run is_even(1000) with the default system recursion limit, it
    # blows up. But trampolining keeps the stack depth constant and small.
    print(trampoline(is_even_thunked, 1000))
