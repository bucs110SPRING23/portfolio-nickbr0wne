import pygame 
import random
import math

pygame.init()
window=pygame.display.set_mode((600, 600))
screen_size=window.get_size()
center_of_screen=(screen_size[0]/2, screen_size[1]/2)
half_width=screen_size[0]/2
half_height=screen_size[1]/2
width=screen_size[0]
height=screen_size[1]
window.fill("white")
pygame.draw.circle(window, "black", center_of_screen, half_height) 
pygame.draw.circle(window, "grey", center_of_screen, half_height - 5)
pygame.draw.line(window, "black", (half_width, 0), (half_width, height), 3)
pygame.draw.line(window, "black", (0, half_height), (width, half_height), 3)

for i in range(10):
    dart2x=random.randrange(0, width)
    dart2y=random.randrange(0, height)
    dart2_distance=math.hypot(dart2x-half_width, dart2y-half_height)
    in_circle_dart_2=(dart2_distance<=half_width)  
    if (in_circle_dart_2):
        pygame.draw.circle(window, "green", [dart2x, dart2y], 5)
    else:
        pygame.draw.circle(window, "red", [dart2x, dart2y], 5)
pygame.display.flip()
pygame.time.wait(3000)