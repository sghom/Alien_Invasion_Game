import sys
import pygame
from raindrop import Raindrop

class RaindropsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Raindrops')

        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_event_KEYDOWN(event)

    def _check_event_KEYDOWN(self,event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = 1200 - drop_width
        number_drops = available_space_x // (2 * drop_width)

        available_space_y = 800 - drop_height
        number_rows = available_space_y // (2 * drop_height)
        for row_num in range(number_rows):
            for drop_num in range(number_drops):
                self._create_drop(drop_num,row_num)

    
    def _create_drop(self,drop_num,row_num):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_num
        drop.rect.x = drop.x
        drop.y = 2 * drop_height * row_num
        drop.rect.y = drop.y
        self.raindrops.add(drop)

    def _update_raindrops(self):
        self.raindrops.update()
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                self.raindrops.remove(drop)

    def _update_screen(self):
        self.screen.fill((230,230,230))
        self.raindrops.draw(self.screen)
        pygame.display.flip()


inst = RaindropsGame()
inst.run_game()