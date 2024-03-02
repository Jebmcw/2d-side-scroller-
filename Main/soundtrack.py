import pygame
from pygame import mixer

def soundtrack():
    mixer.init()
    mixer.music.load('Main/music/Title Theme.wav')
    mixer.music.set_volume(0.2)
    mixer.music.play()