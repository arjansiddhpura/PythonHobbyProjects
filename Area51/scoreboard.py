import json
import pygame.font
from pygame.sprite import Sprite

from ship import Ship

class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('resources/sfpro.ttf', 25)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship_image, self.ship_rect)
        self.ships.draw(self.screen)

    def prep_score(self):
        rounded_score = self.stats.score
        score_str = "score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_high_score(self):
        high_score = self.stats.high_score
        high_score_str = "high score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

            filename = 'resources/last_high_score.json'
            with open(filename, 'w') as f_obj:
                json.dump(self.stats.high_score, f_obj)

    def prep_level(self):
        level_str = "level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = pygame.sprite.Group()
        self.ship_image = self.font.render("ships left: ", True, self.text_color, self.settings.bg_color)
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 40
            self.ships.add(ship)
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.x = 10
        self.ship_rect.y = 10
