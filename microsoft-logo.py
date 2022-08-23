import turtle

ttl = turtle.Turtle()
ttl.hideturtle()
ttl.speed(8)
#  draw square
# ttl.back(100)


def draw_square():
    for i in range(4):
        ttl.forward(200)
        ttl.left(90)


def pen():
    # first square, 3rd quadrant(i.e. -x, -y)
    ttl.fillcolor('cyan')
    ttl.penup()
    ttl.goto(-200, -220)
    ttl.pendown()
    ttl.begin_fill()
    draw_square()
    ttl.end_fill()
    # 2nd square, 4th quadrant (i.e. x, -y)
    ttl.fillcolor('yellow')
    ttl.penup()
    ttl.goto(10, -220)
    ttl.pendown()
    ttl.begin_fill()
    draw_square()
    ttl.end_fill()
    # 3rd square, 2nd quadrant (i.e. -x, y)
    ttl.fillcolor('red')
    ttl.penup()
    ttl.goto(-200, -10)
    ttl.pendown()
    ttl.begin_fill()
    draw_square()
    ttl.end_fill()
    # 4th square, 1st quadrant(i.e. x, y)
    ttl.fillcolor('green')
    ttl.penup()
    ttl.goto(10, -10)
    ttl.pendown()
    ttl.begin_fill()
    draw_square()
    ttl.end_fill()


pen()

turtle.done()
