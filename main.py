import random
import pygame
import time
from stone import Stone


def conv_coords(stone, board, board_border_dist, square_dist):
    # stone and board should be Rect objects
    # location_1 sets the coordinates of the associated stone, with its corners at the intersection
    # location_2 adjusts the coordinates so that its center is at the intersection
    location_1 = (board.x + board_border_dist + (stone.coordinates[0] * square_dist)), (board.y + board_border_dist + (stone.coordinates[1] * square_dist))
    location_2 = (location_1[0] - (stone.size[0] / 2), location_1[1] - (stone.size[1] / 2))
    return location_2


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

# BOARD DRAWING
board_base = pygame.Rect(0, 0, 689, 689)
board_horizontal = pygame.Rect(0, 0, 649, 1)
board_vertical = pygame.Rect(0, 0, 1, 649)

board_base.center = screen.get_rect().center
board_horizontal.center = board_base.center
board_vertical.center = board_base.center

# VARIABLES
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
board_border = 20

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
        board_horizontal.center = (board_base.center[1], (board_base.top + board_border + 36 * i))
        pygame.draw.rect(screen, pygame.Color("#000000"), board_horizontal)
    # vertical lines
    for i in range(19):
        # same thing as before, just vertical
        board_vertical.center = ((board_base.left + board_border + 36 * i), board_base.center[1])
        pygame.draw.rect(screen, pygame.Color("#000000"), board_vertical)

    # PLACING STONES
    a = Stone((1, 1), "white")
    stones = [a]

    # BLIT STONES
    for stone in stones:
        screen.blit(stone.image, conv_coords(stone, board_base, board_border, 36))
    pygame.display.update()

    clock.tick(60)
