import pygame, random
from pygame.constants import QUIT

pygame.init()

HEIGHT = 400
WIDTH = 400

main_display = pygame.display.set_mode((HEIGHT,WIDTH))

COLOR_WHITE = (255,255,255)
PLAYER_SIZE = (20,20)

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

playing = True

while playing: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            palying = False

    main_display.blit(player, player_rect)

    pygame.display.flip()
