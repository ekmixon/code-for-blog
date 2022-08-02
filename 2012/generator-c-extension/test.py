# Test for the extension.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.
import spam
import unittest


def pyrevgen(seq):
    yield from enumerate(reversed(seq))

therevgen = spam.revgen


class Test(unittest.TestCase):
    def test_revgen(self):
        global therevgen

        lst = list(therevgen(['a', 'b', 'c']))
        self.assertEqual(lst, [(0, 'c'), (1, 'b'), (2, 'a')])

        lst = list(therevgen(['a']))
        self.assertEqual(lst, [(0, 'a')])

        lst = list(therevgen([]))
        self.assertEqual(lst, [])

        gen = therevgen(['a', 'b', 'c'])
        self.assertEqual(next(gen), (0, 'c'))
        self.assertEqual(next(gen), (1, 'b'))
        self.assertEqual(next(gen), (2, 'a'))
        self.assertRaises(StopIteration, next, gen)

        self.assertRaises(TypeError, therevgen, 12)


if __name__ == '__main__':
    unittest.main()

    seq = ['a', 'b', 'c']
    for index, elem in revgen(seq):
        print(index, elem)

    for index, elem in spam.revgen(seq):
        print(index, elem)
