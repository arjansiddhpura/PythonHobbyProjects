import random
import pygame

from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('resources/star.png')
        self.rect = self.image.get_rect()

        self.random_x = random.randint(-100, 100)
        self.random_y = random.randint(-75, 75)
