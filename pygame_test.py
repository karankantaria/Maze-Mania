import pygame 
import os

pygame.init()
# SCREEN_WIDTH = 704
# SCREEN_HEIGHT = 320
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
#16:9^
WINDOW=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
BLACK=(0,0,0)
WIN_EDGE = pygame.Rect(SCREEN_WIDTH//2 - 5, 0, 10, SCREEN_HEIGHT)
pygame.display.set_caption("TCA2")
BACKGROUND_TEST = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Grass_Sample.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'test_sprite.png'))
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60
PLAYER_COMP = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)#rotate redundant for now

#Creating a class for player the main character
class Player(pygame.sprite.Sprite):
  
  def __init__(self,width, height, speed, max_health,player_image=PLAYER_IMAGE):
    #self.rect = pygame.Rect(2, 2, width, height) # linking pygame
    self.image=player_image
    self.rect=self.image.get_rect()
    self.speed = speed # Creating the variable 
    self.max_health = max_health
    self.rect.width = width
    self.rect.height = height
    pygame.sprite.Sprite.__init__(self)
    screen = pygame.display.get_surface()

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

#Enemy behaviour
def enemy():
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
#Could be done in check_collision
def coin_collect():
    pass

loop=True
player_init = Player(20, 20, 100,50,PLAYER_IMAGE) #Creating a player as a object
while loop:
    #WINDOW.fill((0,0,0))
    # pygame.draw.rect(WINDOW,(50,50,50),Player)
    WINDOW.blit(BACKGROUND_TEST, (0, 0))
    #pygame.draw.rect(WINDOW, BLACK, WIN_EDGE)
    #pygame.draw.rect(WINDOW, (255, 0, 0), player_init.rect)
    WINDOW.blit(PLAYER_COMP, (player_init.rect.x, player_init.rect.y))
    move=pygame.key.get_pressed()
    if move:
        movement(player_init.rect,move)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
    pygame.display.update()

import pygame 

pygame.init()

#set up display

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
#16:9^
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("MazeMania")

#define color

black = (0, 0, 0)
white = (255, 255, 255)


#created the outline and color of maze


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


def draw_maze(level):
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == "x":
               pygame.draw.rect(screen, white, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

running = True
while running:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     running = False

            screen.fill(black)  
            draw_maze(level_1)    
            pygame.display.update()

    


pygame.quit()


pygame.quit()
