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
        self.surf = surface
        self.color = color
        self.x = surface.get_width() // 2 - Rocket.width_rocket // 2
        self.y = surface.get_height()

    def fly(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.width_rocket, Rocket.height_rocket))
        self.y -= 3
        if self.y < - Rocket.height_rocket:
            self.y = WIN_HEIGHT

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
rect_left = pygame.Rect(0, 0, WIN_WIDTH // 2, WIN_HEIGHT)
rect_right = pygame.Rect(WIN_WIDTH // 2, 0, WIN_WIDTH // 2, WIN_HEIGHT)
surf_left = pygame.Surface((rect_left.width, rect_left.height))
surf_right = pygame.Surface((rect_right.width, rect_right.height))
surf_left.fill(WHITE)
sc.blit(surf_left, rect_left)
sc.blit(surf_right, rect_right)
pygame.display.update() # сравни с linux class Surface and method blit lesson 2.py и смотри вниз

rocket_left = Rocket(surf_left, BLACK)
rocket_right = Rocket(surf_right, WHITE)

active_left = False
active_right = False

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            if rect_left.collidepoint(i.pos):
                active_left = True
                active_right = False
            elif rect_right.collidepoint(i.pos):
                active_left = False
                active_right = True

    if active_left:
        surf_left.fill(WHITE)
        rocket_left.fly()
        sc.blit(surf_left, rect_left)
        pygame.display.update(rect_left)
    elif active_right:
        surf_right.fill(BLACK)
        rocket_right.fly()
        sc.blit(surf_right, rect_right)
        pygame.display.update(rect_right)

    pygame.time.delay(20)