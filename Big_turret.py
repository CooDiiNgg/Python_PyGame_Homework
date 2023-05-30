import pygame
import math


class Big_turret():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.img = pygame.image.load("Images/Big_turret.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.range = 200

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))