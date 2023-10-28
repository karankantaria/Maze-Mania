from typing import Any
import pygame 
import os
import math

#Monday lecture nic day talked about djikstra's algorithm, we can use A* instead which is just dji's but with a heuristic


class enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_width,enemy_height,enemy_image,x,y):
        self.image=enemy_image
        self.rect=self.image.get_rect()
        self.rect.width = enemy_width
        self.rect.height = enemy_height
        self.rect.x=x
        self.rect.y=y

        pygame.sprite.Sprite.__init__(self)
        WINDOW = pygame.display.get_surface()


class Node():
    def __innit__(self):
        pass

    def calc_cost(self,goal):
        pass

    def print_node(self):
        pass

    def get_neighbours(self):
        pass

    def get_current_node(self):
        pass



def enemy_move(player_rect,enemy_rect):
    player_x, player_y = player_rect.center
    enemy_x, enemy_y = enemy_rect.center
    angle = math.atan2(player_y - enemy_y, player_x - enemy_x)
    speed = 2 
    enemy_x += speed * math.cos(angle)
    enemy_y += speed * math.sin(angle)
    enemy_rect.center = (enemy_x, enemy_y)

def enemy_collision(player_rect,enemy_rect,player_health): 
    if player_rect.colliderect(enemy_rect):
        player_health.health -= 1

def a_star_pathfinding(player,enemy,level):
    enemy_x, enemy_y = enemy.rect.center
    player_x, player_y = player.rect.center
    start= Node(enemy_x,enemy_y)
    node = Node(enemy_x,enemy_y)
    goal = Node(player_x,player_y)
    current_node = start

