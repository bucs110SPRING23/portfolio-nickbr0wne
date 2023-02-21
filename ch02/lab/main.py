import turtle #1
import random

import pygame
import math

#Part A
window = turtle.Screen() #2
window.bgcolor('lightblue')

turtle1 = turtle.Turtle() #3
turtle2 = turtle.Turtle()
turtle1.color('pink')
turtle2.color('blue')
turtle1.shape('turtle')
turtle2.shape('turtle')

turtle1.up() 
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)

range1 = random.randrange(1,100)
range2 = random.randrange(1,100)
print(range1, range2)

turtle1.forward(range1)
turtle2.forward(range2)
print(range1, range2)

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

range3 = random.randrange(1,10)
range4 = random.randrange(1,10)
print(range3, range4)

for i in range(0,10):
    range3 = random.randrange(1,10)
    range4 = random.randrange(1,10)
    turtle1.forward(range3)
    turtle2.forward(range4)

turtle1.goto(-100,20)
turtle2.goto(-100,20)

#Part B
import pygame
import math

pygame.init()
window = pygame.display.set_mode()
surface = pygame,display.get_surface()
def shape_points(num_sides):
    coords = []
    num_sides = num_sides
    side_length = 100
    offset = 150

for i in range(num_sides):
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    t_list = (x,y)
    coords.append(t_list)
    return coords

pygame.display,polygon(surface, "gold", shape_points(3))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

pygame.display,polygon(surface, "green", shape_points(4))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

pygame.display,polygon(surface, "red", shape_points(6))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

pygame.display,polygon(surface, "orange", shape_points(20))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

pygame.display,polygon(surface, "purple", shape_points(100))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

pygame.display,polygon(surface, "green", shape_points(360))
pygame.display.flip()
pygame.time.wait(200)
window.fill("black")

turtle.done()
window.exitonclick()