# Imperative sequence processing in Python.
# Tested with Python 3.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.

def process(s):
    return sum(i + 1 for i in s if i % 2 == 0)


if __name__ == '__main__':
    print(process(range(10)))
