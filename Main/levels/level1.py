import pygame
import os
import math

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "level1_background.webp")
        self.background = pygame.image.load(image_path).convert_alpha()
        self.background_width = self.background.get_width()
        print(self.background_width)
        self.scroll = 0
        self.tiles = math.ceil(1500 / self.background_width) + 1
        
        
    def run(self):
        for i in range(0, self.tiles):
            self.display.blit(self.background, (i  * self.background_width + self.scroll, 0))
        self.scroll -= 5
        
        if abs(self.scroll) > self.background_width:
            self.scroll = 0

        


        









