import pygame
import sys

WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Rocket:

    width_rocket = 20
    height_rocket = 50

    def __init__(self, surface, color):
        """Конструктору необходимо передать
        поверхность, по которой будет летать
        ракета и цвет самой ракеты"""
        self.surf = surface
        self.color = color
        self.x = surface.get_width() // 2 - Rocket.width_rocket // 2
        self.y = surface.get_height() # методы поверхности get_width() и get_height() возвращают ее размеры

    def fly(self):
        """Вызов метода поднимает ракету
        на 3 пикселя.
        Если ракета скрывается вверху,
        она снова появится снизу"""
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.width_rocket, Rocket.height_rocket))
        self.y -= 3
        if self.y < - Rocket.height_rocket:
            self.y = WIN_HEIGHT

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
surf_left = pygame.Surface((WIN_WIDTH // 2, WIN_HEIGHT))
surf_right = pygame.Surface((WIN_WIDTH // 2, WIN_HEIGHT))
surf_left.fill(WHITE)
sc.blit(surf_left, (0, 0))
sc.blit(surf_right, (WIN_WIDTH // 2, 0))

rocket_left = Rocket(surf_left, BLACK)
rocket_right = Rocket(surf_right, WHITE) # обрати внимание, что в draw.rect() будет передаватся не главная оконная поверхность, а та которая принадлежит ракете. Отсюдо ясно что координаты для левого верхнего угла квадрата нужно давать в координатной системе поверхности этой ракеты. На самом деле координатные системы sc и surf_left полностью совпадают, ось OY surf_right симметрична оси OY sc и surf_left.

active_left = False
active_right = False

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.pos[0] < WIN_WIDTH // 2:
                active_left = True
                active_right = False
            elif i.pos[0] > WIN_WIDTH // 2:
                active_left = False
                active_right = True

    if active_left:
        surf_left.fill(WHITE)
        rocket_left.fly()
        sc.blit(surf_left, (0, 0))
    elif active_right:
        surf_right.fill(BLACK)
        rocket_right.fly()
        sc.blit(surf_right, (WIN_WIDTH // 2, 0))

    pygame.display.update()
    pygame.time.delay(20)