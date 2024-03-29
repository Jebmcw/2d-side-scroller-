import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, screen_width=600, screen_height=1500, initial_y=0, initial_x=None):
        super().__init__()
        self.image = pygame.image.load("Main/Level1_img/boss/first_boss.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        
        # Set initial positions
        if initial_x is None:
            initial_x = screen_width // 10  # Start at the middle of the screen
        self.rect.x = initial_x
        self.rect.y = initial_y
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        
          
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




    def update(self):
        
        pass