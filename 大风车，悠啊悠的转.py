import turtle
import time
turtle.bgcolor('grey')
turtle.speed(0)
turtle.tracer(0)
while True:
    turtle.color('black')
    turtle.pensize(20)
    turtle.goto(0,-400)
    turtle.goto(0,0)
    r = 100
    colors = ['red','pink','green','purple']
    turtle.pensize(1)
    for c in colors:
        turtle.color(c)
        turtle.begin_fill()
        turtle.fd(r*2)
        turtle.left(90)
        turtle.circle(r,180)
        turtle.end_fill()
    turtle.update()
    time.sleep(0.0000000000001)
    turtle.clear()
    turtle.right(1000000000000)
turtle.done()