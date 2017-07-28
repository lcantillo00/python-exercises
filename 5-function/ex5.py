
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess,3,40)
# ////////////////////
t=3
for i in range(t):
    tess.forward(40)
    tess.left(360/t)
