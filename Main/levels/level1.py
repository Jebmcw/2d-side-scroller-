import pygame
import time

from levels.mobs.mobs_LevelOne import Mob
from main_character.player import Player
from levels.backgrounds.background import Background


class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.mobs = pygame.sprite.Group()  # Corrected from a list to a sprite group
        
        # Initialize Background with the display
        self.bg = Background(self.display)
        
        # Frame rate and timing for spawns
        self.FPS = 25
        self.start_time = time.time()
        self.spawn_intervals = [1, 19, 20, 10] # seconds between spawns
        self.next_spawn_time = self.spawn_intervals[0]
        self.spawn_index = 0

        #initialize main character pos and jumps
        self.jumpCount = 0
        self.jump = 0
        self.player_x = 150
        self.player_y = 450
        self.alive = False
        self.mainCharacter = pygame.sprite.Group()


    def spawn_mobs(self):
        # use the static method from Mob class
        mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 2, 350, 50)
        self.mobs.add(*mobs_to_add)
        
    
            
    def run(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        keys=pygame.key.get_pressed()
        
        # Draw the background first
        self.bg.draw_bg()
        
        if self.alive == False:
            #Create Player Sprite
            live = Player.spawnPlayer(self.display, 1, self.player_x, self.player_y)
            self.mainCharacter.add(*live)
            self.alive = True
            

        #Jump button is 'w':
        if keys[pygame.K_w] and self.player_y == self.player_y == 450:
            print('jump')
            self.jump = 1

            
        if elapsed_time >= self.next_spawn_time:
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
            Mob.draw_health_bar(self.display, mob, self.bg.scroll)
            
       
        #Update and draw player
        if self.jump == 1:
            self.mainCharacter.update()
            self.jumpCount += 1
        if self.jumpCount >= 60:
            self.jump = 0
            self.jumpCount = 0
            for player in self.mainCharacter:
                player.rect.y = player.initial_y
                
        for player in self.mainCharacter:
            self.display.blit(player.image, (player.rect.x, player.rect.y))
            Player.draw_health_bar_player(self.display, player,100)

















        









