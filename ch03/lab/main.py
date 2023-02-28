import random
import pygame
import math

pygame.init()

backcolor=("light blue")
cicrlecolor=(0,0,200)
hitcolor=(0,255,0)
misscolor=(255,0,0)
player1color=("white")
player2color=("black")
chosenplayer=0
buttonsize=75
buttondistance=10
player1score=0
player2score=0

print("Who do you predict will win? (Choose White or Black)")
window=pygame.display.set_mode()
windowx,windowy=pygame.display.get_window_size()
center=int(windowx)/2,int(windowy)/2
window.fill(backcolor)
pygame.draw.circle(window,'pink',center,center[1])
pygame.draw.line(window, "black", (340,425), (1180,425), 1)
pygame.draw.line(window, "black", (770,0), (770,2000), 1)


player1button=pygame.Rect(buttondistance,buttondistance,buttonsize,buttonsize)
drawing1button=pygame.draw.rect(window,player1color,player1button)
player2button=pygame.Rect(windowx-buttonsize-buttondistance,buttondistance,buttonsize,buttonsize)
drawing2button=pygame.draw.rect(window,player2color,player2button)
pygame.display.flip()

user_has_chosen=False

while not user_has_chosen:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            clickposition=event.pos
            if player1button.collidepoint(clickposition):
                print("You predict White will win...")
                user_has_chosen=True
                chosenplayer=1
            elif player2button.collidepoint(clickposition):
                print("you predict Black will win...")
                user_has_chosen=True
                chosenplayer=2

for i in range(10):
    throwx=random.randrange(0,windowx)
    throwy=random.randrange(0,windowy)
    farfromcenter=math.hypot(center[0]-throwx,center[1]-throwy)
    is_in_circle=farfromcenter<=center[1]
    if is_in_circle:
        dartcolor=player1color
        player1score=player1score+1
    else:
        dartcolor=misscolor
    pygame.draw.circle(window,dartcolor,(throwx,throwy),2)
    pygame.time.wait(1000)
    pygame.display.flip()

    throwx=random.randrange(0,windowx)
    throwy=random.randrange(0,windowy)
    farfromcenter=math.hypot(center[0]-throwx,center[1]-throwy)
    is_in_circle=farfromcenter<=center[1]
    if is_in_circle:
        dartcolor=('black')
        player2score=player2score+1
    else:
        dartcolor=misscolor
    
    if player1score>player2score:
        print("White wins! :D")
    elif player2score>player1score:
        print("Black wins! :D")
    else:
        print("It's a tie! :O")

pygame.display.update()
pygame.time.wait(1000)

