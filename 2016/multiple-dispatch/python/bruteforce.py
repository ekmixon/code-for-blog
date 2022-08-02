# A "brute-force" solution using a chain of if-elif statements.
#
# Tested with Python 3.4
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.

class Shape:
    @property
    def name(self):
        return self.__class__

class Rectangle(Shape): pass

class Ellipse(Shape): pass

class Triangle(Shape): pass

def intersect(s1, s2):
    if isinstance(s1, Rectangle) and isinstance(s2, Ellipse):
        print(f'Rectangle x Ellipse [names s1={s1.name}, s2={s2.name}]')
    elif isinstance(s1, Rectangle) and isinstance(s2, Rectangle):
        print(f'Rectangle x Rectangle [names s1={s1.name}, s2={s2.name}]')
    else:
        # Generic shape intersection.
        print(f'Shape x Shape [names s1={s1.name}, s2={s2.name}]')


if __name__ == '__main__':
    r1 = Rectangle()
    r2 = Rectangle()
    e = Ellipse()
    t = Triangle()

    intersect(r1, e)
    intersect(r1, r2)
    intersect(t, e)
