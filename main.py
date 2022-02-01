import pygame
import utility as util

# for displaying life we need text
pygame.font.init()

# width, height = 900, 500
WINDOW = pygame.display.set_mode((util.width, util.height))
pygame.display.set_caption("Atlantic Wars Game")

# Creating user event so that we can came to know if the bullet collides, different number indicating different events
BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def drawWindow(red, blue, red_bullets, blue_bullets, red_life, blue_life,
               BLUE_PLAYER, RED_PLAYER, SPACE, BORDER):
    """
    This function displays the graphics of the Game which including the weapons, background-image, bullets, and life of players
    with 60 Frames per second.
    """
    # RECOGNISING THE ORDER IN WHICH TO DRAW THINGS
    WINDOW.blit(SPACE, (0, 0))

    # Adding border created above
    pygame.draw.rect(WINDOW, (0, 255, 0), BORDER)

    # Indicating life
    LIFE_FONT = pygame.font.SysFont('comicsans', 40)

    # Displaying Health by font
    red_life_text = LIFE_FONT.render("Life: " + str(red_life), True, (255, 0, 0))
    blue_life_text = LIFE_FONT.render("Life: " + str(blue_life), True, (0, 0, 255))
    WINDOW.blit(red_life_text, (util.width - red_life_text.get_width() - 10, 10))
    WINDOW.blit(blue_life_text, (10, 10))

    # using blit to load surfaces
    WINDOW.blit(BLUE_PLAYER, (blue.x, blue.y))

    WINDOW.blit(RED_PLAYER, (red.x, red.y))

    # Drawing bullets
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, (255, 0, 0), bullet)

    for bullet in blue_bullets:
        pygame.draw.rect(WINDOW, (0, 0, 255), bullet)

    pygame.display.update()

def handle_bullets(blue_bullets, red_bullets, blue, red):

    BULLET_VELOCITY = 7            # Bullet velocity

    # To check weather the bullet hit red or blue player or they fly through the skin
    for bullet in blue_bullets:
        bullet.x += BULLET_VELOCITY

        # colliddirect only works if both are rectangle
        if red.colliderect(bullet):
            # Now we are going to post a event then check in the main function for the event
            # it will indicate us that the bullet hit the player
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x > util.width:
            blue_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY

        # colliddirect only works if both are rectangle
        if blue.colliderect(bullet):
            # Posting a event then checking in the main function for the event
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    """
    Making everything work together.
    """
    # Loading Assets
    BLUE_PLAYER, RED_PLAYER, SPACE, BORDER = util.load_assests()

    # Making two rectangles so that we can control where our player are moving
    PLAYER_WIDTH, PLAYER_HEIGHT = (50, 40)
    red = pygame.Rect(700, 250, PLAYER_WIDTH, PLAYER_HEIGHT)
    blue = pygame.Rect(100, 250, PLAYER_WIDTH, PLAYER_HEIGHT)

    # To making our game refresh at a constant interval
    clock = pygame.time.Clock()

    # To storing our bullet location in pixels so that we can move it
    blue_bullets = []
    red_bullets = []

    # Healths of our players
    red_life = 10
    blue_life = 10

    run = True

    while run:
        # Capped frame rate so it remains consistent on different computers
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # checking if key pressed for firing bullet
            if event.type == pygame.KEYDOWN:

                # maximum amount of bullets a player can shoot at a time
                MAX_BULLETS = 4
                # CHECKING if we press LCTRL and we have 3 bullets at a time on a screen
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS:
                    # 10, 5 width, height of bullet and others are location
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height // 2 - 2, 10, 5)
                    blue_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            # If bullets hit red player then decrease life
            if event.type == RED_HIT:
                red_life -= 1
            # If bullets hit blue player then decrease life
            if event.type == BLUE_HIT:
                blue_life -= 1

        winner_text = ""
        if red_life <= 0:
            winner_text = "Winner : Player Blue!!"
        if blue_life <= 0:
            winner_text = "Winner : Player Red!!"
        if winner_text != "":
            util.winner(winner_text, WINDOW)
            break

        # Checking which keys are pressed while the game is running it also checks if the
        # keys are pressed and remain down
        keys_pressed = pygame.key.get_pressed()
        # Spaceship velocity
        VELOCITY = 7
        # Function that handle key movements of blue and red player and bullets
        util.blue_handle_movement(keys_pressed, blue, VELOCITY, BORDER)
        util.red_handle_movement(keys_pressed, red, VELOCITY, BORDER)

        handle_bullets(blue_bullets, red_bullets, blue, red)

        # Displaying everything on the screen.
        drawWindow(red, blue, red_bullets, blue_bullets, red_life, blue_life,
                   BLUE_PLAYER, RED_PLAYER, SPACE, BORDER)

    main()


if __name__ == "__main__":
    main()
