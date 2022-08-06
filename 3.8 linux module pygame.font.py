import pygame
import sys
pygame.font.init()

sc = pygame.display.set_mode((400, 400))

font = pygame.font.Font(None, 36)
text = font.render('Target locked', True, (255, 0, 0))
place = text.get_rect(center = (200, 100)) # координаты остальных точек поверхности вычесляются автоматически соотв. центру

target_rect = pygame.Rect(175, 175, 50, 50)

pygame.mouse.set_visible(False)

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((255, 255, 255))
    pygame.draw.circle(sc, (0, 0, 0), (200, 200), 25)

    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect(pos[0] - 5, pos[1] - 5, 10, 10)
        pygame.draw.circle(sc, (255, 0, 0), (pos[0], pos[1]), 5)
        if target_rect.contains(rect):
            sc.blit(text, place)

    pygame.display.update()
    pygame.time.delay(20)

