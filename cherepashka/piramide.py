import turtle
import random
t = turtle.Pen()
t.speed(0)
t.width(2)


def square(a, pen='black', fill='gray'):
    t.fillcolor(fill)
    t.pencolor(pen)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()

def circle(a, pen='black', fill='gray'):
    t.fillcolor(fill)
    t.pencolor(pen)
    t.begin_fill()
    t.circle(a)
    t.end_fill()


def recursion(side_length, pen_wight):
    if side_length <=20:
        return
    t.width(pen_wight)
    circle(side_length)
    t.up()
    t.left(90)
    t.fd(30)
    t.right(90)
    t.down()
    recursion(side_length-20, pen_wight-1)


recursion(200, 10)

turtle.Screen().exitonclick()
