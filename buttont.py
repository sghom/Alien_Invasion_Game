import pygame.font

class Button:
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0,0,200,50)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self,msg):
        self.msg_image = pygame.font.SysFont(None,48).render(msg,True,(255,255,255),(0,255,0))
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill((0,255,0),self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)