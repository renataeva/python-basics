import turtle
import random
t = turtle.Pen()
t.speed(0)
t.width(2)


def star(ray_num, diam):
    t.pencolor((random.random(), random.random(), random.random()))
    for i in range(ray_num):
        t.forward(diam/2)
        t.backward(diam)
        t.forward(diam/2)
        t.left(360/ray_num)


for _ in range(random.randint(60, 70)):
    star(random.randint(5, 7), random.randint(20, 40))
    t.up()
    t.goto(random.randint(-250, 250), random.randint(-250, 250))
    t.down()


turtle.Screen().exitonclick()
