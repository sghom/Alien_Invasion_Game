import pygame

class Rocket:
    def __init__(self,r_game):
        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()

        filepath = "C:/Users/lazd/backup/career/python/alien_invasion/images/rocket.bmp"
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image,self.rect)
