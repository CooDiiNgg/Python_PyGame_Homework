import pygame
import random
import test
import numpy as np
from Ghost import Ghost
import time

pygame.init()
clock = pygame.time.Clock()

# Createing tower defense game

class TowerDefence:
    def __init__(self):
        # self.map = map
        # self.hero = hero
        self.enemies = []
        self.towers = []
        self.Big_turrets = []
        # self.Big_turret_img = pygame.transform.scale(pygame.image.load("Images/Big_turret.png").convert(), (50,50))
        self.buying_tower = []
        self.set_map()
        self.money = 75
        self.money_on_round = 25
        self.lives = 10
        self.wave = []
        self.waves = [[1,0],[4,0]]
        self.wave_count = 0
        self.timer = 0
    
    def set_map(self):
        self.width = 1200
        self.height = 800
        self.display = pygame.display.set_mode((self.width, self.height))
        self.map = pygame.image.load("Images/Map.png").convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))
    
    def display_everything(self):
        self.display.blit(self.map, (0, 0))
        for tower in self.towers:
            self.display.blit(self.tower_build_img, tower)
        for turret in self.Big_turrets:
            self.display.blit(pygame.transform.scale(pygame.image.load("Images/Big_turret.png").convert(), (50,50)), turret)
        self.add_life_menu()
        for enemy in self.enemies:
            enemy.draw(self.display)
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
    
    def set_tower_build_places(self):
        # for now static than will be random
        self.tower_build_img = pygame.image.load("Images/Build_place.png")
        self.towers.append(self.tower_build_img.get_rect())
        self.towers[0].x = 106
        self.towers[0].y = 138
        # self.towers.append((106, 138))
        self.towers.append(self.tower_build_img.get_rect())
        self.towers[1].x = 297
        self.towers[1].y = 85
        # self.towers.append((297, 85))
        self.towers.append(self.tower_build_img.get_rect())
        self.towers[2].x = 297
        self.towers[2].y = 200
        # self.towers.append((297, 200))
        self.towers.append(self.tower_build_img.get_rect())
        self.towers[3].x = 463
        self.towers[3].y = 184
        # self.towers.append((463, 184))
        self.tower_build_img = pygame.transform.scale(self.tower_build_img.convert(), (50,50))
    
    def add_life_menu(self):
        self.display.blit(pygame.transform.scale(pygame.image.load("Images/Lives_menu.png").convert(), (450,70)), (375,0))
        # add lives in numbers on the menu
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.lives), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (405,35)
        self.display.blit(text, textRect)
        self.display.blit(pygame.transform.scale(pygame.image.load("Images/Heart.png").convert(), (35,35)), (429,16))
        text = font.render(("+"+str(self.money_on_round)), True, (0, 255, 0))
        textRect = text.get_rect()
        textRect.center = (565,35)
        self.display.blit(text, textRect)
        text = font.render(("$" + str(self.money)), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (750,35)
        self.display.blit(text, textRect)
    
    def right_menu(self, option, tower):
        self.option = option
        self.current_tower = tower
        self.display.blit(pygame.transform.scale(pygame.image.load("Images/Lives_menu.png").convert(), (450,70)), (375,730))
        # add options for towers
        if option == 0:
            # needs to build tower(For now we havee only one)
            self.display.blit(pygame.transform.scale(pygame.image.load("Images/Big_turret.png").convert(), (50,50)), (380,735))
            font = pygame.font.Font('freesansbold.ttf', 18)
            text = font.render(("$30"), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (405,760)
            self.display.blit(text, textRect)
            self.buying_tower.append(pygame.transform.scale(pygame.image.load("Images/Big_turret.png").convert(), (50,50)).get_rect())
            self.buying_tower[0].x = 380
            self.buying_tower[0].y = 735
        elif option == 1:
            # already builded tower can upgrade to level 2(first tower)
            # will do leter(dont have the tower image)
            pass
    
    def set_waves(self):
        if sum(self.wave) == 0:
            if self.wave_count == len(self.waves):
                return
            if len(self.enemies) == 0:
                self.wave = self.waves[self.wave_count]
                self.wave_count += 1
                self.money += self.money_on_round
                self.money_on_round += 25
        else:
            en = [Ghost(), None]
            for x in range(len(self.wave)):
                if self.wave[x] != 0:
                    self.wave[x] -= 1
                    self.enemies.append(en[x])
                    


        




def test_functions():
    running = True
    game = TowerDefence()
    game.set_tower_build_places()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if game.lives == 0:
            running = False
        clock.tick(60)
        if time.time() - game.timer >= random.randrange(2, 20):
            game.timer = time.time()
            game.set_waves()
        to_delete = []
        if len(game.enemies) != 0:
            for enemy in game.enemies:
                if enemy.y > 800:
                    game.lives -= enemy.hearts_to_take
                    to_delete.append(enemy)
                enemy.move()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         for tower in game.towers:
            #             if tower.collidepoint(event.pos):
            #                 game.right_menu(0, tower)
            #                 break
            #         for i, option in enumerate(game.buying_tower):
            #             if option.collidepoint(event.pos):
            #                 if game.option == 0:
            #                     if i == 0:
            #                         if game.money >= 30:
            #                             game.money -= 30
            #                             rct = game.towers[game.current_tower]
            #                             game.Big_turrets.append(rct)
            #                             game.towers.pop(game.current_tower)
            #                             game.right_menu(1)
            #                 break
        for delete in to_delete:
            game.enemies.remove(delete)
        game.display_everything()
    
    pygame.quit()


test_functions()