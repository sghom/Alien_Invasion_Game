import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen
        filepath = "C:/Users/lazd/backup/career/python/alien_invasion/images/star.bmp"
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #self.x = float(self.rect.x)