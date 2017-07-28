class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    def reflect_x(self, newpoint):
        newx=newpoint.get_x()
        newy=-newpoint.get_y()
        return (newx,newy)
p = Point(4, 3)
q = Point(3, 5)
print(p.reflect_x(q))
# ///////////////////////////////////////////////////////////////////////////
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    def reflex_x(self):
        newx=self.x
        newy=-self.y
        return (newx,newy)
def main():
        p=Point(3,5)
        r=p.reflex_x()
        print(r)

if __name__ == "__main__":
    main()
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    def reflex_x(self):
        newx=self.x
        newy=-self.y
        return (newx,newy)
def main():
        p=Point(3,5)
        r=p.reflex_x()
        print(r)

if __name__ == "__main__":
    main()
