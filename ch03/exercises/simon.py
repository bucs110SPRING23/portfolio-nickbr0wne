# simon says 

import pygame
import random
pygame.init()
screen=pygame.display.set_mode()
colors=["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip
    pygame.time.wait(250)
