import sys
import pygame

from bird import Bird

class BlueBirdGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Bird Game')

        self.bird = Bird(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0,0,0))
            self.bird.blitme()    

            pygame.display.flip()

inst = BlueBirdGame()
inst.run_game()