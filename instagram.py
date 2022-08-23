import turtle

ttl = turtle.Turtle()
ttl.hideturtle()

ttl.circle(40)
ttl.penup()
ttl.goto(-50, -30)
ttl.pendown()


for i in range(4):
    ttl.forward(100)
    ttl.circle(22, 90)


# drawing flashlight in the top right corner of the logo.
ttl.penup()
ttl.goto(52, 98)
ttl.pendown()
ttl.dot(10)

turtle.done()
