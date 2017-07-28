# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# def wagon(length, corners):
#
#     wheel = turtle.Turtle()
#     wheel.color("blue")
#     wheel.speed(0)
#
#     for corner in range(corners):
#         for i in range(4):
#             wheel.forward(length)
#             wheel.right(90)
#         wheel.left(360 / corners)
#
# wagon(125, 20)
#
# wn.exitonclick()
import turtle

win = turtle.Screen()
win.bgcolor("green")

def draw_square(length, turtle):
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)


def draw_grid(length, angle, turtle):
    # turtle.left(angle)
    for side in range(4):
        draw_square(length, turtle)
        turtle.left(90)

def pattern(lines):
    mike = turtle.Turtle()
    mike.speed(10)
    mike.color("blue")
    for angle in range(0, 85, int(90/lines)):
        mike.left(90)
        draw_grid(50,90, mike)

win = turtle.Screen()
win.bgcolor("green")
pattern(4)
win.exitonclick()
