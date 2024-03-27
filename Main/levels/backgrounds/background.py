import pygame
import os

class Background():
    def __init__(self):
        self.bg_images = []
        for i in range(1, 6):
            self.bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
            self.bg_images.append(self.bg_image)
            self.bg_width = self.bg_images[0].get_width()
            
    @staticmethod
    def draw_bg(self):
        for x in range(8):
            self.speed = 1
            for i in self.bg_images:
                self.screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.001
