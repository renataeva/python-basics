import turtle
t = turtle.Pen()
a = int(input())
t.pencolor('#8384de')
t.fillcolor('red')
t.begin_fill()
for _ in range(4):
    t.forward(a/4)
    t.left(90)
t.end_fill()
turtle.Screen().exitonclick()
