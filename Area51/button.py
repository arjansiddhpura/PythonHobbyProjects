import pygame.font

from roundrects import aa_round_rect

class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.alien_face = pygame.image.load('resources/alien_face.png')
        self.alien_face_rect = self.alien_face.get_rect()
        self.alien_face_rect.centerx = self.screen_rect.centerx
        self.alien_face_rect.y = 270

        self.width, self.height = 175, 75
        self.button_color = (0, 255, 32)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('resources/sfpro.ttf', 45)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 410

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        aa_round_rect(self.screen, (513, 407, 175, 75), self.button_color, 37, 0)

    def draw_button(self):
        self.draw()
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.alien_face, self.alien_face_rect)
