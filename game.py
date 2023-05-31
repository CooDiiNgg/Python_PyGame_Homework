import pygame
import random
import test
import numpy as np
from Ghost import Ghost
from Eye import Eye
from Place_to_build import Place
from Big_turret import Big_turret
from Fast_turret import Fast_turret
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
        self.Real_towers = []
        # self.Big_turret_img = pygame.transform.scale(pygame.image.load("Images/Big_turret.png").convert(), (50,50))
        self.set_map()
        self.money = 75
        self.money_on_round = 25
        self.lives = 10
        self.wave = []
        self.waves = [[6,1],[4,0]]
        self.wave_count = 0
        self.timer = 0
        self.win = False
    
    def set_map(self):
        self.width = 1200
        self.height = 800
        self.display = pygame.display.set_mode((self.width, self.height))
        self.map = pygame.image.load("Images/Real_map.png").convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))
    
    def display_everything(self):
        self.display.blit(self.map, (0, 0))
        for tower in self.towers:
            tower.draw(self.display)
        for turret in self.Real_towers:
            turret.draw(self.display)
        self.add_life_menu()
        for enemy in self.enemies:
            enemy.draw(self.display)
        if self.win:
            self.win_screen()
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
        self.towers.append(Place())
        self.towers[0].x = 313
        self.towers[0].y = 293
        # self.towers.append((106, 138))
        self.towers.append(Place())
        self.towers[1].x = 297
        self.towers[1].y = 85
        # self.towers.append((297, 85))
        self.towers.append(Place())
        self.towers[2].x = 102
        self.towers[2].y = 346
        # self.towers.append((297, 200))
        self.towers.append(Place())
        self.towers[3].x = 515
        self.towers[3].y = 422
        # self.towers.append((463, 184))
        self.towers.append(Place())
        self.towers[4].x = 663
        self.towers[4].y = 425
        # self.towers.append((663, 425))
        self.towers.append(Place())
        self.towers[5].x = 445
        self.towers[5].y = 611
        # self.towers.append((445, 611))
        self.towers.append(Place())
        self.towers[6].x = 737
        self.towers[6].y = 611
        # self.towers.append((737, 611))
    
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
    
    
    def set_waves(self):
        if sum(self.wave) == 0:
            if self.wave_count == len(self.waves):
                if len(self.enemies) == 0:
                    self.win = True
                return
            if len(self.enemies) == 0:
                self.wave = self.waves[self.wave_count]
                self.wave_count += 1
                self.money += self.money_on_round
                self.money_on_round += 25
        else:
            en = [Ghost(), Eye()]
            for x in range(len(self.wave)):
                if self.wave[x] != 0:
                    self.wave[x] -= 1
                    self.enemies.append(en[x])
                    break
    
    def win_screen(self):
        self.display.blit(pygame.transform.scale(pygame.image.load("Images/Win_screen.png").convert(), (1200,800)), (0,0))
        pass
                    


        




def test_functions():
    running = True
    game = TowerDefence()
    game.set_tower_build_places()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if game.lives <= 0:
            running = False
        clock.tick(60)
        if time.time() - game.timer >= random.randrange(2, 20):
            game.timer = time.time()
            game.set_waves()
        to_delete = []
        if len(game.enemies) != 0:
            for enemy in game.enemies:
                if enemy.x > 1200:
                    game.lives -= enemy.hearts_to_take
                    to_delete.append(enemy)
                enemy.move()
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    towers = [Big_turret(), Fast_turret()]
                    for tower in game.towers:
                        if tower.check_if_tower_clicked(event.pos[0], event.pos[1]) != None and tower.selected == True and game.money >= tower.tower_prices[tower.check_if_tower_clicked(event.pos[0], event.pos[1])]:
                            game.money -= tower.tower_prices[tower.check_if_tower_clicked(event.pos[0], event.pos[1])]
                            tower.selected = False
                            game.Real_towers.append(towers[tower.check_if_tower_clicked(event.pos[0], event.pos[1])])
                            game.Real_towers[-1].x = tower.x
                            game.Real_towers[-1].y = tower.y
                            game.towers.remove(tower)
                            break
                    for tower in game.towers:
                        if tower.collide(event.pos[0], event.pos[1]):
                            break

        for enemy in game.enemies:
            for tower in game.Real_towers:
                if tower.collide_range(enemy.x, enemy.y):
                    tower.shooting()
                    if time.time() - tower.tower_timer >= random.randrange(tower.min_shoot_delay, 10):
                        tower.shoot_bullet()
                        tower.tower_timer = time.time()
                    for bullet in tower.bullets:
                        if enemy.collide(bullet.x, bullet.y):
                                enemy.hit(tower.damadge)
                                bullet.active = False
                                break
                    
            

        for enemy in game.enemies:
            if enemy.health <= 0:
                to_delete.append(enemy)

        for delete in to_delete:
            game.enemies.remove(delete)
        game.display_everything()
    
    pygame.quit()


test_functions()