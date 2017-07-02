import math
class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def reflect_x(self,newpoint):
        dx=newpoint.getX()
        dy=-newpoint.getY()
        return ( dx,dy)
p = Point(4, 3)
q = Point(3, 5)
print(p.reflect_x(q))
