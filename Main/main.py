import pygame
import sys
from title import Menu
from levels.level1 import Level1
from soundtrack import soundtrack


FPS = 45

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500,600), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('menu')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.start = Start(self.screen, self.gameStateManager)
        self.level1 = Level1(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'menu': self.menu, 'level1': self.level1}
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
            current_state = self.gameStateManager.get_state()
            if current_state == 'menu':
                # Call the main_menu method of Menu
                self.menu.main_menu()  
            else:
                # Call the run method for other states
                self.states[current_state].run()  

            pygame.display.update()
            self.clock.tick(FPS)
            

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.font = pygame.font.Font(None, 36)
        # Pass gameStateManager to the Menu
        self.menu = Menu(self.display, self.gameStateManager)

    def run(self):
        self.display.fill('red')
        text_surface = self.font.render('Press E to start', True, (255, 255, 255))  # Render white text
        text_rect = text_surface.get_rect(center=(750, 300))  # Position the text in the center
        self.display.blit(text_surface, text_rect)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('level1')
            soundtrack('Main/music/xDeviruchi - Exploring The Unknown.wav')
        if self.gameStateManager.get_state() == 'menu':
            self.menu.main_menu()
        elif self.gameStateManager.get_state() == 'level1':
            # Logic for starting level 1
            pass
 
                      
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

    
if __name__ == '__main__': 
    soundtrack('Main/music/Title Theme.wav')
    game = Game()
    game.run()

