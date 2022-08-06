import pygame
import sys

pygame.init()
sc=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

bomb=False
x_goal=0
y_goal=0
y_bomb=615

while True:
    
    sc.fill((255,255,255))
    pygame.display.update()
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1 and not bomb:
                bomb=True
                x_goal=i.pos[0]
                y_goal=i.pos[1]

    if bomb and y_bomb>y_goal:
        pygame.draw.circle(sc,(0,0,0),(x_goal,y_bomb),15)
        pygame.display.update()
        y_bomb-=10
    elif bomb and y_bomb<=y_goal:
        pygame.draw.rect(sc,(255,0,0),(x_goal-15,y_bomb-15,30,30))
        pygame.display.update()
        pygame.time.delay(500)
        bomb=False
        y_bomb=615

    clock.tick(60)
    
        
    