import pygame
import sys

WIDTH = 700
HEIGHT = 300

sc = pygame.display.set_mode((WIDTH, HEIGHT))
surf = pygame.Surface((200, 200))

pygame.draw.circle(surf, (255, 0, 0), (75, 75), 75)
pygame.draw.line(surf, (0, 255, 0), (0, 150), (200, 150), 5)

x = 0
y = HEIGHT // 2 - 100

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((0, 0, 0))
    sc.blit(surf, (x, y))
    pygame.display.update()
    x += 3
    pygame.time.delay(20)