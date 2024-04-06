import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, screen_width=600, screen_height=1500, initial_y=0, initial_x=None):
        super().__init__()
        self.image = pygame.image.load("Main/Level1_img/boss/first_boss.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        
        # Set initial positions
        if initial_x is None:
            initial_x = screen_width // 10  # Start at the middle of the screen
        self.rect.x = initial_x
        self.rect.y = initial_y
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.gravity = 0.5  # Gravity effect
        self.jump_force = -15  # Initial force for jumps
        self.vertical_speed = 0  # Current vertical speed
        
        self.speed_x = 1  # Horizontal speed
        
        self.direction_x = -1  # 1 for right, -1 for left
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.jump_max = screen_height-100  # this set a max limt for the mob to jump to
        
          
    @staticmethod
    def spawn_boss_horizontally(display, num_mobs, initial_y, spacing, x_offset=0):
        screen_width, screen_height = display.get_size()
        bosses = pygame.sprite.Group()
        initial_y = 450
        for i in range(num_mobs):
            initial_x = (i * spacing) + x_offset
            boss = Boss(screen_width=screen_width, screen_height=screen_height, initial_y=initial_y, initial_x=initial_x)
            bosses.add(boss)
        return bosses
    
    @staticmethod
    def draw_health_bar(display, bosses, scroll):
        # Example health bar properties
        BAR_WIDTH = 50
        BAR_HEIGHT = 10
        border_color = (0, 0, 0)  # Black
        fill_color = (255, 0, 0)  # Red
    
        # Calculate health bar position
        # Let's assume the health bar is drawn directly above the mob sprite
        bar_x = bosses.rect.x+50 - scroll  # Adjust mob's X position with scroll value
        bar_y = bosses.rect.y - 7  # Positioned 10 pixels above the mob
    
        # Draw the health bar
        pygame.draw.rect(display, border_color, (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT), 1)  # Border
        pygame.draw.rect(display, fill_color, (bar_x + 1, bar_y + 1, BAR_WIDTH - 2, BAR_HEIGHT - 2))  # Fill 



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