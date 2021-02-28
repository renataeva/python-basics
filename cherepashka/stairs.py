import turtle
t = turtle.Pen()
t.penup()
t.setposition(-200, -200)
t.width(3)
i = 1
while t.xcor() != 100:
    t.down()
    t.lt(90)
    t.forward(10)
    t.rt(90)
    t.forward(10)