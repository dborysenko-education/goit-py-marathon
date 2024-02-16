import pygame
import random
from pygame.constants import QUIT

# -- GAME CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = 24
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20


# -- GAME SETTINGS
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = ((PLAYER_WIDTH, PLAYER_HEIGHT))
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()


def rand_speed(min,max): 
    ver = random.randint(min,max)
    hor = random.randint(min,max)
    return [hor,ver]

min = 1
max = 7
player_speed = rand_speed(min,max)

# -- GAME PROCESS
pygame.init()

playing = True

while playing:  
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            palying = False

    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_speed = rand_speed(min,max)
        player_speed[1] = -player_speed[1]
        print("Touched Bottom Border")
        
    if player_rect.right >= WIDTH:
        player_speed = rand_speed(min,max)
        player_speed[0] = -player_speed[0]
        print("Touched Right Border")

    if player_rect.top < 0:
        player_speed = rand_speed(min,max)
        player_speed[1] = -player_speed[1]
        print("Touched Top Border")

    if player_rect.left < 0:
        player_speed = rand_speed(min,max)
        player_speed[0] = -player_speed[0]
        print("Touched Left Border")

    print(player_speed)

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()

