import pygame
import math
from Bullets import Bullet


class Big_turret():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.delete_all = False
        self.width = 50
        self.height = 50
        self.damadge = [2, 2]
        self.img = [pygame.transform.scale(pygame.image.load("Images/Big_turret.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Images/Big_turret_lvl_1.png"), (self.width, self.height)), False]
        self.range = [200, 250]
        self.shoot_speed = [5, 6]
        self.shoot = (self.x, self.y)
        self.bullets = []
        self.tower_timer = 0
        self.min_shoot_delay = [4, 3]
        self.level = 0
        self.selected = False
        self.sell_prices = [20, 40]
        self.level_up_prices = [50]
        self.options = [pygame.transform.scale(pygame.image.load("Images/Sell.png"), (20,20)), self.img[self.level + 1]]
        self.options_coordinates = [(380,735), (430,735)]

    def draw(self, win):
        win.blit(self.img[self.level], (self.x, self.y))
        for bullet in self.bullets:
           bullet.draw(win)
        if self.selected:
            self.draw_menu(win)
    
    def collide_range(self, X, Y):
        if X <= self.x + (self.range[self.level]/2) and X >= self.x - (self.range[self.level]/2):
            if Y <= self.y + (self.range[self.level]/2) and Y >= self.y - (self.range[self.level]/2):
                self.shoot = (X,Y)
                return True
        self.shoot = (self.x, self.y)
        return False

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                self.selected = True
                return True
        self.selected = False
        return False
    
    def draw_menu(self, win):
        win.blit(pygame.transform.scale(pygame.image.load("Images/Lives_menu.png").convert(), (100,70)), (375,730))
        for i, img in enumerate(self.options):
            if self.img[self.level + 1] == False and i == 1:
                self.options_coordinates.remove(self.options_coordinates[i])
                self.options.remove(img)
                continue
            if i == 0:
                win.blit(img, (self.options_coordinates[i]))
                win.blit(pygame.font.SysFont("comicsans", 30).render(str(self.sell_prices[self.level]), 1, (255,255,255)), (self.options_coordinates[i][0], self.options_coordinates[i][1] + 40))
            else:
                win.blit(pygame.transform.scale(img, (20, 20)), (self.options_coordinates[i]))
                win.blit(pygame.font.SysFont("comicsans", 30).render(str(self.level_up_prices[self.level]), 1, (255,255,255)), (self.options_coordinates[i][0], self.options_coordinates[i][1] + 40))
    
    def check_if_option_clicked(self, X, Y):
        for i, coordinate in enumerate(self.options_coordinates):
            if X <= coordinate[0] + self.width and X >= coordinate[0]:
                if Y <= coordinate[1] + self.height and Y >= coordinate[1]:
                    return i
        return None

    def shooting(self):
        for bullet in self.bullets:
            if not bullet.active:
                self.bullets.remove(bullet)
            bullet.update()
    
    def shoot_bullet(self):
        self.bullets.append(Bullet(self.x, self.y, self.shoot[0], self.shoot[1], self.shoot_speed[self.level]))

        


