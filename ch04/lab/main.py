import pygame
import random
import math

pygame.init()
window=pygame.display.set_mode((800, 800))
screen_size=window.get_size()
center_of_screen=(screen_size[0]/2, screen_size[1]/2)
half_width=screen_size[0]/2
half_height=screen_size[1]/2
width=screen_size[0]
height=screen_size[1]
window.fill("white")
pygame.draw.circle(window, "black", center_of_screen, half_height) 
pygame.draw.circle(window, "orange", center_of_screen, half_height - 5)
pygame.draw.line(window, "black", (half_width, 0), (half_width, height), 3)
pygame.draw.line(window, "black", (0, half_height), (width, half_height), 3)

for i in range(10): 
    dart1x=random.randrange(0, width)
    dart1y=random.randrange(0, height)
    dart2x=random.randrange(0, width)
    dart2y=random.randrange(0, height)
    dart1_distance=math.hypot(dart1x-half_width, dart1y-half_height)
    dart2_distance=math.hypot(dart2x-half_width, dart2y-half_height)
    in_circle_dart_1=(dart1_distance<=half_width)
    in_circle_dart_2=(dart2_distance<=half_width)
    if (in_circle_dart_1):
        pygame.draw.circle(window, "purple", [dart1x, dart1y], 10)
    else:
        pygame.draw.circle(window, "pink", [dart1x, dart1y], 10)
        
    if (in_circle_dart_2):
        pygame.draw.circle(window, "dark green", [dart2x, dart2y], 10)
    else:
        pygame.draw.circle(window, "green", [dart2x, dart2y], 10)
pygame.display.flip()
pygame.time.wait(2000)