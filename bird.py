import pygame

class Bird:
    def __init__(self,inst_bird):
        self.screen = inst_bird.screen
        self.screen_rect = inst_bird.screen.get_rect()

        filepath = "C:/Users/lazd/backup/career/python/alien_invasion/images/bird_small.bmp"
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    