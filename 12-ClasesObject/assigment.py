class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # TODO define a method called slopeFromOrigin here
    def slopeFromOrigin(self):
             return None if self.x == 0 else self.y / self.x

# some tests to check your code
from test import testEqual
testEqual( Point(4, 10).slopeFromOrigin(), 2.5 )
testEqual( Point(5, 10).slopeFromOrigin(), 2 )
testEqual( Point(0, 10).slopeFromOrigin(), None )
testEqual( Point(20, 10).slopeFromOrigin(), 0.5 )
testEqual( Point(20, 20).slopeFromOrigin(), 1 )
testEqual( Point(4, -10).slopeFromOrigin(), -2.5 )
testEqual( Point(-4, -10).slopeFromOrigin(), 2.5 )
testEqual( Point(-6, 0).slopeFromOrigin(), 0 )


# //////////////////////////////////////////////////////////////
# TODO: add the Car class
class Car:
    def __init__(self,gas_level):
        self.gaslevel=gas_level
    def add_gas(self):
        return self.gaslevel
    def fill_up(self):
        if self.gaslevel==13 :
            return 0
        else:
            if (13-self.gaslevel)<=0:
                return 0
            else:
                return 13-self.gaslevel
    

# some tests to check your code, Do Not Post These in Vocareum
from test import testEqual
testEqual( Car(10).fill_up(), 3 )
testEqual( Car(20).fill_up(), 0 )
testEqual( Car(5.5).fill_up(), 7.5 )
testEqual( Car(12.5).fill_up(), 0.5 )
testEqual( Car(13).fill_up(), 0 )

my new carr assigment
class Car():
    def __init__(self,gas_level):
        self.gas_level=float(gas_level)
    def add_gass(self,amount):
         self.gass_level=float(amount)
        
    
    
    def fill_up(self):
        if self.gas_level<13:
            result= 13-self.gas_level
        else:
            result= 0
          
        return result