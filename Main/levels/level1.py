import pygame
import time
import os
from levels.platforms.platforms import TileMap
from levels.mobs.mobs_LevelOne import Mob
from main_character.player import Player
from levels.backgrounds.background import Background
from levels.Level1_boss.level1_boss import Boss
from Voice import Voice 
from soundtrack import soundtrack
from weapons.fireball import Fireball

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        
        self.mobs = pygame.sprite.Group()  # Corrected from a list to a sprite group
        self.boss = pygame.sprite.Group()
        
        # Initialize Background with the display
        self.bg = Background(self.display)
        
        self.lines = "In a mystical realm, a hero embarks \non a quest to recover ancient artifacts,\n battling foes and unraveling mysteries\n to restore harmony to the land."
        # Frame rate and timing for spawns
        self.start_time = time.time()
        self.spawn_intervals = [3, 5, 6, 9, 10] # seconds between spawns
        self.next_spawn_time = self.spawn_intervals[0]
        self.spawn_index = 0
        
         # Timing for text box display
        self.text_box_start_time = 1  # Displaying the text box 1 second into the game
        self.text_box_end_time = 10  # Stop displaying the text box 6 seconds into the game
        self.text_displayed = False  # Flag

        #audio for the text
        self.audio_start_time = self.text_box_start_time
        self.audio_end_time = self.text_box_end_time
        
        self.audio_displayed = False  

        current_path = os.path.dirname(__file__)
        # Initialize the TileMap
        csv_file_path = "Main/levels/platforms/level 1 tile map.csv"
        self.tile_map = TileMap(csv_file_path, tile_size=32)  # Adjust as needed

        #initialize main character pos and jumps
        self.jumpCount = 0
        self.jump = 0
        self.player_x = 300
        self.player_y = 390
        self.alive = True
        self.freddy = Player.spawnPlayer(self.display, 2, 300, 390)
        print('freddy dimensions: ', self.freddy.rect.width, ', ', self.freddy.rect.height)

        #initialize power up fireball to collect
        self.powerUp_img = pygame.image.load('assets/fireball.png').convert_alpha()
        self.scaled_width = 50  # Desired width after scaling
        self.scaled_height = 50  # Desired height after scaling
        self.powerUp_img1 = pygame.transform.scale(self.powerUp_img, (self.scaled_width, self.scaled_height))
        self.powerUp_rect = self.powerUp_img1.get_rect()
        print('Power Up dimensions: ', self.powerUp_rect.width, ',', self.powerUp_rect.height)
        self.powerUp_img2 = pygame.transform.flip(self.powerUp_img1, 0, 90)
        self.powerUp_img3 = pygame.transform.flip(self.powerUp_img1, 90, 90)
        self.powerUp_img4 = pygame.transform.flip(self.powerUp_img1, 90, 0)
        self.fireFrame = 0
        # Original dimensions of the image
        # original_width, original_height = self.powerUp_img.get_width(), self.powerUp_img.get_height()
        # print(original_width, ", ", original_height, '\n')
        # Scale the image
        


        self.some_additional_offset = 100

        self.bossFightTextShown = False
        
    def spawn_mobs(self):
        dynamic_offset = 0
        if self.spawn_intervals[self.spawn_index] == 3:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 400, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 1")
        if self.spawn_intervals[self.spawn_index] == 5:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 5")
            
        if self.spawn_intervals[self.spawn_index] == 6:
            self.some_additional_offset = 500
            soundtrack('Main/music/xDeviruchi - Exploring The Unknown.wav')
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 8")
            
        if self.spawn_intervals[self.spawn_index] == 9:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 9")
            
        if self.spawn_intervals[self.spawn_index] == 10:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 10")
            
    def spawn_boss(self):
        font = pygame.font.SysFont('arial', 100)  # Specify the font name and size.
        text_color = (255, 0, 0)  # Red color

        if self.bg.scroll == 8000:
            dynamic_offset = 10000
            boss_to_add = Boss.spawn_boss_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.boss.add(boss_to_add)
            
        if self.bg.scroll >8000 and self.bg.scroll <= 9000 and not self.bossFightTextShown:
            text_surface = font.render('Boss Fight!!!', True, text_color)
            self.display.blit(text_surface, (450, 150))  # Position of the text

    #def spawn_powerUp(self):
        #make the png a sprite and scale and blit to screen
                
                      
            
    def update_timer(self):
        self.font = pygame.font.Font(None, 36)
    # Calculate elapsed time
        if self.gameStateManager.start_time is not None:
            current_time = time.time()
            elapsed_time = current_time - self.gameStateManager.start_time
        
            # Format as minutes:seconds
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            timer_text = f"{minutes:02d}:{seconds:02d}"
        
            # Render the text
            text_surface = self.font.render(timer_text, True, (255, 255, 255))  # White text
            text_rect = text_surface.get_rect(topright=(1420, 20))  # Position it at the top right
        
            # Blit the text surface onto the screen
            self.display.blit(text_surface, text_rect)
                  
    def run(self):
        self.display.fill((0, 0, 0))
        pygame.draw.rect(self.display, (255, 0, 0), (50, 50, 100, 100))  # Draw a red rectangle
        self.tile_map.draw(self.display)
        current_time = time.time()
        #total time since instance of lvl1 was initialized
        elapsed_time = current_time - self.start_time
        game_elapsed_time = current_time - self.start_time


        keys=pygame.key.get_pressed()
        
        # Draw the background first
        self.bg.draw_bg()
        self.bg.draw_ground()
        self.update_timer()
        font = pygame.font.SysFont('Times New Roman',30)
        text_color = (255,255,255)
        text_surface = font.render('Freddy World', True, text_color)
        self.display.blit(text_surface, (0,10))
       

        #Jump button is 'w':
        if keys[pygame.K_w] and self.player_y == 390:
            #print('jump')
            self.jump = 1

        #Timed spawning only works with infinite scroll and infinite scroll doesn't work bc?
            #coordinate spawning would be easier to plan and level would have a set duration till boss fight.
            #less group list creation would be necessary --> cleaner code.    
        if elapsed_time >= self.next_spawn_time:
            #self
            self.spawn_mobs()
            self.spawn_index +=1
            if self.spawn_index < len(self.spawn_intervals):
                self.next_spawn_time += self.spawn_intervals[self.spawn_index]
            else:
                self.next_spawn_time = float('inf') # Stop spawning after last interval
                
        # Update and draw mobs
        self.mobs.update()
        for mob in self.mobs:
            mob_world_x = mob.rect.x - self.bg.scroll
            self.display.blit(mob.image, (mob_world_x, mob.rect.y))
            mob.seeRect(self.bg.scroll)
            pygame.draw.rect(self.display, (255, 0, 0), mob.rect, 2)  # Draw a rectangle around the sprite's rect
            mob.revertX(self.bg.scroll)
            Mob.draw_health_bar(self.display, mob, self.bg.scroll)
         
        self.spawn_boss()   
        self.boss.update()
        for boss in self.boss:
            self.display.blit(boss.image, (boss.rect.x-self.bg.scroll, boss.rect.y))
            Boss.draw_health_bar(self.display, boss, self.bg.scroll)
             
        #Update and draw player
        if self.jump == 1:
            self.freddy.jump()
            self.jumpCount += 1
        if self.jumpCount >= 60:
            self.jump = 0
            self.jumpCount = 0
            self.freddy.rect.y = self.freddy.initial_y

        #Freddy is updated, so spawn the fireball at his pos
            #shoot fireball    
        if keys[pygame.K_f]:
            #spawn fireball into player projectile list
            #update fireball sprite every frame
            #apply gravity until it hits the ground and then make it bounce twice
            #explodes on third bounce or collision
            #remove fireball from the projectiles list
            self.freddy.projectiles.append(Fireball(350, self.freddy.rect.y, True))
        
                
        self.display.blit(self.freddy.image, (self.freddy.rect.x - 58, self.freddy.rect.y - 40))
        pygame.draw.rect(self.display, (0, 255, 0), self.freddy.rect, 2)
        Player.draw_health_bar_player(self.display, self.freddy,100)
        if self.bg.scroll == 10000:
            keys = pygame.key.get_pressed()
            self.freddy.player_movements(keys)
        


        if self.text_box_start_time <= game_elapsed_time <= self.text_box_end_time:
            Player.draw_text_box(self.display, self.freddy,self.lines)
            if not self.audio_displayed:
                Voice('Main/music/AI.mp3')  # Play the audio
                #soundtrack('Main/music/xDeviruchi - Exploring The Unknown.wav')
                self.audio_displayed = True  # Prevent audio from being played again in this session
            self.text_displayed = True  # Keep showing the text box
        else:
            self.audio_displayed = False
        #soundtrack('Main/music/xDeviruchi - Exploring The Unknown.wav')
        #while self.fireAnime == True:
        if self.fireFrame <= 20:
            print('fireball1')
            self.display.blit(self.powerUp_img1, (350, self.freddy.rect.y))
            self.fireFrame += 1
        elif self.fireFrame <= 40:
            print('fireball2')
            self.display.blit(self.powerUp_img2, (350, self.freddy.rect.y))
            self.fireFrame += 1
        elif self.fireFrame <= 60:
            print('fireball3')
            self.display.blit(self.powerUp_img3, (350, self.freddy.rect.y))
            self.fireFrame += 1
        else:
            print('fireball4')
            self.fireFrame += 1
            self.display.blit(self.powerUp_img4, (350, self.freddy.rect.y))
            if self.fireFrame == 80:    
                self.fireFrame = 0

        collisions = pygame.sprite.spritecollide(self.freddy, self.mobs, False)
        #for collided_sprite in collisions:
            #print("Collison!")