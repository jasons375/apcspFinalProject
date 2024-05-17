import pygame
import random


class Fox:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color == "orange":
            self.image = pygame.image.load("orange-fox-sprite.png")
        elif color == "gray":
            self.image = pygame.image.load("gray-fox-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.current_direction = "right"

    def move_direction(self, direction):
        direction = direction.lower()

        if direction == "left":
            if self.current_direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = direction  # sets current direction to direction
            self.x -= self.delta

        elif direction == "right":
            if self.current_direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = direction  # sets current direction to direction
            self.x += self.delta

        elif direction == "up":
            self.y -= self.delta

        elif direction == "down":
            self.y += self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    # some code so i can randomize position of fox spawning
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rand_reposition(self, bounding_box):
        rand_x = random.randint(bounding_box.x, (bounding_box.width - self.rect.width))
        rand_y = random.randint(bounding_box.y, (bounding_box.height - self.rect.height))
        self.move(rand_x, rand_y)