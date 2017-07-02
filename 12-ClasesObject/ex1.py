import math
class Point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def distanceFromPoint(self,somepoint):
        dx=(somepoint.getX()-self.x)
        dy=(somepoint.getY()-self.y)
        return math.sqrt(dy**2 + dx**2)

p = Point(4, 3)
q = Point(6, 7)
print(p.distanceFromPoint(q))
