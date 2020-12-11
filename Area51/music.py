import pygame

pygame.mixer.pre_init()
pygame.mixer.init(buffer=64)

def play_bgmusic():
    filename = 'resources/bg_music.mp3'
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

def stop_bgmusic():
    pygame.mixer.music.fadeout(3000)

def play_bullet_sound():
    filename = 'resources/bullet_fire.wav'
    bullet_fire_sound = pygame.mixer.Sound(filename)
    bullet_fire_sound.set_volume(0.1)
    bullet_fire_sound.play()

def play_ship_crash():
    filename = 'resources/ship_crash.wav'
    ship_crash_sound = pygame.mixer.Sound(filename)
    ship_crash_sound.set_volume(0.5)
    ship_crash_sound.play()
