import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((800,600))

x=400
y=300
r=50

STOP='stop'
LEFT='left'
RIGHT='right'

motion=STOP
x1=1

while True:
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                x1=x
                motion=LEFT
            elif i.key==pygame.K_RIGHT:
                x1=x
                motion=RIGHT
        elif i.type==pygame.KEYUP:
            if i.key==pygame.K_LEFT:
                motion=RIGHT
            elif i.key==pygame.K_RIGHT:
                motion=LEFT

    sc.fill((255,255,255))
    pygame.draw.circle(sc,(0,70,225),(x,y),r)
    pygame.display.update()

    if motion==LEFT:
        x=x-3
    elif motion==RIGHT:
        x=x+3
    if x == x1:
        motion = STOP

    pygame.time.delay(20)

    # в этой программе также как и в linux keyboard lesson.py круг ведет себя не 'естественно' при зажатии обеих клавиш, вплоть до того что бесконечно движется вправо если нажать лево, потом не отпуская лево нажать право, отпустить поочередно право и лево (см. алгоритм) 

