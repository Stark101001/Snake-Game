import pygame
import random

pygame.init()

# =======Color Codes======
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# ========Title==========
title = "Snake Game"
pygame.display.set_caption(title)

#============Adding Game Icon=========
gameIcon = pygame.image.load('snake.png')
pygame.display.set_icon(gameIcon)

# =====Creating Display=============
scr_width = 800
scr_height = 600

screen = pygame.display.set_mode((scr_width, scr_height))

# ========Image Load===========
bg_img = pygame.image.load('bg.jpg').convert()

# =======Clock Function =========
FPS = 10

clk = pygame.time.Clock()

# ========Font Import======
font = pygame.font.SysFont("Times new Roman", 34)


def Snake(React, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(screen, red, [XnY[0], XnY[1], React, React])


def End_text(msg, color):
    scr_text = font.render(msg, True, color)
    screen.blit(scr_text, [scr_width - 790, scr_height - 400])


def Loop():
    # ==========Snake Position==========
    start_x = int(scr_width / 2)
    start_y = int(scr_height / 2)

    # ======= Updation into Movement ====
    React = 20

    update_x = 0
    update_y = 0

    # ======= Snake List===========
    snakeList = []
    snakeLength = 1

    # =====Creating Food ============

    rFoodX = round(random.randrange(0, scr_width - React) / 20) * 20
    rFoodY = round(random.randrange(0, scr_height - React) / 20) * 20
    # =====Event Handling===========
    Game_quit = False
    Game_over = False

    while not Game_quit:
        while Game_over == True:
            screen.fill(black)
            End_text("Game Over Press\n 'Space' To Retry Press\n 'Esc' To Quit", white)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Call Quit Event
                    Game_quit = True  # Quit game
                    Game_over = False   # Game End
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Game_quit = True
                        Game_over = False

                    if event.key == pygame.K_SPACE:
                        Loop()

        for event in pygame.event.get():  # import All Event By Get method
            if event.type == pygame.QUIT:  # Call Quit Event
                Game_quit = True  # Quit game
            # Event Handling =======================
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    update_x = -React
                    update_y = 0

                if event.key == pygame.K_RIGHT:
                    update_x = +React
                    update_y = 0

                if event.key == pygame.K_UP:
                    update_y = -React
                    update_x = 0

                if event.key == pygame.K_DOWN:
                    update_y = +React
                    update_x = 0
            # If Snake Touch Boundary Then game is over Logic ==========
        if start_x >= scr_width or start_x < 0 or start_y >= scr_height or start_y < 0:
            Game_over = True

        start_y += update_y
        start_x += update_x

        screen.blit(bg_img, [0, 0])  # image load method
        pygame.draw.rect(screen, blue, [rFoodX, rFoodY, React, React])  # draw rectangle as Snake Food
        pygame.draw.rect(screen, black, [0, 0, scr_width, scr_height], 10)  # draw rectangle as boundary

        snakHead = [start_x, start_y]
        snakeList.append(snakHead)
        if len(snakeList) > snakeLength:
            del (snakeList[0])

        for eachsegment in snakeList[:-1]:
            if eachsegment == snakHead:
                # Game_over = True
                pass

        Snake(React, snakeList)  # Calling Snake Function

        pygame.display.update()

        if start_x == rFoodX and start_y == rFoodY:  # Conditiion Apply Snake Hover to Food
            rFoodX = round(random.randrange(0, scr_width - React) / 20) * 20  # Snake food Position Correct
            rFoodY = round(random.randrange(0, scr_height - React) / 20) * 20  # Snake food Position Correct

            snakeLength += 1  # Increase Snake Length

        clk.tick(FPS)  # Snake movement Frame Per Seconds (FPS)


Loop()
