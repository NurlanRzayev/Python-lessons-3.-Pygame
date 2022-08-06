import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

x=400
y=300
r=50

while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    sc.fill((255,255,255))
    pygame.draw.circle(sc,(0,70,225),(x,y),r)
    pygame.display.update()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=3
    if keys[pygame.K_RIGHT]: # если elif вместо if, то при зажатии обеих клавиш круг будет направлен в сторону соотв. последней зажатой клавише если первой была зажата правая, т. е. влево, и наоборот в сторону первой зажатой клавиши если первой была зажата левая, т. е. опять же влево
        x+=3

    clock.tick(30)