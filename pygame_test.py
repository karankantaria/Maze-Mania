import pygame 
import os

pygame.init()
SCREEN_WIDTH = 704
SCREEN_HEIGHT = 320
#16:9^
WINDOW=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
BLACK=(0,0,0)
WIN_EDGE = pygame.Rect(SCREEN_WIDTH//2 - 5, 0, 10, SCREEN_HEIGHT)
pygame.display.set_caption("TCA2")
BACKGROUND_TEST = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Grass_Sample.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'test_sprite.png'))
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60
PLAYER_COMP = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

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


#test changes
pygame.quit()
