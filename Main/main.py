import pygame
import sys
from title import Menu
from levels.level1 import Level1


FPS = 30

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500,600))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('menu')
        self.start = Start(self.screen, self.gameStateManager)
        self.menu = Menu(self.screen)
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
         # Initialize Menu
        self.menu = Menu(self.display)
    def run(self):
        if self.gameStateManager.get_state() == 'menu':
            # The Menu class handles displaying the title screen
            self.menu.main_menu()
        elif self.gameStateManager.get_state() == 'level1':
            # Here, you might clear the screen and start the level1 game logic
            # If level1 has its own background, you might not need to fill the screen with a solid color here
            pass
            
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

    
if __name__ == '__main__': 
    game = Game()
    game.run()

