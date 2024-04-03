import pygame
import os
#testing branches on gitkraken.
class Player(pygame.sprite.Sprite):
    def __init__(self,imageChoice, screen_width = 700, screen_height=1500, initial_x = 150, initial_y = 450):
        super().__init__()
        #Current file directory
        current_path = os.path.dirname('assets')
        #Load image file path
        if imageChoice == 1:
            self.image = pygame.image.load('assets/main_character.png').convert_alpha()
        elif imageChoice == 2:
            self.image = pygame.image.load('assets/main character 2nd option.png').convert_alpha()
        self.rect = self.image.get_rect()
        #Creates the rectangle for the sprite
        #This will be the area of collision
        #coordinates of top left corner.
        self.width = self.image.get_width
        self.height = self.image.get_height
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.initial_y = initial_y
        self.verticalSpeed = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.jump_max = screen_height - 80
        self.parabolaX = 0
        
        self.health = 100
        
    @staticmethod
    def spawnPlayer(display, imageNum, initial_x, initial_y):
        screen_width = display.get_width()
        screen_height = display.get_height()
        player = Player(imageNum, screen_width, screen_height+500, initial_x, initial_y)  
        return player
    
    @staticmethod
    def draw_health_bar_player(display, player,scroll):
        # Health bar drawing
        health_percentage = player.health / 100
        bar_width = 50
        bar_height = 10
        fill = bar_width * health_percentage
        outline_rect = pygame.Rect(player.rect.x-scroll+ 150, player.rect.y -20, bar_width, bar_height)
        fill_rect = pygame.Rect(player.rect.x-scroll+ 150, player.rect.y - 20, fill, bar_height)
        
        pygame.draw.rect(display, (255, 0, 0), outline_rect)  # Red background
        pygame.draw.rect(display, (0, 255, 0), fill_rect)  # Green foreground
        pygame.draw.rect(display, (255, 255, 255), outline_rect, 2)  # White border 
   
    @staticmethod       
    def draw_text_box(display, player, text, font_size=24, text_color=(255, 255, 255), box_color=(0, 0, 0, 128), padding=10, offset_y=50):
        font = pygame.font.Font(None, font_size)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=(player.rect.centerx, player.rect.y - offset_y))

        # Calculate box dimensions based on text dimensions + padding
        box_rect = text_surf.get_rect()
        box_rect.inflate_ip(padding * 2, padding * 2)  # Inflate the rect to add padding around the text
        box_rect.center = (player.rect.centerx, player.rect.y - offset_y - text_rect.height // 2 - padding)

        # Create a semi-transparent surface for the text box background
        box_surface = pygame.Surface(box_rect.size, pygame.SRCALPHA)
        box_surface.fill(box_color)

        # Blit the semi-transparent surface onto the display first
        display.blit(box_surface, box_rect.topleft)
        # Then blit the text onto the display, centered within the text box
        display.blit(text_surf, text_rect)
   
   
   
    def update(self):
        #Jump curve
        factor = self.parabolaX - 30
        square = factor*factor
        coefficient = float(square)*0.144
        jump_height = int(coefficient)-130
        self.rect.y = self.initial_y + jump_height
        self.parabolaX += 1
        if self.parabolaX >= 60:
            self.parabolaX = 0

    