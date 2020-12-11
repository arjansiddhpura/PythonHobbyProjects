import random

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 9
        self.bullets_allowed = 5

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points += int(1)

    def randomize_color(self):
        a = (255, 0, 0)
        b = (0, 255, 0)
        c = (0, 0, 255)
        d = (255, 255, 0)
        e = (255, 0, 255)
        f = (0, 255, 255)

        color_options = [a, b, c, d, e, f]
        return random.choice(color_options)
