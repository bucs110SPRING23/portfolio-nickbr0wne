import turtle
import random
import math

window=turtle.screensize(1400,1000,"white")


x=random.randrange(1,10)
print(x)

turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle1.color("red")
turtle2.color('blue')
turtle1.shape('turtle')
turtle2.shape('turtle')
turtle1.speed(1)
turtle2.speed(1)

#race1

turtle1.penup()
turtle1.goto(-100,20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100,-20)
turtle2.pendown()

turtle1.forward(random.randrange(1,100))
turtle2.forward(random.randrange(1,100))


turtle1.penup()
turtle1.goto(-100,20)


turtle2.penup()
turtle2.goto(-100,-20)


#race2

turtle1.pendown()
turtle2.pendown()
for i in range(10):
    turtle1.forward(random.randrange(1,100))
    turtle2.forward(random.randrange(1,100))
turtle1.penup()
turtle1.goto(-100,20)
turtle2.penup()
turtle2.goto(-100,-20)


#part B

import pygame
import math

pygame.init()
window= pygame.display.set_mode()
xpos=900
ypos=450

def getpoints(num_sides, side_length):
    coords =[]
    for i in range(num_sides):
        angle=360/num_sides
        radians=math.radians(i*angle)
        x= xpos+side_length*math.cos(radians)
        y= ypos+side_length*math.sin(radians)
        t_list=(x,y)
        coords.append(t_list)
        pygame.display.flip()
    return coords

triangle=getpoints(3,250)
window.fill('white')
pygame.draw.polygon(window,'red',triangle)
pygame.time.wait(1000)

square=getpoints(4,250)
window.fill('white')
pygame.draw.polygon(window,'orange',square)
pygame.time.wait(1000)

hexagon=getpoints(6,250)
window.fill('white')
pygame.draw.polygon(window,'yellow',hexagon)
pygame.time.wait(1000)

icosagon=getpoints(20,250)
window.fill('white')
pygame.draw.polygon(window,'green',icosagon)
pygame.time.wait(1000)

hectagon=getpoints(100,250)
window.fill('white')
pygame.draw.polygon(window,'blue',hectagon)
pygame.time.wait(1000)


circleish=getpoints(360,250)
window.fill("white")
pygame.draw.polygon(window,'purple',circleish)
pygame.time.wait(1000)

circlenotshowing=getpoints(360,250)
window.fill("white")
pygame.draw.polygon(window,'white',circlenotshowing)
pygame.time.wait(3000)

pygame.quit()