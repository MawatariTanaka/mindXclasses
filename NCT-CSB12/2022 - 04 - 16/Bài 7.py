import turtle
t = turtle.Turtle()
t.up()
t.pensize(1.5)


def draw_square(color, initx):
    t.pencolor(color)
    for i in range(10):
        t.setpos(initx, 30 + i)
        t.setheading(330)
        t.pendown()
        for j in range(2):
            t.forward(2 * (30 + i))
            t.right(120)
            t.forward(2 * (30 + i))
            t.right(60)
    t.up()


draw_square('#cf8f03', 0)
draw_square('#0b2c3c', 30)

t.screen.mainloop()
