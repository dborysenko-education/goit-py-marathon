import pygame, sys, random, os
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_0
from pygame.locals import *
# -- GAME CONSTANTS

WIDTH = 800
HEIGHT = 600
FPS = pygame.time.Clock()
COLOR_PLAYER = (0, 0, 0) # BLACK
COLOR_GAMEFIELD = (0, 0, 0) # BLACK
COLOR_ENEMY = (255, 0, 0) # RED
COLOR_BONUS = (250, 215, 0) # GOLDEN
COLOR_SCORE = (0, 255, 0)
CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2
CHANGE_IMAGE = pygame.USEREVENT + 3
RATE_ENEMY = 1500
RATE_BONUS = 1000
RATE_ANIMATION = 200
GAME_SPEED = 60

# -- GAME SETTINGS
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

ANIMATED_PLAYER_PATH = "C:\\python\\goit\\goit-py-marathon\\mygame\\assets\\animated_goose"
ANIMATED_PLAYER_IMAGES = os.listdir(ANIMATED_PLAYER_PATH)
PLAYER_IMG = pygame.image.load('C:\python\goit\goit-py-marathon\mygame\\assets\\player.png').convert_alpha()
ENEMY_IMG = pygame.image.load('C:\python\goit\goit-py-marathon\mygame\\assets\\enemy.png').convert_alpha()
BONUS_IMG = pygame.image.load('C:\python\goit\goit-py-marathon\mygame\\assets\\bonus.png').convert_alpha()
PLAYER_WIDTH = PLAYER_IMG.get_width()
PLAYER_HEIGHT = PLAYER_IMG.get_height()
ENEMY_WIDTH = ENEMY_IMG.get_width()
ENEMY_HEIGHT = ENEMY_IMG.get_height()
BONUS_WIDTH = BONUS_IMG.get_width()
BONUS_HEIGHT = BONUS_IMG.get_height()
player = PLAYER_IMG
player_rect = pygame.Rect(0, 300, PLAYER_HEIGHT, PLAYER_WIDTH)

pygame.time.set_timer(CREATE_ENEMY, RATE_ENEMY)
pygame.time.set_timer(CREATE_BONUS, RATE_BONUS)
pygame.time.set_timer(CHANGE_IMAGE, RATE_ANIMATION)

bg = pygame.transform.scale(pygame.image.load('C:\python\goit\goit-py-marathon\mygame\\assets\\background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

def create_enemy():
    enemy_size = (ENEMY_WIDTH, ENEMY_HEIGHT)
    enemy = ENEMY_IMG
    enemy_rect = pygame.Rect(WIDTH, random.randint(150, HEIGHT-ENEMY_HEIGHT-150), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (BONUS_WIDTH, BONUS_HEIGHT)
    bonus = BONUS_IMG
    bonus_rect = pygame.Rect(random.randint(150, WIDTH-BONUS_WIDTH-150), 0, *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

# -- GAME PROCESS
pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20)

playing = True

enemies = []
bonuses = []
score = 0
image_index = 0

while playing:  

    FPS.tick(GAME_SPEED)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            palying = False
        if event.type == CREATE_ENEMY: 
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS: 
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE: 
            player = pygame.image.load(os.path.join(ANIMATED_PLAYER_PATH, ANIMATED_PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(ANIMATED_PLAYER_IMAGES): 
                image_index = 0
            
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width(): 
        bg_X1 = bg.get_width()
    if bg_X2 < -bg.get_width(): 
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))
    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT : 
        player_rect = player_rect.move([0, 4])

    if keys[K_UP] and player_rect.top > 0 : 
        player_rect = player_rect.move([0, -4])

    if keys[K_LEFT] and player_rect.left > 0 : 
        player_rect = player_rect.move([-4, 0])

    if keys[K_RIGHT] and player_rect.right < WIDTH : 
        player_rect = player_rect.move([4, 0])
        
    for enemy in enemies: 
        enemy[1] = enemy[1].move(enemy[2]) #enemy_rect
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            print("GAME OVER!")
            playing = False

    for bonus in bonuses: 
        bonus[1] = bonus[1].move(bonus[2]) #bonus_rect
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            score += 1


    main_display.blit(FONT.render(str(score), True, COLOR_SCORE), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies: 
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        
    for bonus in bonuses: 
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
  
# -- EXIT WHEN PRESSED 0
    if keys[K_0]: 
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        exit()