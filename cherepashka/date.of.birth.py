import turtle

WIDTH = 50
HEIGHT = 100
SIZE = 5
GAP = 15
BEGIN = -280


def goto(x):
    t.setposition(x, 0)


def dot(start, color):
    goto(start)
    t.pencolor(color)
    t.down()
    for _ in range(4):
        t.forward(SIZE)
        t.left(90)
    t.up()


def zero(start, color):
    goto(start)
    t.pencolor(color)
    t.down()
    for _ in range(2):
        t.forward(WIDTH)
        t.left(90)
        t.forward(HEIGHT)
        t.left(90)
    t.up()


def one(start, color):
    goto(start)
    t.pencolor(color)
    t.forward(WIDTH)
    t.down()
    t.left(90)
    t.forward(HEIGHT)
    t.up()
    t.right(90)


def two(start, color):
    goto(start)
    t.pencolor(color)
    t.left(90)
    t.forward(HEIGHT)
    t.down()
    t.right(90)
    t.forward(WIDTH)
    t.right(90)
    t.forward(HEIGHT/2)
    t.right(90)
    t.forward(WIDTH)
    t.left(90)
    t.forward(HEIGHT / 2)
    t.left(90)
    t.forward(WIDTH)
    t.up()


def seven(start, color):
    goto(start)
    t.pencolor(color)
    t.forward(WIDTH)
    t.down()
    t.left(90)
    t.forward(HEIGHT)
    t.left(90)
    t.forward(WIDTH)
    t.up()
    t.left(90)
    t.forward(HEIGHT/2)
    t.left(90)
    t.forward(WIDTH/2)
    t.pendown()
    t.forward(WIDTH)
    t.up()


def eight(start, color):
    goto(start)
    t.pencolor(color)
    t.down()
    for _ in range(2):
        t.forward(WIDTH)
        t.left(90)
        t.forward(HEIGHT)
        t.left(90)
    t.left(90)
    t.forward(HEIGHT / 2)
    t.right(90)
    t.forward(WIDTH)
    t.up()


t = turtle.Pen()
t.width(SIZE)
t.speed(3)
t.up()
goto(BEGIN)

# 0
s = BEGIN
zero(s, '#42ddf5')

# 8
s = s + WIDTH + GAP
eight(s, '#716be8')

# .
s = s + WIDTH + GAP
dot(s, '#42ddf5')

# 0
s = s + GAP
zero(s, '#42ddf5')

# 7
s = s + WIDTH + GAP
seven(s, '#f5b342')

# .
s = s + WIDTH + GAP
dot(s, '#42ddf5')

# 2
s = s + GAP
two(s, '#42f55d')

# 0
s = s + WIDTH + GAP
zero(s, '#42ddf5')

# 1
s = s + WIDTH + GAP
one(s, '#f542dd')

# 0
s = s + WIDTH + GAP
zero(s, '#42ddf5')

t.forward(WIDTH + GAP)
turtle.Screen().exitonclick()