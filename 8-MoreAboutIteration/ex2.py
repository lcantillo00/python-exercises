import turtle
import random
wn=turtle.Screen()
l=turtle.Turtle()
for i in range(40):
    x=random.randint(1,90)
    l.forward(40)
    l.left(x)
