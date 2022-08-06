import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((400,400))

pygame.mouse.set_visible(False)

while True:
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    sc.fill((255,255,255))
    
    if pygame.mouse.get_focused():
        pos=pygame.mouse.get_pos()
        pygame.draw.rect(sc,(0,0,225),(pos[0]-10,pos[1]-10,20,20))
    
    pygame.display.update()
    pygame.time.delay(20)