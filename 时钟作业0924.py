import turtle
import time
turtle.hideturtle()

turtle.tracer(0)
turtle.speed(0)
t = turtle.Pen()
miao = turtle.Pen()
fen = turtle.Pen()
shi = turtle.Pen()
miao.left(90)
while True:
    t.goto(0,0)
    t.dot(500,'yellow')
    t.dot(450, 'skyblue')
    t.goto(0, 0)
    t.penup()
    t.goto(0, (-210))
    t.pendown()
    for i in range(12):
        t.color('white')
        t.dot(20)
        t.penup()
        t.circle(210, 30)
        turtle.pendown()
    for i in range(60):
        t.color('white')
        t.dot(10)
        t.penup()
        t.circle(210, 6)
        turtle.pendown()
    t.hideturtle()
    miao.color('black')
    miao.pendown()
    miao.pensize(2)
    miao.forward(150)
    miao.penup()
    miao.goto(0, 0)
    miao.right(6)
    miao.hideturtle()

    fen.color('brown')
    fen.pendown()
    fen.pensize(5)
    fen.forward(120)
    fen.penup()
    fen.goto(0, 0)
    fen.right(0.1)
    fen.hideturtle()

    shi.color('red')
    shi.pendown()
    shi.pensize(10)
    shi.forward(60)
    shi.penup()
    shi.goto(0, 0)
    shi.right(0.0083)
    shi.hideturtle()

    turtle.update()
    time.sleep(1)
    turtle.clear()
turtle.done()
