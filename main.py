import random
import pygame
import time

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("GOMOKU")
screen = pygame.display.set_mode((689, 689))
# fps
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# TEXT FONTS
font_title = pygame.font.SysFont("oldenglishtext", 72)

# TEXT RENDER
display_title_screen1 = font_title.render("GOMOKU", True, BLACK)

# variables

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    end_msg_center = display_end_msg.get_rect(center=screen.get_rect().center)
    pygame.display.update()

    clock.tick(60)