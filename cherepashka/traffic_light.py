import turtle

t = turtle.Pen()
t.speed(1)

t.width(50)
t.left(90)
colors = ['#43c232', 'yellow', 'red']
for c in colors:
    t.pendown()
    t.pencolor(c)
    t.circle(0)
    t.penup()
    if c == 'red':
        t.forward(30)
    else:
        t.forward(51)


t.left(90)
t.backward(30)
t.width(2)
t.pencolor('#7a4e22')
t.pendown()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(160)
    t.left(90)

turtle.Screen().exitonclick()
