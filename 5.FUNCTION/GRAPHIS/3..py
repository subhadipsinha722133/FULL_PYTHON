import turtle
distance = 0.2
angle = 45

turtle.pencolor("blue")   # Set pen color

#turtle.penup()                               # Left pen to move it

turtle.setposition(0, 0)               # Position the pen at coordinates (0, 0)

#turtle.pendown()                             # Set pen down to begin drawing

for i in range(100):
    turtle.forward(distance)
    turtle.left(angle)
    distance += 0.5

turtle.hideturtle()                              # Make pen invisible
turtle.exitonclick()
