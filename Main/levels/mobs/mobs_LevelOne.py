import pygame
import os
import random  # Import the random module

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Mob(pygame.sprite.Sprite):
    def __init__(self, screen_width=700, screen_height=1500, initial_y=0, initial_x=None):
        super().__init__()
        current_path = os.path.dirname(__file__)  # Current file directory
        image_path = os.path.join(current_path, "level1_mob.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        
        # Set initial positions
        if initial_x is None:
            initial_x = screen_width // 2  # Start at the middle of the screen
        self.rect.x = initial_x
        self.rect.y = initial_y
        
        self.gravity = .5 # Gravity effect
        self.jump_force = -10 # Initial force for jumps
        self.vertical_speed = 0 # current vertical speed
        
        self.speed_x = 0.55  # Horizontal speed
       
        
        self.direction_x = 1  # 1 for right, -1 for left
        self.direction_y = -1  # 1 for down, -1 for up
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.jump_max = screen_height-100  # this set a max limt for the mob to jump to
        
        self.health = 100  # Max health
        
    @staticmethod
    def draw_health_bar(display, mob,scroll):
        # Health bar drawing
        health_percentage = mob.health / 100
        bar_width = 50
        bar_height = 10
        fill = bar_width * health_percentage
        outline_rect = pygame.Rect(mob.rect.x+scroll+60, mob.rect.y - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(mob.rect.x+scroll+60, mob.rect.y - 10, fill, bar_height)
        
        pygame.draw.rect(display, (255, 0, 0), outline_rect)  # Red background
        pygame.draw.rect(display, (0, 255, 0), fill_rect)  # Green foreground
        pygame.draw.rect(display, (255, 255, 255), outline_rect, 2)  # White border    
          
    @staticmethod
    def spawn_mobs_horizontally(display, num_mobs, initial_y, spacing=0):
        screen_width = display.get_width()
        screen_height = display.get_height()
        mobs = pygame.sprite.Group()
        
        for _ in range(num_mobs):
            # initial_x calculation
            initial_x = random.randint(0, screen_width)
            mob = Mob(screen_width=screen_width, screen_height=screen_height, initial_y=initial_y, initial_x=initial_x)
            mobs.add(mob)
            
        return mobs

    def update(self):
        
        # speed based on direction
        self.rect.x += self.speed_x * self.direction_x
        
        # Apply gravity
        self.vertical_speed += self.gravity
        self.rect.y += self.vertical_speed
        
        if self.rect.right > self.screen_width-500:  # If mob hits the right edge of the screen
            self.rect.right = self.screen_width-500
            self.direction_x *= -1  # Reverse direction
            
        elif self.rect.left < 0:  # If mob hits the left edge of the screen
            self.rect.left = 0
            self.direction_x *= -1  # Reverse direction
            
        # Boundary checks and jumping logic
        if self.rect.bottom > self.jump_max:
            self.rect.bottom = self.jump_max
            self.vertical_speed = self.jump_force  # Apply jump force to simulate a bounce
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vertical_speed = 0  # Stop upward movement
        


       




        
        



