import pygame
import math
from Bullets import Bullet


class Fast_turret():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.damadge = 1
        self.img = pygame.image.load("Images/Fast_turret.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.range = 300
        self.shoot_speed = 6
        self.shoot = (self.x, self.y)
        self.bullets = []
        self.tower_timer = 0
        self.min_shoot_delay = 2

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        for bullet in self.bullets:
           bullet.draw(win)
    
    def collide_range(self, X, Y):
        if X <= self.x + (self.range/2) and X >= self.x - (self.range/2):
            if Y <= self.y + (self.range/2) and Y >= self.y - (self.range/2):
                self.shoot = (X,Y)
                return True
        self.shoot = (self.x, self.y)
        return False
    
    def shooting(self):
        for bullet in self.bullets:
            if not bullet.active:
                self.bullets.remove(bullet)
            bullet.update()
    
    def shoot_bullet(self):
        self.bullets.append(Bullet(self.x, self.y, self.shoot[0], self.shoot[1], self.shoot_speed))

        


