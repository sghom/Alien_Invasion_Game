import pygame
from pygame.sprite import Sprite

class Bullet():
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.rect = pygame.Rect(0,0,15,3)
        self.rect.midright = ai_game.shipt.rect.midright

        self.x = self.rect.x

    def update(self):
        self.x += 10
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,(60,60,60),self.rect)
