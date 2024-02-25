import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 15
GOAL_WIDTH, GOAL_HEIGHT = 20, 150
PLAYER_SPEED = 5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALE_GREEN = (152, 251, 152)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("super fun pong pong pong")
clock = pygame.time.Clock()


player1_x = WIDTH - GOAL_WIDTH - 20
player1_y = (HEIGHT - GOAL_HEIGHT) // 2
player2_x = 20
player2_y = (HEIGHT - GOAL_HEIGHT) // 2
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5


score_red = 0
score_blue = 0


font = pygame.font.Font(None, 36)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP] and player1_y > 0:
        player1_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player1_y < HEIGHT - GOAL_HEIGHT:
        player1_y += PLAYER_SPEED


    if keys[pygame.K_w] and player2_y > 0:
        player2_y -= PLAYER_SPEED
    if keys[pygame.K_s] and player2_y < HEIGHT - GOAL_HEIGHT:
        player2_y += PLAYER_SPEED


    ball_x += ball_speed_x
    ball_y += ball_speed_y

 
    if ball_x - BALL_RADIUS < 0:
        # Ball hits the left wall, Red team scores
        score_red += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
    elif ball_x + BALL_RADIUS > WIDTH:
        # Ball hits the right wall, Blue team scores
        score_blue += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -ball_speed_x


    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y = -ball_speed_y


    if (
        player1_x < ball_x < player1_x + GOAL_WIDTH
        and player1_y < ball_y < player1_y + GOAL_HEIGHT
    ):
        ball_speed_x = -ball_speed_x

    # Ball collision with player 2 goal
    if (
        player2_x < ball_x < player2_x + GOAL_WIDTH
        and player2_y < ball_y < player2_y + GOAL_HEIGHT
    ):
        ball_speed_x = -ball_speed_x

    screen.fill(PALE_GREEN)
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 2)
    pygame.draw.rect(screen, RED, (player1_x, player1_y, GOAL_WIDTH, GOAL_HEIGHT))
    pygame.draw.rect(screen, BLUE, (player2_x, player2_y, GOAL_WIDTH, GOAL_HEIGHT))
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), BALL_RADIUS)


    score_text = font.render(f"Red: {score_red}   Blue: {score_blue}", True, BLACK)
    screen.blit(score_text, (10, 10))


    reset_button = pygame.draw.rect(screen, RED, (WIDTH - 90, 10, 80, 30))
    reset_text = font.render("Reset", True, WHITE)
    screen.blit(reset_text, (WIDTH - 80, 15))


    mouse_pos = pygame.mouse.get_pos()
    if reset_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            score_red = 0
            score_blue = 0
            

    pygame.display.flip()


    clock.tick(FPS)