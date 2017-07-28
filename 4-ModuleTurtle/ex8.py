import turtle

sc = turtle.Screen()
sc.bgcolor("lightgreen")

wolfram = turtle.Turtle()
wolfram.color("hotpink")
wolfram.speed(0)
wolfram.pensize(3)
wolfram.pu()
wolfram.forward(75)
wolfram.right(90)
wolfram.forward(75)
wolfram.left(90)

n = 5

def draw_star(t):
    t.down()
    for i in range(5):
        t.forward(100)
        t.left(216)
    t.pu()

for i in range(n):
    draw_star(wolfram)
    wolfram.left((360/n))
    wolfram.forward(100)
