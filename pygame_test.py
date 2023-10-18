import pygame 

pygame.init()
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
#16:9^
screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("TCA2")

rectangle_test=pygame.Rect(100,100,50,50)
rectangle_test.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


def movement(entity,key_press):
    if move[pygame.K_a]:
        rectangle_test.move_ip(-1,0) 
    elif move[pygame.K_d]:
        rectangle_test.move_ip(1,0) 
    elif move[pygame.K_w]:
        rectangle_test.move_ip(0,-1)
    elif move[pygame.K_s]:
        rectangle_test.move_ip(0,1)

loop=True
while loop:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),rectangle_test)
    move=pygame.key.get_pressed()
    movement(rectangle_test,move)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
    pygame.display.update()


pygame.quit()
