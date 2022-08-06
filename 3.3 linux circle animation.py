import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()

r=30
x=0-r
y=300

while True:
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    sc.fill((0,0,0))
    pygame.draw.circle(sc,(255,150,100),(x,y),r)
    pygame.display.update()

    if x>=1000+r:
        x=0-r
    else:
        x=x+2

    clock.tick(30)

