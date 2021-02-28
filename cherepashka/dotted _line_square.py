import turtle
t = turtle.Pen()
t.penup()
t.setposition(-200, -200)
t.width(3)
i = 1
while i != 5:
    for j in range(10):
        t.down()
        t.forward(10)
        t.up()
        t.forward(10)
    i+=1
    t.lt(90)

turtle.Screen().exitonclick()
