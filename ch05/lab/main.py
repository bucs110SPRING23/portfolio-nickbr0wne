import pygame

##part a
def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count 

def threenp1range(upper_limit):
    objsequence = {}
    for x in range(2,upper_limit+1):
       objsequence[x] = threenp1(x)
    return objsequence

##part b
def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    window = pygame.display.set_mode()
    threenplus1_iters_dict = threenp1range(threenplus1_iters_dict)
    pos = [(i,i2) for i, i2 in threenplus1_iters_dict.items()]

    pygame.draw.lines(window, "green", True, pos)
    
    new_display = pygame.transform.flip(window, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width*10,height*0.5))
    window.blit(new_display, (0, 0))

    
    for x,y in pos:
        max_so_far = (0,0)
        if y > max_so_far[1]:
          max_so_far = (x,y)
    font = pygame.font.Font(None,60)
    text = font.render("Max value is: "+str(max_so_far[1]), True, "green")
    window.blit(text, (760,540))
def main():
    upper_limit = int(input("Insert upper limit:"))
    print(threenp1range(upper_limit))
    graph_coordinates(upper_limit)
    pygame.display.flip()
    pygame.time.wait(1500)

main()