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
        self.speed = 5
        
    @staticmethod
    def spawnPlayer(display, imageNum, initial_x, initial_y):
        screen_width = display.get_width()
        screen_height = display.get_height()
        player = Player(imageNum, screen_width, screen_height+500, initial_x, initial_y=350)  
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


        lines = text.split('\n')
        max_width = 0
        text_surfs = []


        for line in lines:
            text_surf = font.render(line, True, text_color)
            text_surfs.append(text_surf)
            if text_surf.get_width() > max_width:
                max_width = text_surf.get_width()


        total_height = sum(text_surf.get_height() for text_surf in text_surfs) + padding * (len(text_surfs) - 1)


        box_rect = pygame.Rect(0, 0, max_width + padding * 2, total_height + padding * 2)
        box_rect.center = (player.rect.centerx, player.rect.y - offset_y - total_height // 2 - padding)


        box_surface = pygame.Surface(box_rect.size, pygame.SRCALPHA)
        box_surface.fill(box_color)


        display.blit(box_surface, box_rect.topleft)


        current_y = box_rect.y + padding
        for text_surf in text_surfs:
            text_rect = text_surf.get_rect(center=(box_rect.centerx, current_y + text_surf.get_height() // 2))
            display.blit(text_surf, text_rect)
            current_y += text_surf.get_height() + padding
    
   
   
   
    def jump(self):
        #Jump curve
        factor = self.parabolaX - 30
        square = factor*factor
        coefficient = float(square)*0.2
        jump_height = int(coefficient)-180
        self.rect.y = self.initial_y + jump_height
        self.parabolaX += 1
        if self.parabolaX >= 60:
            self.parabolaX = 0
            
    def player_movements(self, keys):
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))

    