import pygame 

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
#16:9^
screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("TCA2")

#Creating a class for player the main character
class Player:
  def __init__(self, x, y,width, height, speed, max_heath)
    self.rect = pygame.Rect(2, 2, width, height) # linking pygame
    self.speed = speed # Creating the variable 
    self.heath = max_heath

#Updating moveing block to block
def movement(entity,key_press):
    if move[pygame.K_a]:
        Player.move_ip(-1,0) 
    elif move[pygame.K_d]:
        Player.move_ip(1,0) 
    elif move[pygame.K_w]:
        Player.move_ip(0,-1)
    elif move[pygame.K_s]:
        Player.move_ip(0,1)

loop=True
player = player(2, 2, 20, 5, 100) #Creating a player as a object
while loop:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),Player)
    move=pygame.key.get_pressed()
    movement(Player,move)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
    pygame.display.update()


#test changes
pygame.quit()
