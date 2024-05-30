import random
import pygame
import time
import math
from stone import Stone


def conv_coords(stone, board, board_border_dist, square_dist):
    # stone and board should be Rect objects
    # location_1 sets the coordinates of the associated stone, with its corners at the intersection
    # location_2 adjusts the coordinates so that its center is at the intersection
    location_1 = (board.x + board_border_dist + (stone.coordinates[0] * square_dist)), (board.y + board_border_dist + (stone.coordinates[1] * square_dist))
    location_2 = (location_1[0] - (stone.size[0] / 2), location_1[1] - (stone.size[1] / 2))
    return location_2


def check_5_in_a_row(grid, coordinates):
    if grid[coordinates[1]][coordinates[0]] == 0:       # if u do this ur dumb
        return False
    else:
        color = grid[coordinates[1]][coordinates[0]]
    directions = ("E", "SE", "S", "SW")
    directions_dict = {"E": (1, 0), "SE": (1, -1), "S": (0, -1), "SW": (-1, -1)}
    for direction in directions:
        stones_in_a_row = 1
        delta_x, delta_y = directions_dict[direction]
        # forwards
        i = 1
        while grid[coordinates[1] + i*delta_y][coordinates[0] + i*delta_x] == color:
            stones_in_a_row += 1
            i += 1
        # backwards
        i = 1
        while grid[coordinates[1] - i*delta_y][coordinates[0] - i*delta_x] == color:
            stones_in_a_row += 1
            i += 1
        if stones_in_a_row >= 5:
            return True
    return False


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



# VARIABLES
# GAME STATE
# board
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
# placing stuff
turn = 1        # white = 1, black = 2
mouse_can_click = False
mouse_place_coords = (0, 0)
game_won = False
game_winner = ""


# BOARD DRAWING
board_base = pygame.Rect(0, 0, 649 + 2*board_border, 649 + 2*board_border)
board_horizontal = pygame.Rect(0, 0, 649, 1)
board_vertical = pygame.Rect(0, 0, 1, 649)

board_base.center = screen.get_rect().center
board_horizontal.center = board_base.center
board_vertical.center = board_base.center

# misc
stones = []

# -------- Main Program Loop -----------
while True:
    # detecting mouse pos
    # j, i = x, y
    for i in range(19):
        for j in range(19):
            current_board_coordinate = ((board_base.x + board_border + (36 * j)), (board_base.y + board_border + (36 * i)))
            if math.dist(pygame.mouse.get_pos(), current_board_coordinate) < 15:        # if mouse is within 15 pixels
                mouse_place_coords = (j, i)
                if board_state[mouse_place_coords[1]][mouse_place_coords[0]] == 0:      # if that board coord is empty
                    mouse_can_click = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # detects click
        if mouse_can_click:
            if event.type == pygame.MOUSEBUTTONUP:
                # update board
                board_state[mouse_place_coords[1]][mouse_place_coords[0]] = turn
                stones.append(Stone(mouse_place_coords, turn))
                mouse_can_click = False
                if check_5_in_a_row(board_state, mouse_place_coords):
                    game_won = True
                    if turn == 1:
                        game_winner = "white"
                    elif turn == -1:
                        game_winner = "black"
                turn *= -1
    print(game_winner)



    # --- BLIT ----
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
    # DRAWING THE STONES
    for stone in stones:
        screen.blit(stone.image, conv_coords(stone, board_base, board_border, 36))
    pygame.display.update()

    clock.tick(60)
