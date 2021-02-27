import turtle

t = turtle.Pen()

for _ in range(4):
    t.forward(50)
    t.left(90)

t.up()
t.left(180)
t.forward(100)
t.down()

for _ in range(4):
    t.forward(50)
    t.up()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.down()

t.up()
t.right(90)
t.forward(100)
t.down()

for _ in range(3):
    t.forward(30)
    t.right(120)

t.up()
t.right(90)
t.forward(200)
t.down()

for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(75)
    t.left(90)

turtle.Screen().exitonclick()
