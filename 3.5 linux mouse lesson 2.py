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

    pressed=pygame.mouse.get_pressed()
    pos=pygame.mouse.get_pos()

    if pressed[0]:
        pygame.draw.circle(sc,(0,0,225),pos,5)
        pygame.display.update()

    pygame.time.delay(20)