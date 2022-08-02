# Based on Guido's sample in https://www.artima.com/weblogs/viewpost.jsp?thread=101605
# with some small tweaks, and ported to Python 3.
#
# Tested with Python 3.4
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.

#
# This part is the multimethod "library".
#

class _MultiMethod:
    """Maps tuples of argument types to function to call for these types."""
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        try:
            return self.typemap[types](*args)
        except KeyError:
            raise TypeError(f'no match {self.name} for types {types}')

    def register_function_for_types(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function


# Maps function.__name__ -> _MultiMethod object.
_multi_registry = {}

def multimethod(*types):
    def register(function):
        name = function.__name__
        mm = _multi_registry.get(name)
        if mm is None:
            mm = _multi_registry[name] = _MultiMethod(name)
        mm.register_function_for_types(types, function)
        return mm
    return register

#
# From here on an example of client code: using multimethods for dispatching
# shape intersections.
#

class Shape:
    @property
    def name(self):
        return self.__class__

class Rectangle(Shape): pass

class Ellipse(Shape): pass

class Triangle(Shape): pass


@multimethod(Rectangle, Ellipse)
def intersect(r, e):
    print(f'Rectangle x Ellipse [names r={r.name}, e={e.name}]')

@multimethod(Rectangle, Rectangle)
def intersect(r1, r2):
    print(f'Rectangle x Rectangle [names r1={r1.name}, r2={r2.name}]')

@multimethod(Shape, Shape)
def intersect(s1, s2):
    print(f'Shape x Shape [names s1={s1.name}, s2={s2.name}]')


if __name__ == '__main__':
    r1 = Rectangle()
    r2 = Rectangle()
    e = Ellipse()

    intersect(r1, e)
    #intersect(e, r1)
    #intersect(r1, r2)
