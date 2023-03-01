import pygame

class Target:
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0,0,15,120)

        self.center_target()

        self.direction = 1

    def update(self):
        self.y += self.direction * 1.5

        if self.rect.bottom == self.screen_rect.bottom:
            self.direction = -1
        elif self.rect.top == self.screen_rect.top:
            self.direction = 1

        self.rect.y = self.y

    def center_target(self):
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def draw_target(self):
        pygame.draw.rect(self.screen,(180, 60,10),self.rect)