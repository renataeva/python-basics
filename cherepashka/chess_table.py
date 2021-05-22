import turtle
t = turtle.Pen()
t.speed(0)


def square(a, pen='black', _fill='black'):
    t.fillcolor(_fill)
    t.pencolor(pen)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


for i in range(8):
    if i % 2 == 0:
        fill = 'black'
    else:
        fill = 'white'
    for j in range(8):
        square(30, _fill=fill)
        t.penup()
        t.forward(30)
        t.down()
        if fill == 'black':
            fill = 'white'
        else:
            fill = 'black'
    t.up()
    t.backward(240)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
turtle.Screen().exitonclick()
