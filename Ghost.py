import pygame
import numpy as np 
from Enemy import Enemy

imgs = []

for x in range(1, 2):
    image = pygame.image.load(f"Images/Ghost/{x}.png")
    imgs.append(pygame.transform.scale(image, (64, 64)))


class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 2
        self.health = self.max_health
        self.name = "Ghost"
        self.imgs = imgs[:]
        self.hearts_to_take = 1
        self.speed_increase = 1
        self.animation_time = 0
