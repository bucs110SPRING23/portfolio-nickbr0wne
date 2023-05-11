import pygame
pygame.init()

screen=pygame.display.set_mode()
dimensions=screen.get_size()
starting_point=(dimensions[0]//2, dimensions[1]//2+120)
pygame.draw.circle(screen, "red", starting_point, 200)
starting_point=(dimensions[0]//2, dimensions[1]//2-150)
pygame.draw.circle(screen, "blue", starting_point, 130)
starting_point=(dimensions[0]//2, dimensions[1]//2-300)
pygame.draw.circle(screen, "purple", starting_point, 60)

pygame.display.flip()
pygame.time.wait(400)
input()