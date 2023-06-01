import pygame
import math


class Bullet:
    def __init__(self, x, y, X, Y, speed):
        self.x = x
        self.y = y
        self.en_x = X
        self.en_y = Y
        self.speed = speed
        self.active = True
        self.bullet_img = pygame.image.load("Images/Big_turret_ammo.png")
        self.bullet_img = pygame.transform.scale(self.bullet_img, (10,10))
    
    def update(self):
        # Calculate the direction vector towards the enemy's current position
        dir_x = self.en_x - self.x
        dir_y = self.en_y - self.y
        distance = math.sqrt(dir_x ** 2 + dir_y ** 2)
        if distance == 0:
            self.x = self.en_x
            self.y = self.en_y
            return
        direction = (dir_x / distance, dir_y / distance)
        
        # Move the bullet along the direction vector
        self.x += direction[0] * self.speed
        self.y += direction[1] * self.speed

        # Check if the bullet reaches its target
        if distance <= self.speed:
            self.x = self.en_x
            self.y = self.en_y
            self.active = False
    
    def draw(self, win):
        if self.active:
            win.blit(self.bullet_img, (self.x, self.y))
