import pygame
import sys
pygame.init()

sc = pygame.display.set_mode((400, 300))

surf_gate = pygame.Surface((100, 100))
surf_gate.fill((0, 255, 255))
rect_gate = surf_gate.get_rect(bottomright = (400, 300)) # объект класса Rect берет у объекта класса Surface размеры
sc.blit(surf_gate, rect_gate) # объект класса Surface берет у объекта класса Rect координаты левого верхнего угла

surf = pygame.Surface((50, 50))
surf.fill((255, 255, 0))
rect = surf.get_rect()
sc.blit(surf, rect)

font = pygame.font.Font(None, 24)
text = font.render('Yes!!!', True, (255, 255, 255))
rect_text = text.get_rect(topleft = (10, 10))

pygame.display.update()

flag = False

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(i.pos):
                flag = True
        elif i.type == pygame.MOUSEBUTTONUP:
            flag = False

    if flag:
        sc.fill((0, 0, 0))
        rect.center = pygame.mouse.get_pos()
        sc.blit(surf_gate, rect_gate)
        sc.blit(surf, rect)
        pygame.display.update()

    if rect_gate.contains(rect):
        sc.fill((0, 0, 0))
        sc.blit(text, rect_text)
        pygame.display.update(rect_text)

    pygame.time.delay(20)