import pygame
import os
import math
from levels.mobs.mobs_LevelOne import Mob  # Ensure this import path is correct for your project

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Load background
        current_path = os.path.dirname(__file__)  # Current file directory
        image_path = os.path.join(current_path, "backgrounds/level1_background.webp")
        self.background = pygame.image.load(image_path).convert_alpha()
        self.background_width = self.background.get_width()

        # Initialize scrolling variables
        self.scroll = 0
        self.tiles = math.ceil(self.display.get_width() / self.background_width) + 1
        self.scroll_speed = 3
        self.scroll_duration_foward = 100 * 25
        self.scroll_duration_backwards = 100 * 25
        self.scroll_frames_remaining_foward = self.scroll_duration_foward
        self.scroll_frames_remaining_backwards = self.scroll_duration_backwards
        
        self.mobs = pygame.sprite.Group()  # Corrected from a list to a sprite group
        self.health_bar = pygame.sprite.Group()
        
        # Frame rate and timing for spawns
        self.FPS = 25
        self.current_frame = 0
        self.spawn_frames = [self.FPS * 1, self.FPS * 20, self.FPS * 40, self.FPS * 50, self.FPS * 60]
        self.spawn_index = 0

    def spawn_mobs(self):
        # use the static method from Mob class
        mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 350, 50)
        self.mobs.add(*mobs_to_add)
        
    
            
    def run(self):
        self.current_frame += 1
        keys = pygame.key.get_pressed()

        
        self.display.fill((0, 0, 0))  # Fill the screen with black before redrawing the background

        if keys[pygame.K_d] and self.scroll_frames_remaining_foward > 0:
            self.scroll -= self.scroll_speed
            if self.scroll <= -self.background_width:
                self.scroll += self.background_width  # This ensures continuous scrolling
            self.scroll_frames_remaining_foward -= 2

        # Corrected logic for scrolling left
        elif keys[pygame.K_a] and self.scroll_frames_remaining_backwards > 0:
            self.scroll += self.scroll_speed
            if self.scroll >= 0:  # Adjust for leftward scrolling
                self.scroll -= self.background_width
            self.scroll_frames_remaining_backwards -= 2

        # Render the background tiles
        for i in range(self.tiles):
            self.display.blit(self.background, (i * self.background_width + self.scroll, 0))

        # Mob spawning, updating, and drawing
        if self.spawn_index < len(self.spawn_frames) and self.current_frame >= self.spawn_frames[self.spawn_index]:
            self.spawn_mobs()
            self.spawn_index += 1

        # Update and draw mobs
        self.mobs.update()
        
        for mob in self.mobs:
            self.display.blit(mob.image, (mob.rect.x + self.scroll, mob.rect.y))
            Mob.draw_health_bar(self.display, mob,self.scroll)




















        









