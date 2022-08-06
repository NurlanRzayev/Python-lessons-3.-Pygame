import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

x=400
y=300
r=50

STOP='stop'
LEFT='left'
RIGHT='right'

motion=STOP

while True:
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                motion=LEFT
            elif i.key==pygame.K_RIGHT:
                motion=RIGHT
        elif i.type==pygame.KEYUP:
            if i.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                motion=STOP

    sc.fill((255,255,255))
    pygame.draw.circle(sc,(0,70,225),(x,y),r)
    pygame.display.update()

    if motion==LEFT:
        x-=3
    elif motion==RIGHT:
        x+=3

    clock.tick(30)