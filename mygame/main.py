import pygame, sys
from pygame.constants import QUIT

# -- GAME CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = pygame.time.Clock()
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
LIMIT = 0

# -- GAME SETTINGS
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = ((PLAYER_WIDTH, PLAYER_HEIGHT))
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [3, 2]

# -- GAME PROCESS
pygame.init()

playing = True


while playing:  

    FPS.tick(120)
    if LIMIT != 5: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                palying = False

        main_display.fill(COLOR_BLACK)

        if player_rect.bottom >= HEIGHT:
            player_speed[1] = -player_speed[1]
            touches += 1
        if player_rect.right >= WIDTH:
            player_speed[0] = -player_speed[0]
            touches += 1
        if player_rect.top < 0:
            player_speed[1] = -player_speed[1]
            touches += 1
        if player_rect.left < 0:
            player_speed[0] = -player_speed[0]
            touches += 1
        #print(player_rect.bottom)

        main_display.blit(player, player_rect)

        player_rect = player_rect.move(player_speed)

        pygame.display.flip()
        print("Touches:",touches)
    else: 
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        exit()
        


