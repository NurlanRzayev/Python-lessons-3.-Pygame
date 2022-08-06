import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((400,400))
sc.fill((255,255,255))
pygame.display.update()

while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                pygame.draw.circle(sc,(225,0,50),i.pos,20)
                pygame.display.update()
            elif i.button==3:
                pygame.draw.circle(sc,(0,0,225),i.pos,20)
                pygame.draw.rect(sc,(0,225,0),(i.pos[0]-10,i.pos[1]-10,20,20))
                pygame.display.update()
            elif i.button==2:
                sc.fill((255,255,255))
                pygame.display.update()
    
    pygame.time.delay(20)