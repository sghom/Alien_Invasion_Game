import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        filepath = "C:/Users/lazd/backup/career/python/alien_invasion/images/raindrop.bmp"
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_disappeared(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.bottom:
            return False

    def update(self):
        self.y += 1.5
        self.rect.y = self.y