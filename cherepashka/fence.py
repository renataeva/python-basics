import turtle
n = int(input())
t = turtle.Pen()
t.color('#808782')
t.fillcolor('#abb3ad')

t.up()
t.backward(100)
t.down()

i = 0
t.begin_fill()
while i < n:
    t.left(90)
    t.forward(50)
    t.right(45)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(45)
    t.forward(50)
    t.left(90)
    i += 1
t.end_fill()

turtle.Screen().exitonclick()
