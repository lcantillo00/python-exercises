# def grade(n):
#     if n>=90:
#         return "A"
#     else:
#         if 80<=n<90:
#             return "B"
#         else:
#             if 70<=n<80:
#                 return "C"
#             else:
#                 if 60<=n<70:
#                    return "D"
#                 else:
#                     return "F"
#
# mark = 83
# print( "Mark:", str(mark), "Grade:", grade(mark))
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    if height < 0:
        t.color(red)
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, 50,100, 200, 240, 160, 260, 220]
    max_height = max(data)
    min_height = min(data)
    num_bars = len(data)
    border = 10

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    if min_height > 0 :
        bottom = 0

    else:
        bottom = min_height - border

    wn.setworldcoordinates(0-border, bottom, 40 * num_bars + border, max_height + border)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()
