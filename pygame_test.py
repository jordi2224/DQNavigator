import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
win.fill((255,255,255))
run = True
while run:
    pygame.draw.rect(win, (255,0,0), (0, 0, 60, 60))

    pygame.display.update()