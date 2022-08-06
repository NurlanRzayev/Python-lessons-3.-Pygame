import pygame
import sys

sc = pygame.display.set_mode((400, 300))
sc.fill((100, 150, 200))

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
STOP = 'stop'

x = 200
y = 150

car = pygame.image.load('Sprite-0004.PNG').convert()
car.set_colorkey((0, 0, 0))
car_rect = car.get_rect(center = (x, y))
sc.blit(car, car_rect)
pygame.display.update()

car_turn = car

flag = STOP
while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                flag = UP
            elif i.key == pygame.K_DOWN:
                flip = pygame.transform.flip(car, False, True) # функция flip() переворачивает
                flag = DOWN
            elif i.key == pygame.K_LEFT:
                rot1 = pygame.transform.rotate(car, 90) # функция rotate() поворачивает
                flag = LEFT
            elif i.key == pygame.K_RIGHT:
                rot2 = pygame.transform.rotate(car, -90)
                flag = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                flag = STOP

    if flag == UP:
        y -= 3
        car_turn = car
    elif flag == DOWN:
        y += 3
        car_turn = flip
    elif flag == LEFT:
        x -= 3
        car_turn = rot1
    elif flag == RIGHT:
        x += 3
        car_turn = rot2

    sc.fill((100, 150, 200))
    car_rect = car_turn.get_rect(center = (x, y)) # т. к. размеры car_turn меняются местами при повороте, нужно каждый раз создавать новый car_rect по новым размерам car_turn. Также координаты car_rect зависят от переменных x, y
    sc.blit(car_turn, car_rect)
    pygame.display.update()
    pygame.time.delay(20)
