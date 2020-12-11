import json

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False 

        filename = 'resources/last_high_score.json'
        with open(filename) as f_obj:
            self.high_score = json.load(f_obj)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
