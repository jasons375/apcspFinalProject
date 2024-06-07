import pygame


class RedRect:
    def __init__(self, coordinates: tuple):
        self.coordinates = coordinates
        self.image = pygame.image.load("red_rect.png")

        self.size = self.image.get_size()
