import sys
import pygame

from rocket import Rocket

class RocketGame:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Rocket Game')

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)    

    def _check_events_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_events_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update(self):
        self.screen.fill((230,230,230))
        self.rocket.blitme()
        pygame.display.flip()


inst = RocketGame()
inst.run_game()
    