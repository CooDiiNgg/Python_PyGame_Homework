import pygame
import math
import os

class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(150, -10),(160, 20), (175, 180), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 492), (740, 504), (580, 542), (148, 541), (100, 442), (110, 600), (115, 700), (115, 800)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_health = 0
        self.hearts_to_take = 0
        self.speed_increase = 0

    def draw(self, win):
       
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
       
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0)

    def collide(self, X, Y):
       
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
       
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (115, 850)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1), (y2-y1))
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)


        move_x = self.x + dirn[0] * self.speed_increase
        move_y = self.y + dirn[1] * self.speed_increase

        
        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    def hit(self, damage):
        
        self.health -= damage
        if self.health <= 0:
            return True
        return False