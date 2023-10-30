from typing import Any
import pygame 
import os
import math

#Monday lecture nic day talked about djikstra's algorithm, we can use A* instead which is just dji's but with a heuristic


class enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_width,enemy_height,enemy_image,x,y,level):
        self.image=enemy_image
        self.rect=self.image.get_rect()
        self.rect.width = enemy_width
        self.rect.height = enemy_height
        self.rect.x=x
        self.rect.y=y
        self.level=level

        pygame.sprite.Sprite.__init__(self)
        WINDOW = pygame.display.get_surface()

    def enemy_to_player(self,player_rect,maze_wall):
        path = self.calc_path(self.rect.center, player_rect.center, maze_wall)

        if path:
            next_position = path[0]
            x, y = next_position
            self.rect.center = (x, y)

    def calc_path(self, start, end, maze_walls):
        open_set = [Node(start[0], start[1], None)]
        closed_set = set()

        while open_set:
            current_node = min(open_set, key=lambda node: node.calc_cost())

            if current_node.x == end[0] and current_node.y == end[1]:
                path = []
                while current_node:
                    path.append((current_node.x, current_node.y))
                    current_node = current_node.parent
                return path[::-1] 

            open_set.remove(current_node)
            closed_set.add((current_node.x, current_node.y))

            for neighbor in self.get_neighbors(current_node, maze_walls):
                neighbor_position = (neighbor.x, neighbor.y)
                if neighbor_position in closed_set:
                    continue

                tentative_g_cost = current_node.g_cost + 1

                if neighbor not in open_set or tentative_g_cost < neighbor.g_cost:
                    neighbor.parent = current_node
                    neighbor.g_cost = tentative_g_cost
                    neighbor.h_cost = self.heuristic(neighbor, Node(end[0], end[1], None))

                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return [] 

    def get_neighbors(self, node, maze_walls):
        neighbors = []
        x, y = node.x, node.y

        positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for (new_x, new_y) in positions:
            if 0 <= new_x < len(self.level[0]) and 0 <= new_y < len(self.level_1):
                if self.level_1[new_y][new_x] != "x" and not self.is_colliding_with_walls(new_x, new_y, maze_walls):
                    neighbors.append(Node(new_x, new_y, node))

        return neighbors


    def is_colliding_with_walls(self, x, y, maze_walls):
        for wall_rect in maze_walls:
            if wall_rect.collidepoint(x, y):
                return True
        return False

    def heuristic(self, node, goal):
        return abs(node.x - goal.x) + abs(node.y - goal.y)



class Node:
    def __init__(self,x,y,parent=None):
        self.x=x
        self.y=y
        self.parent=parent
        self.current_cost=0
        self.heuristic_cost=0

    def calc_cost(self):
        tot_cost=self.current_cost+self.heuristic_cost
        return tot_cost




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


