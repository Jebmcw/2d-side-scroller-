import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,imageChoice, screen_width = 700, screen_height=1500, initial_x = 150, initial_y = 450):
        super().__init__()
        #Current file directory
        current_path = os.path.dirname(__file__)
        #Load image file path
        if imageChoice == 1:
            image_path = os.path.join(current_path, "main_character.png")
        elif imageChoice == 2:
            image_path = os.path.join(current_path, "main character 2nd option.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        #Creates the rectangle for the sprite
        #This will be the area of collision
        #coordinates of top left corner.
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.initial_y = initial_y
        self.verticalSpeed = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.jump_max = screen_height - 80
        self.parabolaX = 0
        self.gravity = .5
        self.health = 100
        
    @staticmethod
    def spawnPlayer(display, imageNum, initial_x, initial_y):
        screen_width = display.get_width()
        screen_height = display.get_height()
        player = Player(imageNum, screen_width, screen_height+500, initial_x, initial_y)
        players = pygame.sprite.Group()
        players.add(player)    
        return players
    
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
        #self.verticalSpeed += self.gravity
        #self.rect.y += self.verticalSpeed

