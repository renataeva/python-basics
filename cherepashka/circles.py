import turtle
import random
r = 250
t = turtle.Pen()
t.setposition(0, -260)

while r > 0:
    t.fillcolor(random.random(), random.random(), random.random())
    t.pencolor((random.random(), random.random(), random.random()))
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r -= 10

turtle.Screen().exitonclick()
