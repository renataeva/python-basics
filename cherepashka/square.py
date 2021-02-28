import turtle
t = turtle.Pen()
a = int(input())
t.pencolor('#8384de')
t.fillcolor('yellow')
t.begin_fill()
for _ in range(4):
    t.forward(a)
    t.left(90)
t.end_fill()
turtle.Screen().exitonclick()
