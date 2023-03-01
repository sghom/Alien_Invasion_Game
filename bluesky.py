import sys
import pygame

class Sky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,250))
            pygame.display.flip()

inst = Sky()
inst.run()