import pygame
import os

class Mob(pygame.sprite.Sprite):
    def __init__(self, screen_width=700, initial_y=0, initial_x=None):  # Assume screen_width is passed or preset
        super().__init__()
        current_path = os.path.dirname(__file__)  # Current file directory
        image_path = os.path.join(current_path, "level1_mob.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(x=initial_x, y=initial_y)
        self.speed_x = .9  # Horizontal speed
        self.direction = 1  # -1 for left
        self.screen_width = screen_width
        self.is_dead = False

        if initial_x is None:
            initial_x = self.screen_width  # Start at the right edge of the screen
        self.rect.x = initial_x
        self.rect.y = initial_y

    def update(self):
        
    # Move mob based on direction and speed
        self.rect.x += self.speed_x * self.direction

    # Check boundaries and reverse direction if hitting screen edges
        if self.rect.left < -1:  # If mob goes past the left edge
            self.rect.left = -1  # Position it at the left edge
            self.direction *= -1  # And reverse direction to move right
        elif self.rect.right > self.screen_width:  # If mob goes past the right edge while moving back
            self.rect.right = self.screen_width  # Position it at the right edge
            self.direction *= -1  # And reverse direction to move left again


        # Check if mob has moved off the left side of the screen
        if self.rect.right < 0:
            self.is_dead = True
        # Check if mob has moved off the right side of the screen
        if self.rect.left > self.screen_width:
            self.is_dead = True


        
        



