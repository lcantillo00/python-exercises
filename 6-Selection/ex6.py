# from test import testEqual
# import math
#
# def findHypot(a,b):
#     return math.sqrt( (a**2) + (b**2) )
#
# testEqual(findHypot(12.0, 5.0), 13.0)
# testEqual(findHypot(14.0, 48.0), 50.0)
# testEqual(findHypot(21.0, 72.0), 75.0)
# testEqual(findHypot(1, 1.73205), 1.999999)
from test import testEqual

def is_odd(n):
    # Your code here
    if n%2 !=0:
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)
