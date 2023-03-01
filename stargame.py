import sys
import pygame

from star import Star

class StarsGame:
    def __init__(self):
        pygame.init()
        screen_width = 1200
        screen_height = 800
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Star game')

        self.stars = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self._create_stars()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = 1200 - (2*star_width)
        number_stars = available_space_x // (2*star_width)

        available_space_y = 800 - (2*star_height)
        number_rows = available_space_y // (2*star_height)

        for row_number in range(number_rows):
            for star_number in range (number_stars):
                self._create_star(star_number,row_number)

    def _create_star(self,star_number,row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.y = star_height + 2 * star_height * row_number
        star.rect.y = star.y
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill((50,50,50))
        self.stars.draw(self.screen)
        pygame.display.flip()

inst = StarsGame()
inst.run_game()