import pygame
import numpy as np 
from Enemy import Enemy

imgs = []

for x in range(1, 2):
    image = pygame.image.load(f"Images/Eye/{x}.png")
    imgs.append(pygame.transform.scale(image, (40, 40)))


class Eye(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 1
        self.width = 40
        self.height = 40
        self.health = self.max_health
        self.name = "Eye"
        self.imgs = imgs[:]
        self.hearts_to_take = 1
        self.speed_increase = 1.5
        self.animation_time = 0
