import sys
import pygame

from target import Target
from shipt import Ship
from bullett import Bullet
from buttont import Button

class TargetPractice:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Target Practice')

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = Button(self,"Play")
    
    def run_game(self):
        while True:
            self._check_events()
            self.target.update()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_KEYDOWN_events(event)
            elif event.type == pygame.KEYUP:
                self._check_KEYUP_events(event)

    def _check_KEYDOWN_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _check_KEYUP_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill((230,230,230))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.target.draw_target()
        self.play_button.draw_button()

        pygame.display.flip()

inst = TargetPractice()
inst.run_game()