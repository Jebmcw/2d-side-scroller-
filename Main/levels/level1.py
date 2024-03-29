import pygame
import time

from levels.mobs.mobs_LevelOne import Mob
from main_character.player import Player
from levels.backgrounds.background import Background
from levels.Level1_boss.level1_boss import Boss

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.mobs = pygame.sprite.Group()  # Corrected from a list to a sprite group
        self.boss = pygame.sprite.Group()
        
        # Initialize Background with the display
        self.bg = Background(self.display)
        
        # Frame rate and timing for spawns
        self.FPS = 45
        self.start_time = time.time()
        self.spawn_intervals = [1, 5, 9, 12, 14] # seconds between spawns
        self.next_spawn_time = self.spawn_intervals[0]
        self.spawn_index = 0

        #initialize main character pos and jumps
        self.jumpCount = 0
        self.jump = 0
        self.player_x = 150
        self.player_y = 450
        self.alive = False
        self.mainCharacter = pygame.sprite.Group()
        self.some_additional_offset = 100

    def spawn_mobs(self):
        dynamic_offset = 0
        if self.spawn_intervals[self.spawn_index] ==1:
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
            
        if self.spawn_intervals[self.spawn_index] == 9:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 10")
            
        if self.spawn_intervals[self.spawn_index] == 12:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 12")
            
        if self.spawn_intervals[self.spawn_index] == 14:
            self.some_additional_offset = 500
            dynamic_offset = self.bg.scroll + self.some_additional_offset
            mobs_to_add = Mob.spawn_mobs_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.mobs.add(*mobs_to_add)
            print("Mob spawned : 14")
            
    def spawn_boss(self):
        if self.bg.scroll == 8000:
            dynamic_offset = 10000
            boss_to_add = Boss.spawn_boss_horizontally(self.display, 1, 500, 50, dynamic_offset)
            self.boss.add(boss_to_add)
            print("boss spawned")
               
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
            #print('jump')
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
         
        self.spawn_boss()   
        self.boss.update()
        for boss in self.boss:
            self.display.blit(boss.image, (boss.rect.x-self.bg.scroll, boss.rect.y))
            
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

















        









