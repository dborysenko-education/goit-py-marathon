import pygame, random
from pygame.constants import QUIT

pygame.init()

HEIGHT = 400
WIDTH = 400

FPS = pygame.time.Clock()

main_display = pygame.display.set_mode((HEIGHT,WIDTH))

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)

player_size = (20,20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]



playing = True

while playing:  
    FPS.tick(120)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            palying = False

    
    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_speed = [1, -1]

    if player_rect.right >= WIDTH:
        player_speed = [-1, -1]

    print(player_rect.bottom)

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()

