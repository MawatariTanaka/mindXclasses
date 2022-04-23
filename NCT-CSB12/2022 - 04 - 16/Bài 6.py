import turtle


def changepos(turtle, newx, newy):
    turtle.up()
    turtle.setpos(newx, newy)
    turtle.pendown()


t = turtle.Turtle()
changepos(t, -50, -20)
t.forward(100)
changepos(t, -50, -100)
t.forward(100)

t.pencolor('#de5246')
t.pensize(3)
t.left(90)
t.forward(80)
t.left(135)
t.forward(70.7)
changepos(t, -50, -100)
t.setheading(90)
t.forward(80)
t.right(135)
t.forward(70.7)

t.up()
t.home()
t.setheading(90)
t.screen.mainloop()
