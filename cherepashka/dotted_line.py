import turtle
t = turtle.Pen()
t.penup()
t.setposition(-200, -200)
t.width(3)
while t.xcor() != 200:
    t.down()
    t.forward(10)
    t.up()
    t.forward(10)
turtle.Screen().exitonclick()
