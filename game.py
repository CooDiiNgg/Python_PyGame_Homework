import pygame
import random

pygame.init()


# Createing tower defense game

class TowerDefence:
    def __init__(self):
        # self.map = map
        # self.hero = hero
        # self.enemies = enemies
        # self.towers = towers
        self.set_map()
        # self.set_hero_start_place(map)
        # self.set_tower_build_places()
    
    def set_map(self):
        #set the background
        self.display = pygame.display.set_mode((600, 800))
        self.map = pygame.image.load("Images/Map.png").convert()
        self.map = pygame.transform.scale(self.map, (600, 800))
    
    def display_map(self):
        self.display.blit(self.map, (0, 0))
        pygame.display.update()

    # def set_hero_start_place(self, map):
    #     self.hero_x = 0
    #     self.hero_y = 0
    #     for y in map:
    #         for x in y:
    #             if x == "S":
    #                 self.hero_x = map.index(y)
    #                 self.hero_y = y.index(x)
    #                 self.hero = pygame.image.load("Images/Hero_1.png")
    #                 self.hero.set_position(self.hero_x, self.hero_y)
    #                 break
    
    # def set_tower_build_places(self):
    #     # for now static than will be random
    #     self.tower_x = 12
    #     self.tower_y = 12
        




def test_functions():
    running = True
    game = TowerDefence()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.display_map()
    
    pygame.quit()


test_functions()