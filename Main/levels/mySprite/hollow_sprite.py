import pygame
import os 

#Load Images

sprite_idle = pygame.image.load("main_character.png").convert_alpha()
sprite_active = pygame.image.load("main_character2.png").convert_alpha()

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, image, screen_width=700, screen_height=1500, initial_y=0, initial_x=100):
        super().__init__()
        #image is passed as parameter, must be loaded in main
        if image == 1:
            self.image = sprite_idle
        else:
            self.image = sprite_active
        self.rect = self.image.get_rect()
        #Creates the rectangle for the sprite
        #This will be the area of collision
        #coordinates of top left corner.

        self.rect.x = initial_x
        self.rect.y = initial_y
        
        #Alternate image load #must take 'image' out of parameters.
            #could be useful for animations: swiching file path for image loads.
        #current_path = os.path.dirname(__file__)  # Current file directory
        #image_path = os.path.join(current_path, "level1_mob.png")
        #self.image = pygame.image.load(image_path).convert_alpha()
        #self.rect = self.image.get_rect()

        self.gravity = .5 # Gravity effect
        self.jump_force = -12 # Initial force for jumps
        self.vertical_speed = 0 # current vertical speed
        
        self.speed_x = 0.0  # Horizontal speed
                            # Start at rest
       
        
        self.direction_x = 1  # 1 for right, -1 for left
        self.direction_y = -1  # 1 for down, -1 for up
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.jump_max = screen_height-80  # this set a max limt for the mob to jump to


        
@staticmethod
def drawHollow(display, initial_y, initial_x):
        #hollow_png is the color option of the user.
        #dd as parameter.
        screen_width = display.get_width()
        screen_height = display.get_height()
        # define Group: 
        sprites = pygame.sprite.Group()
        
        for _ in range(num_mobs):
            # initial_x calculation
            initial_x = random.randint(0, screen_width)
            hollow = Sprite(screen_width=screen_width, screen_height=screen_height, initial_y=initial_y, initial_x=initial_x)
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
        
