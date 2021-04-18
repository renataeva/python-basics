import turtle
n =289
t = turtle.Pen()
t.color('#808782')

while n > 0:
    t.forward(n)
    t.left(90)
    n -= 10

turtle.Screen().exitonclick()
