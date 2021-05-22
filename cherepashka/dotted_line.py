import turtle

p = turtle.Pen()

p.penup()
p.setposition(-200, -200)
p.width(3)

while p.xcor() != 200:
    p.down()
    p.forward(10)
    p.up()
    p.forward(10)

turtle.Screen().exitonclick()
