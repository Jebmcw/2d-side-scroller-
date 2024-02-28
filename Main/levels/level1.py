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
        self.scroll_speed = 5
        self.scroll_duration = 100 * 25
        self.scroll_frames_remaining = self.scroll_duration

        # Initialize mob storage using pygame.sprite.Group for better management
        self.mobs = pygame.sprite.Group()  # Corrected from a list to a sprite group

        # Frame rate and timing for spawns
        self.FPS = 25
        self.current_frame = 0
        self.spawn_frames = [self.FPS * 1, self.FPS * 5, self.FPS * 3]
        self.spawn_index = 0


    def spawn_mobs(self):
        
        self.spawn_mobs_horizontally(1, 350, 50)

    def spawn_mobs_horizontally(self, num_mobs, initial_y, spacing=0):
        screen_width = self.display.get_width()
        start_x = screen_width  # Start just off the right side of the screen

        for _ in range(num_mobs):
            mob = Mob(screen_width=screen_width, initial_y=initial_y, initial_x=start_x)
            self.mobs.add(mob)
            start_x += mob.rect.width + spacing # This would space additional mobs off the screen; adjust logic as needed for your design
        
    def run(self):
        self.current_frame += 1
        keys = pygame.key.get_pressed()

        # Clear the display at the start of each frame
        self.display.fill((0, 0, 0))  # Fill the screen with black before redrawing the background

        if keys[pygame.K_d] and self.scroll_frames_remaining > 0:
            self.scroll -= self.scroll_speed
            if self.scroll <= -self.background_width:
                self.scroll += self.background_width  # This ensures continuous scrolling
            self.scroll_frames_remaining -= 2

        # Corrected logic for scrolling left
        elif keys[pygame.K_a] and self.scroll_frames_remaining > 0:
            self.scroll += self.scroll_speed
            if self.scroll >= 0:  # Adjust for leftward scrolling
                self.scroll -= self.background_width
            self.scroll_frames_remaining -= 2

        # Render the background tiles
        for i in range(self.tiles):
            self.display.blit(self.background, (i * self.background_width + self.scroll, 0))

        # Mob spawning, updating, and drawing
        if self.spawn_index < len(self.spawn_frames) and self.current_frame >= self.spawn_frames[self.spawn_index]:
            self.spawn_mobs()
            self.spawn_index += 1

        # Update and draw mobs
        self.mobs.update()  # This calls the update method on all sprite objects in the group
        # Draw mobs
        
        for mob in self.mobs:
            self.display.blit(mob.image, (mob.rect.x + self.scroll, mob.rect.y))

        # Remove dead mobs
        for mob in self.mobs:
            if mob.is_dead:
                mob.kill()





















        









