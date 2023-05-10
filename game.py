import pygame
import random

pygame.init()


class Game():
    def __init__(self):
        self.screen = None
        self.background = None
        self.playerImg = None
        self.playerX = 30
        self.playerY = 400
        self.playerX_change = 0
        self.playerY_change = 0
        self.bossImg = None
        self.bossX = None
        self.bossY = None
        self.bossX_change = None
        self.bossY_change = None
        self.bulletImg = None
        self.bulletX = None
        self.bulletY = None
        self.bulletX_change = None
        self.bulletY_change = None
    

    def Create_Screen(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Boss Fight Plane Game")
        # self.background = pygame.image.load("/Images/background.png")
        # for now it will be a basic color
        self.background = (0, 0, 0)

    def Create_Player(self):
        # self.playerImg = pygame.image.load("/Images/player.png")
        # For now, I will use a rectangle for the player
        self.playerImg = pygame.draw.rect(self.screen, (255, 255, 255), (self.playerX, self.playerY, 64, 64))
        self.playerX_change = 0
        self.playerY_change = 0

    def Create_Boss(self):
        # self.bossImg = pygame.image.load("/Images/boss.png")
        # For now, I will use a rectangle for the boss
        self.bossX = 680
        self.bossY = 400
        self.bossImg = pygame.draw.rect(self.screen, (255, 255, 255), (self.bossX, self.bossY, 180, 180))
        self.bossX_change = 0
        self.bossY_change = 0
    
    def Create_Bullet(self):
        # self.bulletImg = pygame.image.load("/Images/bullet.png")
        # For now, I will use a rectangle for the bullet
        self.bulletX = 700
        self.bulletY = random.randint(0, 535)
        self.bulletImg = pygame.draw.rect(self.screen, (255, 255, 255), (self.bulletX, self.bulletY, 32, 32))
        self.bulletX_change = -10
        self.bulletY_change = 0
    
    

def main():
    game = Game()
    game.Create_Screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                game.playerX_change = -5
            if keys[pygame.K_d]:
                game.playerX_change = 5
            if keys[pygame.K_w]:
                game.playerY_change = -5
            if keys[pygame.K_s]:
                game.playerY_change = 5
            
            game.playerX += game.playerX_change
            game.playerY += game.playerY_change
            game.Create_Player()
            game.Create_Boss()
            pygame.display.update()
            game.screen.fill(game.background)



if __name__ == "__main__":
    main()