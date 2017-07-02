from test import testEqual

class Point:
    """Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH

    def contains(self, point):
        # Your code here!
        dx=point.getX()
        dy=point.getY()
        np=self.width+dx,self.height+dy

        if np:
            return True
        else:
            return False

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)
