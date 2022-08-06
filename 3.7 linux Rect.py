import pygame
import sys

SIDE = 300
C = SIDE // 2
WHITE = (255, 255, 255)
col = 0
col_flag = '+'
TL_BR = 'top left, bottom right'
TR_BL = 'top right, bottom left'

sc = pygame.display.set_mode((SIDE, SIDE))
sc.fill(WHITE)

r1 = pygame.Rect(C, 0, C, C) # против часовой стрелки
r2 = pygame.Rect(0, 0, C, C)
r3 = pygame.Rect(0, C, C, C)
r4 = pygame.Rect(C, C, C, C)

flag = 0
while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                flag = TL_BR
            elif i.key == pygame.K_2:
                flag = TR_BL
            elif i.key == pygame.K_0:
                flag = 0

    pygame.draw.circle(sc, (col, col, col), (C, C), C - 10)
    if flag == TL_BR:
        pygame.display.update([r2, r4])
    elif flag == TR_BL:
        pygame.display.update([r1, r3])
    else:
        pygame.display.update()
    pygame.time.delay(20)

    if col_flag == '+':
        col += 3
    else:
        col -= 3

    if col == 255:
        col_flag = '-'
    elif col == 0:
        col_flag = '+'

# Внимание: при работе программы будет казаться что цвет в определенные моменты меняется и в двух других дигональных четвертях окружности при flag != 0, но это обман зрения



