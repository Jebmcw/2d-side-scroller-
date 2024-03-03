import pygame
import os
import math
import time

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
        
        # Frame rate and timing for spawns
        self.FPS = 25
        self.start_time = time.time()
        self.spawn_intervals = [1, 19, 20, 10, 10] # seconds between spawns
        self.next_spawn_time = self.spawn_intervals[0]
        self.spawn_index = 0

    def spawn_mobs(self):
        # use the static method from Mob class
        mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 3, 350, 50)
        self.mobs.add(*mobs_to_add)
        
    
            
    def run(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        
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
            if self.scroll >= 0:  # Leftward scrolling
                self.scroll -= self.background_width
            self.scroll_frames_remaining_backwards -= 2
            
        if self.scroll < self.max_scroll:
            self.max_scroll = self.scroll
            
        # Render the background tiles
        for i in range(self.tiles):
            self.display.blit(self.background, (i * self.background_width + self.scroll, 0))

            
        if elapsed_time >= self.next_spawn_time:
            self.spawn_mobs()
            self.spawn_index +=1
            if self.spawn_index < len(self.spawn_intervals):
                self.next_spawn_time += self.spawn_intervals[self.spawn_index]
            else:
                self.next_spawn_time = float('inf') # Stop spawning after last interval
                
        # Update and draw mobs
        self.mobs.update()
        
        for mob in self.mobs:
            self.display.blit(mob.image, (mob.rect.x + self.scroll, mob.rect.y))
            Mob.draw_health_bar(self.display, mob,self.scroll)




















        









