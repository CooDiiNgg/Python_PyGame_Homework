import pygame
import numpy as np 
from Enemy import Enemy

imgs = []

for x in range(1, 6):
    image = pygame.image.load(f"Images/Bat/{x}.png")
    imgs.append(pygame.transform.scale(image, (50, 50)))


class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 1
        self.width = 40
        self.height = 40
        self.health = self.max_health
        self.name = "Bat"
        self.imgs = imgs[:]
        self.hearts_to_take = 1
        self.speed_increase = 1.35
        self.animation_time = 0.2
