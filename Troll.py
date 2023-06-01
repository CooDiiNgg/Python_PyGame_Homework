import pygame
import numpy as np
from Enemy import Enemy

imgs = []

for x in range(1, 8):
    image = pygame.image.load(f"Images/Troll/{x}.png")
    imgs.append(pygame.transform.scale(image, (74, 74)))

class Troll(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 8
        self.health = self.max_health
        self.width = 80
        self.height = 80
        self.name = "Troll"
        self.imgs = imgs[:]
        self.hearts_to_take = 3
        self.speed_increase = 0.8
        self.animation_time = 0.15