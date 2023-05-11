import turtle
import random

window=turtle.Screen()
turtle0=turtle.Turtle()
distance=25
angle=90
in_in_screen=True
turtle0.color("red")
turtle0.shape("turtle")

while in_in_screen:
    coin=random.randrange(0,2)
    if coin:
        turtle0.right(angle)
    else:
        turtle0.left(angle)
    turtle0.forward(distance)

    turtlex=turtle0.xcor()
    turtley=turtle0.ycor()
    xrange=window.window_width()/2
    yrange=window.window_height()/2

    if abs(turtlex)>xrange or abs(turtley)>yrange:
        in_in_screen=False