import pygame
import os
import math

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        current_path = os.path.dirname(__file__)  # Ensure this path is correct.
        image_path = os.path.join(current_path, "backgrounds/level1_background.webp")
        self.background = pygame.image.load(image_path).convert_alpha()
        self.background_width = self.background.get_width()

        self.scroll = 0
        self.tiles = math.ceil(self.display.get_width() / self.background_width) + 1

        # Scroll settings
        self.scroll_speed = 5
        self.scroll_duration = 150 * 40
        self.scroll_frames_remaining = self.scroll_duration

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.scroll_frames_remaining > 0:
            self.scroll -= self.scroll_speed
            if self.scroll <= -self.background_width:
                self.scroll += self.background_width  # This ensures continuous scrolling

            self.scroll_frames_remaining -= 2

        # Render the background tiles
        for i in range(self.tiles):
            self.display.blit(self.background, (i * self.background_width + self.scroll, 0))


        
        



        









