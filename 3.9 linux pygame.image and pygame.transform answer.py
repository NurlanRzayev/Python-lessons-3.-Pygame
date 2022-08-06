# -*- coding: utf-8 -*- # см. 2.9 Статические методы.py

import pygame
import sys

W = 400
H = 400
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)

car = pygame.image.load('Sprite-0001.png').convert()
car.set_colorkey((0, 0, 0))
rect = car.get_rect(center = (W // 2, H // 2))
sc.blit(car, rect)

pygame.display.update()

car1 = car
while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                car1 = pygame.transform.rotate(car, 90)
                flag = 'left'
            elif i.key == pygame.K_RIGHT:
                car1 = pygame.transform.rotate(car, -90)
                flag = 'right'
            elif i.key == pygame.K_UP:
                car1 = car
                flag = 'up'
            elif i.key == pygame.K_DOWN:
                car1 = pygame.transform.rotate(car, 180)
                flag = 'down'

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and flag == 'left':
        rect.centerx -= 3
    elif keys[pygame.K_RIGHT] and flag == 'right':
        rect.centerx += 3
    elif keys[pygame.K_UP] and flag == 'up':
        rect.centery -= 3
    elif keys[pygame.K_DOWN] and flag == 'down':
        rect.centery += 3

    sc.fill(WHITE)
    sc.blit(car1, rect)
    pygame.display.update()
    pygame.time.delay(20)

    # Здесь флаги нужны для того чтобы к примеру если зажав лево, зажать право машинка не двигалась задом в лево
    # Т. к. здесь rect не изменяется получая новые размеры от car1, машинка при повороте будет прорисовываться на фиксированных координатах rect, это означает что она будет поворачиваться не естевственно если изображение не квадратное (размеры квадрата меняясь местами остаются прежними)
