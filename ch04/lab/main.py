import pygame
import random
import math

pygame.init()
pygame.event.get()
window=pygame.display.set_mode((800,800))

button = {
    "white": pygame.Rect(230,400,100,100),
    "black": pygame.Rect(570,400,100,100),
}
whitescore = 0
blackscore = 0
choice=True
darts=False
guess=''
font=pygame.font.Font(None, 30)
center=800/2

while choice==True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button['white'].collidepoint(event.pos):
             guess='white'
             choice=False
             darts=True
            elif button['black'].collidepoint(event.pos):
                guess='black'
                choice=False
                darts=True

    window.fill('grey')
    text=font.render('Who will win?', True, "black")
    window.blit(text, (100, 100))
    pygame.draw.rect(window, 'white', button['white'])
    pygame.draw.rect(window, 'black', button['black'])
    pygame.display.flip()

while darts == True:
    window.fill("white")
    pygame.draw.circle(window,'blue', (center,center), 400)

    for i in range (10):
        white_y=random.randrange(0,800)
        white_x=random.randrange(0,800)
        white_fromcenter=math.hypot(center-white_x, center-white_y)
        if white_fromcenter <= 400:
            is_in_circle=True
            pygame.draw.circle(window, "white", (white_x,white_y), 5)
            whitescore=whitescore+1
        else:
            is_in_circle=False
            pygame.draw.circle(window, "red", (white_x,white_y), 5)
        pygame.display.flip()
        pygame.time.wait(1000)

        black_y=random.randrange(0,800)
        black_x=random.randrange(0,800)
        black_fromcenter=math.hypot(center-black_x, center-black_y)
        if white_fromcenter <= 400:
            in_circle=True
            pygame.draw.circle(window, "black", (black_x,black_y), 5)
            whitescore=whitescore+1
        else:
            in_circle=False
            pygame.draw.circle(window, "red", (black_x,black_y), 5)
        pygame.display.flip()
        pygame.time.wait(1000)

    if (whitescore<blackscore and guess == 'white') or (blackscore<whitescore and guess == 'black'):
        text = font.render("You lose. :(", False, 'black')
    if (whitescore>blackscore and guess == 'white') or (blackscore>whitescore and guess == 'black'):
        text = font.render("You win! :D", True, 'black')
    else:
         text = font.render("Tie.", True, 'black')

    window.fill('white')
    window.blit(text, (100,100))
    pygame.display.flip()
    pygame.time.wait(3000)
    darts=False

pygame.display.quit()
