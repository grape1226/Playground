import turtle
turtle.pensize(5)
turtle.color('green')
turtle.penup()
for i in range(4):
    turtle.goto(0, 0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.right(90)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(4):
        turtle.circle(100,180)
        turtle.left(90)
    turtle.end_fill()
turtle.done()
