import pygame
import math

class Place():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.img = pygame.image.load("Images/Build_place.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = self.img.get_rect()
        self.selected = False
        self.tower_prices = [30]
        self.tower_images = [pygame.transform.scale(pygame.image.load("Images/Big_turret.png"), (20,20))]
        self.tower_coordinates = [(380,735)]

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        if self.selected:
            self.draw_menu(win)

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                self.selected = True
                return True
        self.selected = False
        return False

    def draw_menu(self, win):
        win.blit(pygame.transform.scale(pygame.image.load("Images/Lives_menu.png").convert(), (100,70)), (375,730))
        for i, img in enumerate(self.tower_images):
            win.blit(img, (self.tower_coordinates[i]))
            win.blit(pygame.font.SysFont("comicsans", 30).render(str(self.tower_prices[i]), 1, (255,255,255)), (self.tower_coordinates[i][0], self.tower_coordinates[i][1] + 40))
        
    def check_if_tower_clicked(self, X, Y):
        for i, coordinate in enumerate(self.tower_coordinates):
            if X <= coordinate[0] + self.width and X >= coordinate[0]:
                if Y <= coordinate[1] + self.height and Y >= coordinate[1]:
                    return i
        return None