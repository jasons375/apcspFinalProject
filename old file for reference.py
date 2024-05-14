import random

import pygame
import time
from fox import Fox
from coin import Coin
from bomb import Bomb

# import high score
f = open("high score", "r")
high_score = f.readline()
f.close()

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.display.set_caption("Coin Collector")
screen = pygame.display.set_mode((720, 600), pygame.RESIZABLE)
# fps
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# TEXT FONTS
font_reg = pygame.font.SysFont("tahoma", 15)
font_cool = pygame.font.SysFont("oldenglishtext", 24)
font_title = pygame.font.SysFont("oldenglishtext", 72)

# TEXT RENDER
display_title_screen1 = font_cool.render("Use WASD and the arrow keys to move.", True, BLACK)
display_title_screen2 = font_cool.render("You have 10 seconds to collect as many coins as you can.", True, BLACK)
display_title_screen3 = font_cool.render("Click anywhere to begin!!", True, BLACK)
display_info = font_reg.render("Collect coins as fast as you can!", True, BLACK)
display_score = font_reg.render("Score: 0", True, BLACK)
display_timer = font_reg.render("Time Remaining : 10s", True, BLACK)
display_high_score = font_reg.render(f"High Score: {high_score}", True, BLACK)

# end display
display_end_msg = font_title.render("OUT OF TIME!", True, BLACK)
display_end_high_score = font_reg.render("High Score:", True, BLACK)

# variables
orange_fox = Fox(0, 0, "orange")
gray_fox = Fox(0, 0, "gray")
coin = Coin(999, 999, "normal")
red_coin = Coin(999, 999, "red")
bomb = Bomb(999, 999)
orange_fox.rand_reposition(screen.get_rect())  # ditto
gray_fox.rand_reposition(screen.get_rect())
coin.rand_reposition(screen.get_rect())  # randomly places coin bc im too lazy to put that in the initialization
bomb.rand_reposition(screen.get_rect())  # ditto 2
score = 0
red_coin_dice = 0
red_coin_timer = 0
game_started = False
game_ended = False
start_time = time.time()

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if (event.type == pygame.MOUSEBUTTONUP) and not game_started:  # starts game
            game_started = True
            start_time = time.time()

    if game_started:
        if (time.time() - start_time) > 10:  # ends game
            game_ended = True

    # game rendering
    screen.fill((70, 130, 180))

    if not game_started:
        title_screen1_center = display_title_screen1.get_rect(center=screen.get_rect().center)
        title_screen2_center = display_title_screen2.get_rect(center=screen.get_rect().center)
        title_screen3_center = display_title_screen3.get_rect(center=screen.get_rect().center)

        screen.blit(display_title_screen1, (title_screen1_center[0], screen.get_rect().center[1] - 70))
        screen.blit(display_title_screen2, (title_screen2_center[0], screen.get_rect().center[1] - 40))
        screen.blit(display_title_screen3, (title_screen3_center[0], screen.get_rect().center[1] + 60))

    # after user starts game this runs
    if game_started and (not game_ended):
        # keyboard input
        key_inputs = pygame.key.get_pressed()
        # orange fox
        if key_inputs[pygame.K_w]:
            orange_fox.move_direction("up")
        if key_inputs[pygame.K_a]:
            orange_fox.move_direction("left")
        if key_inputs[pygame.K_s]:
            orange_fox.move_direction("down")
        if key_inputs[pygame.K_d]:
            orange_fox.move_direction("right")
        # gray fox
        if key_inputs[pygame.K_UP]:
            gray_fox.move_direction("up")
        if key_inputs[pygame.K_LEFT]:
            gray_fox.move_direction("left")
        if key_inputs[pygame.K_DOWN]:
            gray_fox.move_direction("down")
        if key_inputs[pygame.K_RIGHT]:
            gray_fox.move_direction("right")

        # prevent sprite from going off screen
        # credit to https://gamedev.stackexchange.com/questions/187535/how-can-i-create-a-boundary-so-the-sprites-dont-go-off-screen
        # for making the code fit in 2 lines
        orange_fox.x = min(max((0, orange_fox.x)), (screen.get_rect().width - orange_fox.rect.width))
        orange_fox.y = min(max((0, orange_fox.y)), (screen.get_rect().height - orange_fox.rect.height))
        orange_fox.rect = pygame.Rect(orange_fox.x, orange_fox.y, orange_fox.image_size[0], orange_fox.image_size[1])

        gray_fox.x = min(max((0, gray_fox.x)), (screen.get_rect().width - gray_fox.rect.width))
        gray_fox.y = min(max((0, gray_fox.y)), (screen.get_rect().height - gray_fox.rect.height))
        gray_fox.rect = pygame.Rect(gray_fox.x, gray_fox.y, gray_fox.image_size[0], gray_fox.image_size[1])

        # scoring
        # COIN
        if orange_fox.rect.colliderect(coin.rect) or gray_fox.rect.colliderect(coin.rect):
            coin.rand_reposition(screen.get_rect())
            score += 10
        display_score = font_reg.render(f"Score: {score}", True, BLACK)
        # RED COIN
        red_coin_dice = random.randint(0, 240)
        if (red_coin_dice == 0) and ((red_coin.x, red_coin.y) == (999, 999)):
            red_coin_timer = time.time()
            red_coin.rand_reposition(screen.get_rect())
        if orange_fox.rect.colliderect(red_coin.rect) or gray_fox.rect.colliderect(red_coin.rect):
            score *= 2
            red_coin.move(999, 999)
        elif (time.time() - red_coin_timer) > 2:
            red_coin.move(999, 999)
        # BOMB
        if orange_fox.rect.colliderect(bomb.rect) or gray_fox.rect.colliderect(bomb.rect):
            bomb.rand_reposition(screen.get_rect())
            score -= 30

        # timer
        display_timer = font_reg.render(f"Time Remaining : {round((10 - (time.time() - start_time)), 3)}s", True, BLACK)

        # top left ui
        screen.blit(display_info, (6, 6))
        screen.blit(display_score, (6, display_info.get_rect().bottom + 6))
        screen.blit(display_timer, (6, display_score.get_rect().bottom + display_info.get_rect().bottom + 6))

        # top right ui
        screen.blit(display_high_score, (screen.get_width() - display_high_score.get_width() - 6, 6))

        # sprites
        screen.blit(orange_fox.image, (orange_fox.x, orange_fox.y))
        screen.blit(gray_fox.image, (gray_fox.x, gray_fox.y))
        screen.blit(coin.image, (coin.x, coin.y))
        screen.blit(red_coin.image, (red_coin.x, red_coin.y))
        screen.blit(bomb.image, (bomb.x, bomb.y))

    if game_ended:
        # high score logic
        if high_score == "N/A":
            high_score = score
        elif score > float(high_score):
            high_score = score
        display_end_high_score = font_reg.render(f"High Score: {high_score}", True, BLACK)

        f = open("high score", "w")
        f.write(str(high_score))
        f.close()

        end_msg_center = display_end_msg.get_rect(center=screen.get_rect().center)
        end_high_score = display_end_high_score.get_rect(center=screen.get_rect().center)

        screen.blit(display_end_msg, (end_msg_center[0], end_msg_center[1] - 30))
        screen.blit(display_end_high_score, (end_high_score[0], end_high_score[1] + 30))

    pygame.display.update()

    clock.tick(60)
