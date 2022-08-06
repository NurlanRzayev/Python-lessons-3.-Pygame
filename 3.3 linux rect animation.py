import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()

RIGHT='right'
LEFT='left'

x=0
y=270#(600-60)/2

while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    sc.fill((255,255,255))
    pygame.draw.rect(sc,(0,0,200),(x,y,60,60))
    pygame.display.update()

    if x==940:
        direction=LEFT
    elif x==0:
        direction=RIGHT

    if direction==RIGHT:
    #увеличиваем х на такое значение которое делило бы 1000-60 без остатка , тогда в какой то момент х==940 будет
    #и квадрат не выйдет за пределы экрана 
        x+=5
    else:
        x-=5
    #на самом деле поставив условия x>=940 , x<=0 можно задать любое число для увеличения , уменьшения х
    #так как скорость цикла на столько велика что выход за край квадрата не замечается
    clock.tick(60)