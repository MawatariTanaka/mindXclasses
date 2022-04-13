import turtle
my_window = turtle.Screen()
my_pen = turtle.Turtle()


def draw_square(size, border):
    my_pen.pensize(border)
    my_pen.up()
    my_pen.forward(size / 2)
    my_pen.right(90)
    my_pen.forward(size / 2)
    my_pen.down()
    for i in range(4):
        my_pen.right(90)
        my_pen.forward(size)
    my_pen.up()
    my_pen.backward(size / 2)
    my_pen.left(90)
    my_pen.backward(size / 2)


my_pen.left(90)
draw_square(100, 1)
draw_square(130, 3)
