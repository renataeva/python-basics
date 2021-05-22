import turtle
t = turtle.Pen()


def settings(width=1, speed=2, pencolor='red', fillcolor='yellow'):
    t.width(width)
    t.speed(speed)
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)


def square(a, pen='blue', fill='green'):
    t.fillcolor(fill)
    t.pencolor(pen)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


settings(speed=6, width=4, )

square(30, 'orange', 'blue')
t.up()
t.forward(100)
t.down()
square(40)
t.right(90)
t.up()
t.forward(100)
t.down()
square(60, '#47cc9b', '#fc0f96')

turtle.Screen().exitonclick()