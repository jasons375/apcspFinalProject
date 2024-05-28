import pygame
import math
import random
import time
from apple import Apple
from bomb import Bomb

# import high score
f = open("high score", "r")
high_score = f.readline()
f.close()


# set up pygame modules
pygame.init()
pygame.font.init()
pygame.font.get_fonts()
pygame.display.set_caption("Shoot the Fruit!")
screen = pygame.display.set_mode((720, 600), pygame.RESIZABLE)
# fps
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# TEXT FONTS
font_reg = pygame.font.SysFont("tahoma", 15)
font_title = pygame.font.SysFont("oldenglishtext", 80)


# TEXT RENDER
display_message = font_reg.render("Click the fruit to score!", True, BLACK)
display_score = font_reg.render("Score: 0", True, BLACK)
display_high_score = font_reg.render(f"High Score: {high_score}", True, BLACK)
display_clock = font_reg.render("", True, BLACK)
display_win_msg = font_title.render("YOU WIN!", True, BLACK)
display_lose_msg = font_title.render("GAME OVER!", True, BLACK)
display_time = font_reg.render("Time: ", True, BLACK)
display_play_again = font_reg.render("Press SPACE to play again.", True, BLACK)

# variables
apple = Apple(60, 60)
bomb = Bomb(240, 240)
score = 0
win_score = 10
start_time = time.time()
time_elapsed = 0
bomb_time = 0

# game state variables
lose = False
win = False

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # lmb
        if event.type == pygame.MOUSEBUTTONUP:
            # checks if you clicked on apple
            if apple.rect.collidepoint(event.pos):
                # makes sure apple doesn't collide with screen border
                apple_rand_x = random.randint(0, (screen.get_width() - apple.image_size[0]))
                apple_rand_y = random.randint(0, (screen.get_height() - apple.image_size[1]))
                apple.move(apple_rand_x, apple_rand_y)
                # update clicks
                score += 1
            elif bomb.rect.collidepoint(event.pos):
                lose = True
            else:
                score -= 1
            display_score = font_reg.render(f"Score: {score}", True, BLACK)

        # space bar
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            lose = win = False
            apple = Apple(60, 60)
            bomb = Bomb(240, 240)
            score = time_elapsed = 0
            display_score = font_reg.render(f"Score: {score}", True, BLACK)
            display_clock = font_reg.render(f"Time: {time_elapsed}s", True, BLACK)
            start_time = time.time()
            bomb_time = 0

    # game state update
    if score >= win_score:
        win = True
    elif score < 0:
        lose = True

    # time calculations & update
    if not (lose or win):
        time_elapsed = round((time.time() - start_time), 3)
        display_clock = font_reg.render(f"Time: {time_elapsed}s", True, BLACK)

    # bomb logic to make it relocate every second
    if bomb_time != math.floor(time_elapsed):
        bomb_time = math.floor(time_elapsed)
        # makes sure bomb doesn't collide with screen border
        bomb_rand_x = random.randint(0, (screen.get_width() - bomb.image_size[0]))
        bomb_rand_y = random.randint(0, (screen.get_height() - bomb.image_size[1]))
        bomb.move(bomb_rand_x, bomb_rand_y)

    # rendering
    screen.fill((167, 199, 231))

    if not (lose or win):
        # GAME
        screen.blit(apple.image, (apple.x, apple.y))
        screen.blit(bomb.image, (bomb.x, bomb.y))

        # top left ui
        screen.blit(display_message, (6, 6))
        screen.blit(display_score, (6, (display_message.get_height() + 6)))
        screen.blit(display_clock, (6, display_message.get_height() + display_score.get_height() + 6))

        # top right ui
        screen.blit(display_high_score, (screen.get_width() - display_high_score.get_width() - 6, 6))
    else:
        # END SCREEN
        # time
        time_end = time_elapsed
        display_time = font_reg.render(f"Time: {time_end}s", True, BLACK)
        time_center = display_time.get_rect(center=screen.get_rect().center)
        screen.blit(display_time, (time_center[0], time_center[1] + 30))

        # play again
        play_again_center = display_play_again.get_rect(center=screen.get_rect().center)
        screen.blit(display_play_again, (play_again_center[0], screen.get_height() - 36))

        if win:
            win_msg_center = display_win_msg.get_rect(center=screen.get_rect().center)
            screen.blit(display_win_msg, (win_msg_center[0], win_msg_center[1] - 30))

            # high score logic
            if high_score == "N/A":
                high_score = time_end
            elif time_end < float(high_score):
                high_score = time_end
            display_high_score = font_reg.render(f"High Score: {high_score}", True, BLACK)
            f = open("high score", "w")
            f.write(str(high_score))
            f.close()

        elif lose:
            lose_msg_center = display_lose_msg.get_rect(center=screen.get_rect().center)
            screen.blit(display_lose_msg, (lose_msg_center[0], lose_msg_center[1] - 30))

    pygame.display.update()
    clock.tick(60)

