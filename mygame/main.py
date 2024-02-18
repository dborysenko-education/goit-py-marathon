import pygame, sys, random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_0
from pygame.locals import *
# -- GAME CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = pygame.time.Clock()
COLOR_PLAYER = (255, 255, 255) # WHITE
COLOR_GAMEFIELD = (0, 0, 0) # BLACK
COLOR_ENEMY = (255, 0, 0) # RED
COLOR_BONUS = (250, 215, 0) # GOLDEN
COLOR_SCORE = (0, 255, 0)
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
ENEMY_WIDTH = 30
ENEMY_HEIGHT = 30
BONUS_WIDTH = 15
BONUS_HEIGHT = 15
CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2
#FONT = pygame.font.SysFont('C:\Windows\Fonts\Arial.ttf', 20)
#FONT = pygame.font.SysFont('Arial', 20)

# -- GAME SETTINGS
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = ((PLAYER_WIDTH, PLAYER_HEIGHT))
player = pygame.Surface(player_size)
player.fill(COLOR_PLAYER)
player_rect = player.get_rect()
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 1000)

# -- GAME FUNCTIONS
# def rand_color(): 
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return [r, g, b]

def create_enemy():
    enemy_size = (ENEMY_WIDTH, ENEMY_HEIGHT)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_ENEMY)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT-ENEMY_HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (BONUS_WIDTH, BONUS_HEIGHT)
    bonus = pygame.Surface(bonus_size)
    # bonus.fill(rand_color())
    bonus.fill(COLOR_BONUS)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH-BONUS_WIDTH), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_move]

# -- GAME PROCESS
pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 20)

playing = True

enemies = []
bonuses = []
score = 0

while playing:  

    FPS.tick(120)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            palying = False
        if event.type == CREATE_ENEMY: 
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS: 
            bonuses.append(create_bonus())

    main_display.fill(COLOR_GAMEFIELD)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT : 
        #print("DOWN")
        player_rect = player_rect.move([0, 1])

    if keys[K_UP] and player_rect.top > 0 : 
        #print("UP")
        player_rect = player_rect.move([0, -1])

    if keys[K_LEFT] and player_rect.left > 0 : 
        #print("LEFT")
        player_rect = player_rect.move([-1, 0])

    if keys[K_RIGHT] and player_rect.right < WIDTH : 
        #print("RIGHT")
        player_rect = player_rect.move([1, 0])
        
    for enemy in enemies: 
        enemy[1] = enemy[1].move(enemy[2]) #enemy_rect
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            print("boom")
            playing = False

    for bonus in bonuses: 
        bonus[1] = bonus[1].move(bonus[2]) #bonus_rect
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            print("bonus")
            bonuses.pop(bonuses.index(bonus))


    main_display.blit(FONT.render(str(score), True, COLOR_SCORE), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies: 
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        
    for bonus in bonuses: 
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
        

    #print(f"ENEMIES:\t{len(enemies)}\nBONUSES:\t{len(bonuses)}")
    
# -- EXIT WHEN PRESSED 0
    if keys[K_0]: 
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        exit()