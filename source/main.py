import pygame

pygame.init()

Width-Screen = 600
Height-Screen = 300

Screen = pygame.display.set_mode((Width-Screen, Heighr-Screen))

class Game:
    def __init__(self):
        Running = True
        while Running = True:
            for Event in pygame.event.get():
                if Event.type == QUIT:
                    pygame.quit()
