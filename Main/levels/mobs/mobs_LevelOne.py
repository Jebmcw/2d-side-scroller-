
import pygame

# Assuming you've initialized pygame and set up a display beforehand
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Mob(pygame.sprite.Sprite):
    def __init__(self, screen_width=600, screen_height=1500, initial_y=None, initial_x=None):
        super().__init__()
        self.image = pygame.image.load("Main/Level1_img/mob/level1_mob.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        # Set initial positions. If no initial_x is provided, start at the screen's 10%.
        # For initial_y, if not provided, place it 50 pixels above the bottom.
        if initial_x is None:
            initial_x = screen_width // 10
        if initial_y is None:
            initial_y = screen_height - 50  # Adjust to spawn closer to the bottom

        self.rect.x = initial_x
        self.rect.y = initial_y
        
        self.gravity = 0.5  # Gravity effect
        self.jump_force = -10  # Initial force for jumps
        self.vertical_speed = 0  # Current vertical speed
        
        self.speed_x = 0.55  # Horizontal speed
        
        self.direction_x = -1  # 1 for right, -1 for left
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.jump_max = screen_height-100  # this set a max limt for the mob to jump to
        
        self.health = 100  # Max health
        
    @staticmethod
    def draw_health_bar(display, mob, scroll):
        # Example health bar properties
        BAR_WIDTH = 50
        BAR_HEIGHT = 10
        border_color = (0, 0, 0)  # Black
        fill_color = (255, 0, 0)  # Red
    
        # Calculate health bar position
        # Let's assume the health bar is drawn directly above the mob sprite
        bar_x = mob.rect.x+65 - scroll  # Adjust mob's X position with scroll value
        bar_y = mob.rect.y - 10  # Positioned 10 pixels above the mob
    
        # Draw the health bar
        pygame.draw.rect(display, border_color, (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT), 1)  # Border
        pygame.draw.rect(display, fill_color, (bar_x + 1, bar_y + 1, BAR_WIDTH - 2, BAR_HEIGHT - 2))  # Fill 
          
    @staticmethod
    def spawn_mobs_horizontally(display, num_mobs, initial_y, spacing, x_offset=0):
        screen_width = display.get_width()
        screen_height = display.get_height()
        mobs = pygame.sprite.Group()
        initial_y = screen_height - 50
        for i in range(num_mobs):
            initial_x = (i * spacing) + x_offset  # Use the dynamic offset here
        # Ensure mobs spawn within the intended area, adjusting as necessary
            mob = Mob(screen_width=screen_width, screen_height=screen_height, initial_y=initial_y, initial_x=initial_x)
            mobs.add(mob)

        return mobs




    def update(self):
        
        # speed based on direction
        self.rect.x += self.speed_x * self.direction_x
        
        # Apply gravity
        self.vertical_speed += self.gravity
        self.rect.y += self.vertical_speed
            
        # Boundary checks and jumping logic
        if self.rect.bottom > self.jump_max:
            self.rect.bottom = self.jump_max
            self.vertical_speed = self.jump_force  # Apply jump force to simulate a bounce
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vertical_speed = 0  # Stop upward movement
        


       




        
        



