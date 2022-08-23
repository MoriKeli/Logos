# drawing YouTube logo with turtle.
import turtle

ttl = turtle.Turtle()
w = 300     # width of rectangle
h = 200     # height of the rectangle
ttl.color('red')    # fill and outline of the rectangle. fill_color('red') also works
ttl.hideturtle()    # hide turtle cursor

ttl.penup()
ttl.goto(-150, -10)
ttl.pendown()

ttl.begin_fill()

for i in [w, h]*2:  # perimeter of a rectangle = 2(w+h)
    ttl.forward(i)
    ttl.circle(15, 90)  # draw curve of radius 15 at angle 90.

ttl.end_fill()

ttl.penup()
ttl.goto(-40, 50)
ttl.pendown()

ttl.color('white')
ttl.begin_fill()

for i in [30, 120]:    # an isosceles triangle has two equal sides.
    print(i)
    ttl.left(i)
    ttl.forward(100)

ttl.end_fill()

turtle.done()
