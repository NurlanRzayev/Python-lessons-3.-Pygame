import pygame
import sys

pygame.init()
pygame.display.set_mode((400, 300))

pygame.mixer.music.load('Images and sounds\Beethoven_-_opus47-3_03.ogg')
pygame.mixer.music.play()

sound1 = pygame.mixer.Sound('Images and sounds\mixkit-fast-game-explosion-1688.wav')
sound2 = pygame.mixer.Sound('Images and sounds\Metallica_-_One.ogg')

while 1:

    for i in pygame.event.get():
        
        if i.type == pygame.QUIT:
            sys.exit()
        
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(1)

        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                sound1.play()
            elif i.button == 3:
                sound2.play()

    pygame.time.delay(20)
