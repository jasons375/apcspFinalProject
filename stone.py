import pygame


# main program already has the place func
# this is just to make a lot of stones`

class Stone:
    def __init__(self, coordinates: tuple, color):
        self.coordinates = coordinates
        # self.int_coordinates = ((ord(coordinates[0]) - 96), coordinates[1])

        if color == "white" or color == 1:
            self.image = pygame.image.load("images/white_stone.png")
        elif color == "black" or color == -1:
            self.image = pygame.image.load("images/black_stone.png")

        self.size = self.image.get_size()
