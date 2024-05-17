import random
import pygame
import time

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("GOMOKU")
screen = pygame.display.set_mode((720, 720))
# fps
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# TEXT FONTS
font_title = pygame.font.SysFont("oldenglishtext", 72)

# TEXT RENDER
display_title_screen1 = font_title.render("GOMOKU", True, BLACK)

# rectangles
board_base = pygame.Rect(0, 0, 689, 689)
board_horizontal = pygame.Rect(0, 0, 649, 1)
board_vertical = pygame.Rect(0, 0, 1, 649)

board_base.center = screen.get_rect().center
board_horizontal.center = board_base.center
board_vertical.center = board_base.center

# variables
board_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # DRAWING THE BOARD
    pygame.draw.rect(screen, pygame.Color("#ffd4a3"), board_base)
    # horizontal lines
    for i in range(19):
        # x coordinate is center of board
        # y coordinate is the top of the board + 20 (extra space around board) and 36i for the separation vertically
        board_horizontal.center = (board_base.center[1], (board_base.top + 20 + 36 * i))
        pygame.draw.rect(screen, pygame.Color("#000000"), board_horizontal)
    # vertical lines
    for i in range(19):
        # same thing as before, just vertical
        board_vertical.center = ((board_base.left + 20 + 36 * i), board_base.center[1])
        pygame.draw.rect(screen, pygame.Color("#000000"), board_vertical)

    # do i use this or a class
    # PROBABLY A CLASS
    black_stone = pygame.image.load("black_stone.png")
    black_center = black_stone.get_rect(center=screen.get_rect().center)
    screen.blit(black_stone, black_center)
    pygame.display.update()

    clock.tick(60)
