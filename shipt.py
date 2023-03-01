import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        filepath = "C:/Users/lazd/backup/career/python/alien_invasion/images/rockett.bmp"
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.centre_ship()

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 3
        if self.moving_up and self.rect.top > 0:
            self.y -= 3
    
        self.rect.y = self.y
        
    def centre_ship(self):
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)