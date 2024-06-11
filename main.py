import random
import pygame
import time
import math
from stone import Stone
from red_rect import RedRect


def conv_coords(object_top, object_grid, border_thickness, tile_size):
    # object_top and object_bottom should be Rect objects
    # object_top is the thing to be blitted
    # location_1 sets the coordinates of the associated stone, with its corners at the intersection
    # location_2 adjusts the coordinates so that its center is at the intersection
    location_1 = (object_grid.x + border_thickness + (object_top.coordinates[0] * tile_size)), (object_grid.y + border_thickness + (object_top.coordinates[1] * tile_size))
    location_2 = (location_1[0] - (object_top.size[0] / 2), location_1[1] - (object_top.size[1] / 2))
    return location_2


def check_5_in_a_row(grid, coordinates):
    # coordinates use index 0
    color = grid[coordinates[1]][coordinates[0]]        # 1: white, -1: black
    if color == 0:       # if u do this ur dumb
        return True, []
    directions = ("E", "SE", "S", "SW")
    directions_dict = {"E": (1, 0), "SE": (1, -1), "S": (0, -1), "SW": (-1, -1)}

    for direction in directions:
        five_in_a_row_coords = [coordinates]
        stones_in_a_row = 1
        delta_x, delta_y = directions_dict[direction]
        # forwards
        can_go_forward = True
        i = 1
        while can_go_forward:
            check_coordinates_x = coordinates[0] + i*delta_x
            check_coordinates_y = coordinates[1] + i*delta_y
            if 0 <= check_coordinates_x < len(grid) and 0 <= check_coordinates_y < len(grid[coordinates[1]]):
                if grid[check_coordinates_y][check_coordinates_x] == color:
                    i += 1
                    stones_in_a_row += 1
                    five_in_a_row_coords.append((check_coordinates_x, check_coordinates_y))
                else:
                    can_go_forward = False
            else:
                can_go_forward = False
        can_go_backward = True
        i = 1
        while can_go_backward:
            check_coordinates_x = coordinates[0] - i*delta_x
            check_coordinates_y = coordinates[1] - i*delta_y
            if 0 <= check_coordinates_x < len(grid) and 0 <= check_coordinates_y < len(grid[coordinates[1]]):
                if grid[check_coordinates_y][check_coordinates_x] == color:
                    i += 1
                    stones_in_a_row += 1
                    five_in_a_row_coords.append((check_coordinates_x, check_coordinates_y))
                else:
                    can_go_backward = False
            else:
                can_go_backward = False
        if stones_in_a_row >= 5:
            return True, five_in_a_row_coords
    return False, []


# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("GOMOKU")
screen = pygame.display.set_mode((1080, 720))
# fps
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# TEXT FONTS
font_title = pygame.font.SysFont("oldenglishtext", 36)
font_body = pygame.font.SysFont("oldenglishtext", 24)

# TEXT RENDER
display_game_info = font_body.render("Connect five stones in a row to win!", True, WHITE)
display_game_winner = font_title.render("NULL WINS!", True, GREEN)


# VARIABLES
# BOARD
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
board_border_thickness = 20
# BOARD DRAWING
board_object = pygame.Rect(0, 0, 649 + 2 * board_border_thickness, 649 + 2 * board_border_thickness)
board_grid_horizontal = pygame.Rect(0, 0, 649, 1)
board_grid_vertical = pygame.Rect(0, 0, 1, 649)

board_object.center = (screen.get_rect().centerx - 180, screen.get_rect().centery)
board_grid_horizontal.center = board_object.center
board_grid_vertical.center = board_object.center
# GAME STATE
turn = 1        # white = 1, black = 2
mouse_place_coords = (-1, -1)
game_won = False
game_winner = ""
# misc
stones = []             # list of stone objects on board
red_rects = []          # list of RedRects on board
fiar_on_board = False         # whether there's a 5 in a row (fiar)
fiar_coords = []                 # what the coords of the 5 in a row are(fiar)
loser_appear = False        # image of loser that only appears if you lose to 6 in a row

# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # DETECTS MOUSE PRESS
        if event.type == pygame.MOUSEBUTTONDOWN:
            # only allows placing pieces if game isn't won
            if not game_won:
                # DETECTING MOUSE POS
                # j, i = x, y
                for i in range(19):
                    for j in range(19):
                        board_coords = ((board_object.x + board_border_thickness + (36 * j)),
                                        (board_object.y + board_border_thickness + (36 * i)))
                        if math.dist(pygame.mouse.get_pos(), board_coords) < 15:  # if mouse is within 15 pixels
                            mouse_place_coords = (j, i)     # in board coords

                # PLACING THE PIECE
                # if that board coord is empty AND if the mouse coord is actually on the board
                if board_state[mouse_place_coords[1]][mouse_place_coords[0]] == 0 and not mouse_place_coords == (-1, -1):
                    # update board
                    board_state[mouse_place_coords[1]][mouse_place_coords[0]] = turn
                    stones.append(Stone(mouse_place_coords, turn))
                    fiar_on_board, fiar_coords = check_5_in_a_row(board_state, mouse_place_coords)
                    if fiar_on_board:
                        game_won = True
                        for fiar_square in fiar_coords:
                            red_rects.append(RedRect(fiar_square))
                        if turn == 1:
                            game_winner = "white"
                        elif turn == -1:
                            game_winner = "black"
                    if len(fiar_coords) > 5:
                        loser_appear = True
                    turn *= -1


    # --- BLIT ----
    screen.fill(BLACK)
    # DRAWING THE BOARD
    pygame.draw.rect(screen, pygame.Color("#ffd4a3"), board_object)
    # horizontal lines
    for i in range(19):
        # x coordinate is center of board
        # y coordinate is the top of the board + 20 (extra space around board) and 36i for the separation vertically
        board_grid_horizontal.center = (board_object.center[1], (board_object.top + board_border_thickness + 36 * i))
        pygame.draw.rect(screen, pygame.Color("#000000"), board_grid_horizontal)
    # vertical lines
    for i in range(19):
        # same thing as before, just vertical
        board_grid_vertical.center = ((board_object.left + board_border_thickness + 36 * i), board_object.center[1])
        pygame.draw.rect(screen, pygame.Color("#000000"), board_grid_vertical)
    # DRAWING THE STONES
    for stone in stones:
        screen.blit(stone.image, conv_coords(stone, board_object, board_border_thickness, 36))
    # DRAWING THE RED RECTANGLES
    for red_rect in red_rects:
        screen.blit(red_rect.image, conv_coords(red_rect, board_object, board_border_thickness, 36))

    # TEXT
    display_game_info_center = display_game_info.get_rect(center=(screen.get_rect().width - 188, screen.get_rect().centery - 300))
    screen.blit(display_game_info, display_game_info_center)

    if game_won:
        display_game_winner = font_title.render(f"{game_winner.upper()} WINS!", True, GREEN)
        display_game_winner_center = display_game_winner.get_rect(center=(screen.get_rect().width - 188, screen.get_rect().centery))
        screen.blit(display_game_winner, display_game_winner_center)

        if loser_appear:
            loser = pygame.image.load("images/loser.png")
            loser = pygame.transform.scale(loser, (240, 240))
            loser_center = loser.get_rect(center=(screen.get_rect().width - 188, screen.get_rect().centery + 160))
            screen.blit(loser, loser_center)

    pygame.display.update()
    clock.tick(60)
