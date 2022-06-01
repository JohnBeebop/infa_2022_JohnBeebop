
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (172, 158, 158), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)
rect(screen, (0, 0, 0), (140, 240, 120, 20))

circle(screen, (255, 37, 31), (150, 170), 23)
circle(screen, (0, 0, 0), (150, 170), 10)
circle(screen, (0, 0, 0), (150, 170), 23, 1)

circle(screen, (255, 37, 31), (250, 170), 17)
circle(screen, (0, 0, 0), (250, 170), 10)
circle(screen, (0, 0, 0), (250, 170), 17, 1)

polygon(screen, (0, 0, 0), [(230, 160), (225, 150),
                            (300, 125), (305, 135)])
polygon(screen, (0, 0, 0), [(90, 115), (95, 105),
                            (185, 150), (180, 160)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()