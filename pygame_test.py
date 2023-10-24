import pygame 
import os

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
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60
PLAYER_COMP = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)#rotate redundant for now

MAZE_WALL=pygame.image.load(os.path.join('Assets', 'maze_wall_test.png'))

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'monster_test.png'))
ENEMY_WIDTH = 20
ENEMY_HEIGHT = 20
ENEMY_COMP = pygame.transform.rotate(pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT)), 0)

#Creating a class for player the main character
class Player(pygame.sprite.Sprite):
  
  def __init__(self,width, height, speed, max_health,player_image,x,y):
    #self.rect = pygame.Rect(2, 2, width, height) # linking pygame
    self.image=player_image
    self.rect=self.image.get_rect()
    self.speed = speed # Creating the variable 
    self.max_health = max_health
    self.rect.width = width
    self.rect.height = height
    self.rect.x=x
    self.rect.y=y

    pygame.sprite.Sprite.__init__(self)
    WINDOW = pygame.display.get_surface()

#Updating moveing block to block
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

#Enemy behaviour
class enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_width,enemy_height,enemy_image,x,y,):
        self.image=enemy_image
        self.rect=self.image.get_rect()
        self.rect.width = enemy_width
        self.rect.height = enemy_height
        self.rect.x=x
        self.rect.y=y

        pygame.sprite.Sprite.__init__(self)
        WINDOW = pygame.display.get_surface()

    def enemy_move():
        pass

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

#Could be done in check_collision and creating a coin
class Coin(pygame.sprite.Sprite):
  def__init__(self, x, y):
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
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "xS    x           x   x   x     xx",  
    "x  x  x  x  x  x        x   xxxxxx",  
    "x  x  x  x  x  x  x  xxxx  xxxx xx",
    "x     x  x  x  x     x  x  xx    x", 
    "x  x  x  x  x  x  x  x  x        x", 
    "x  xx   xx  x   xxx     x       xx",
    "x xxxxxxxx xxxx  xxxxx  xxxxxxx xx",
    "x  xxxx    xxxxx     x  xxx     xx",
    "x    xxx  xxx  xxxxxxx  xxx      x",
    "x    xxx            xx  xxxxxxxxxx",
    "xxxx  xx  xxxxxxxxx xx           x",
    "x     xx            xx        E  x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",




]

TILE_SIZE = 24


loop=True
#Make player start at S
for y, row in enumerate(level_1):
    for x, char in enumerate(row):
        if char == "S":
            player_x, player_y = x * TILE_SIZE, y * TILE_SIZE
        elif char == "E":
            enemy_x, enemy_y = x * TILE_SIZE, y * TILE_SIZE

player_init = Player(20, 20, 100,50,PLAYER_IMAGE,player_x,player_y) #Creating a player as a object
enemy_init = enemy(ENEMY_WIDTH,ENEMY_HEIGHT,ENEMY_IMAGE,enemy_x,enemy_y)

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

    #WINDOW.fill((0,0,0))
    # pygame.draw.rect(WINDOW,(50,50,50),Player)
    WINDOW.blit(BACKGROUND_TEST, (0, 0))
    #pygame.draw.rect(WINDOW, BLACK, WIN_EDGE)
    #pygame.draw.rect(WINDOW, (255, 0, 0), player_init.rect)
    WINDOW.blit(PLAYER_COMP, (player_init.rect.x, player_init.rect.y))
    WINDOW.blit(ENEMY_IMAGE, (enemy_init.rect.x, enemy_init.rect.y))
    #WINDOW.fill(black) 
      
    draw_maze(level_1) 

    move=pygame.key.get_pressed()
    if move:
        movement(player_init.rect,move)

    for wall_rect in maze_walls:
        if player_init.rect.colliderect(wall_rect):
            player_init.rect.x = old_player_x
            player_init.rect.y = old_player_y

    if level_1[int(player_init.rect.y / TILE_SIZE)][int(player_init.rect.x / TILE_SIZE)] == 'E':
        print("Congratulations! You reached the exit!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
            
    pygame.display.update()

    




pygame.quit()
