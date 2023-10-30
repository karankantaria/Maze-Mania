import pygame 
import os
import math
from handle_enemy import enemy, enemy_collision, Node

pygame.init()
# WINDOW_WIDTH = 704
# WINDOW_HEIGHT = 320
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
#16:9^
WINDOW=pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
BLACK=(0,0,0)
WIN_EDGE = pygame.Rect(WINDOW_WIDTH//2 - 5, 0, 10, WINDOW_HEIGHT)
pygame.display.set_caption("TCA2")

BACKGROUND_TEST = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Grass_Sample.png')), (WINDOW_WIDTH, WINDOW_HEIGHT))

PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'test_sprite.png'))
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 30
PLAYER_COMP = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)#rotate redundant for now

MAZE_WALL=pygame.image.load(os.path.join('Assets', 'maze_wall_test.png'))

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'monster2_test.png'))
ENEMY_WIDTH = 15
ENEMY_HEIGHT = 30
ENEMY_COMP = pygame.transform.rotate(pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT)), 0)

#Creating a class for player the main character
class Player(pygame.sprite.Sprite):
  
  def __init__(self,width, height, speed, max_health,player_image,x,y,health=100):
    #self.rect = pygame.Rect(2, 2, width, height) # linking pygame
    self.image=player_image
    self.speed = speed # Creating the variable 
    self.max_health = max_health
    self.health=health

    self.rect=self.image.get_rect()
    self.rect.width = width
    self.rect.height = height
    self.rect.x=x
    self.rect.y=y

    pygame.sprite.Sprite.__init__(self)
    WINDOW = pygame.display.get_surface()

def movement(entity,key_press):
    player=entity
    if move[pygame.K_a]:
        player.move_ip(-1,0) 
    elif move[pygame.K_d]:
        player.move_ip(1,0) 
    elif move[pygame.K_w]:
        player.move_ip(0,-1)
    elif move[pygame.K_s]:
        player.move_ip(0,1)


def draw_maze(level):
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == "x":
                WALL_X = x * TILE_SIZE
                WALL_Y = y * TILE_SIZE
                WINDOW.blit(MAZE_WALL, (WALL_X, WALL_Y))




#Loading level
def load_level():
    pass

#for enemy collision and for trap collision
def check_collision():
    pass

#For player animation
def player_animation():
    pass

#For enemy animation
def enemy_animation():
    pass

def draw_lives(entity):
    #display_surface = pygame.display.set_mode((X, Y))#
    health=str(entity.health)
    #print(health)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(health, True, black)
    textRect = text.get_rect()
    textRect.center = (100,500)
    WINDOW.blit(text, textRect)


#Could be done in check_collision and creating a coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((1,1)) # Changing the size of the coin 
        self.image.fill((215, 185, 0)) # Need to find the right colour for coin
        self.rect = self.image.get.rect() 
        self.rect.center = (x, y)
    
        #Create to a group to hold all the coin for Player
        coins_group = pygame.sprite.Group()


black = (0, 0, 0)
white = (255, 255, 255)

level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x  S        xx                  x      x",
    "x           xx         P        x      x",
    "x    xx                     x   x  xx  x", 
    "x               xxxxxxx  x  x      xx  x", 
    "x           x   xxxxxxx  x  x      xx  x",
    "x  xxxxxx   x       xxx  x  xxxx   xx  x",
    "x    xxx    x       xxx  x  xx     xx  x",
    "x    xxx    xxxxxxxxxxx  x  xx     xx  x",
    "xxx  xxx            xxx  x  xxxxxxxxxxxx",
    "xxx  xxx            xxx  x             x",
    "xxx  xxx  xxxxxxxx  xxx  x             x",
    "xxx  xxx            xxx  xxxxxxxxxxxxxxx",
    "x    xxx            xxx         E      x",
    "x   xxxxxxxxxxxxxxxxxx                 x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",




]


level_1_no_obstacle = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x           xx                  x      x",
    "x           xx                  x      x",
    "x    xx                     x   x  xx  x", 
    "x               xxxxxxx  x  x      xx  x", 
    "x           x   xxxxxxx  x  x      xx  x",
    "x  xxxxxx   x       xxx  x  xxxx   xx  x",
    "x    xxx    x       xxx  x  xx     xx  x",
    "x    xxx    xxxxxxxxxxx  x  xx     xx  x",
    "xxx  xxx            xxx  x  xxxxxxxxxxxx",
    "xxx  xxx            xxx  x             x",
    "xxx  xxx  xxxxxxxx  xxx  x             x",
    "xxx  xxx            xxx  xxxxxxxxxxxxxxx",
    "x    xxx            xxx                x",
    "x   xxxxxxxxxxxxxxxxxx                 x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",




]

TILE_SIZE = 24


loop=True
#Make player start at S
for y, row in enumerate(level_1):
    for x, char in enumerate(row):
        if char == "S":
            player_x, player_y = x * TILE_SIZE, y * TILE_SIZE
        elif char == "P":
            enemy_x, enemy_y = x * TILE_SIZE, y * TILE_SIZE

player_init = Player(PLAYER_WIDTH, PLAYER_HEIGHT, 100,50,PLAYER_IMAGE,player_x,player_y) #Creating a player as a object
enemy_init = enemy(ENEMY_WIDTH,ENEMY_HEIGHT,ENEMY_IMAGE,enemy_x,enemy_y,level_1_no_obstacle)

maze_walls = []  #For collisions with player
for y, row in enumerate(level_1):
    for x, cell in enumerate(row):
        if cell == "x":
            wall_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            maze_walls.append(wall_rect)


while loop:

    old_player_x = player_init.rect.x
    old_player_y = player_init.rect.y
    old_enemy_x = enemy_init.rect.x
    old_enemy_y = enemy_init.rect.y 
    WINDOW.fill(BLACK)
    #WINDOW.fill((0,0,0))
    # pygame.draw.rect(WINDOW,(50,50,50),Player)
    WINDOW.blit(BACKGROUND_TEST, (0, 0))
    #pygame.draw.rect(WINDOW, BLACK, WIN_EDGE)
    #pygame.draw.rect(WINDOW, (255, 0, 0), player_init.rect)
    WINDOW.blit(PLAYER_COMP, (player_init.rect.x, player_init.rect.y))
    WINDOW.blit(ENEMY_COMP, (enemy_init.rect.x, enemy_init.rect.y))
    #WINDOW.fill(black) 
      
    draw_maze(level_1) 
    move=pygame.key.get_pressed()
    if move:
        movement(player_init.rect,move)

    for wall_rect in maze_walls:
        if player_init.rect.colliderect(wall_rect):
            player_init.rect.x = old_player_x
            player_init.rect.y = old_player_y
    enemy_collision(player_init.rect,enemy_init.rect,player_init)
    enemy_init.enemy_to_player(player_init.rect, maze_walls)
    draw_lives(player_init)
    if level_1[int(player_init.rect.y / TILE_SIZE)][int(player_init.rect.x / TILE_SIZE)] == 'E':
        print("Congratulations! You reached the exit!")
    print("Player Position:", player_init.rect.x, player_init.rect.y)
    print("Enemy Position:", enemy_init.rect.x, enemy_init.rect.y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
    
            
    pygame.display.update()

    




pygame.quit()
