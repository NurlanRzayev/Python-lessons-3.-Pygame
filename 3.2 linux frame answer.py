import pygame
import sys

pygame.init()
pygame.display.set_mode((600,400))
clock=pygame.time.Clock()

titles=['game1','game2']
id_title=0

while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()

    pygame.display.set_caption(titles[id_title])

    if id_title<len(titles)-1:
        id_title+=1
    else:
        id_title=0

    clock.tick(1)