import pygame

# main program already has the place func
# this is just to make a lot of stones`

class Stone:
    def __init__(self, coordinates:tuple, color):
        self.coordinates = coordinates
        self.int_coordinates = ((ord(coordinates[0]) - 96), coordinates[1])

        if color.lower() == "white":
            self.image = pygame.image.load("white_stone.png")
        elif color.lower() == "black":
            self.image = pygame.image.load("black_stone.png")

