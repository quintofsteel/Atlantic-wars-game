import pygame
import os

width, height = 900, 500


def load_assests():
    # Loading player images into our file known as surfaces as we use this above background
    playerImageBlue = pygame.image.load(os.path.join("Assets", "Blue_Spaceship.png"))
    playerImageRed = pygame.image.load(os.path.join("Assets", "Red_Spaceship.png"))
    SPACE = pygame.image.load(os.path.join("Assets", "space.jpg"))

    # Scaling down the images
    PLAYER_WIDTH, PLAYER_HEIGHT = (50, 40)
    BLUE_PLAYER = pygame.transform.scale(playerImageBlue, (PLAYER_WIDTH, PLAYER_HEIGHT))
    RED_PLAYER = pygame.transform.scale(playerImageRed, (PLAYER_WIDTH, PLAYER_HEIGHT))
    SPACE = pygame.transform.scale(SPACE, (900, 500))

    # Rotating the images
    BLUE_PLAYER = pygame.transform.rotate(BLUE_PLAYER, 90)
    RED_PLAYER = pygame.transform.rotate(RED_PLAYER, -90)

    # Border in the middle of the window
    # starting coordinates then width and height of the border
    BORDER = pygame.Rect(width / 2 - 5, 0, 10, height)

    return BLUE_PLAYER, RED_PLAYER, SPACE, BORDER


def blue_handle_movement(keys_pressed, blue, VELOCITY, BORDER):
    # and checking that it remains in the screen and dont cross the border
    if keys_pressed[pygame.K_a] and blue.x - VELOCITY > 0:  # LEFT
        blue.x -= VELOCITY
    elif keys_pressed[pygame.K_d] and blue.x + VELOCITY + blue.width < BORDER.x:  # RIGHT
        blue.x += VELOCITY
    elif keys_pressed[pygame.K_w] and blue.y - VELOCITY > 0:  # UP
        blue.y -= VELOCITY
    elif keys_pressed[pygame.K_s] and blue.y + VELOCITY + blue.height < height - 15:  # DOWN
        blue.y += VELOCITY


def red_handle_movement(keys_pressed, red, VELOCITY, BORDER):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width + 8:  # LEFT
        red.x -= VELOCITY
    elif keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < width:  # RIGHT
        red.x += VELOCITY
    elif keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:  # UP
        red.y -= VELOCITY
    elif keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < height - 15:  # DOWN
        red.y += VELOCITY


def winner(text, WIN):
    # Font
    FONT = pygame.font.SysFont('comicsans', 100)
    # Displaying the winner font on the screen.
    draw_text = FONT.render(text, 1, (0, 255, 255))
    WIN.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))
    # Updating the display
    pygame.display.update()
    pygame.time.delay(5000)
