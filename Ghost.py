import pygame
import numpy as np 
from Enemy import Enemy

imgs = []

for x in range(1, 5):
    image = pygame.image.load(f"Images/Ghost/{x}.png").convert()
    imgs.append(pygame.transform.scale(image, (64, 64)))


class Ghost(Enemy):
    def __init__(self):
        self.max_health = 2
        self.health = self.max_health
        self.name = "Ghost"
        self.imgs = imgs[:]
        