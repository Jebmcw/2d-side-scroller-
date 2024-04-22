import pygame
from pygame import mixer

def set_volume(volume):
    print("Setting volume to:", volume) 
    mixer.music.set_volume(volume)

def soundtrack(file_path, volume=0.5):  # Default volume is 0.5
    mixer.init()
    mixer.music.load(file_path)
    set_volume(volume)
    mixer.music.play(-1, fade_ms=5000)