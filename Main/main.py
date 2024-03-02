import pygame
import sys
from levels.level1 import Level1
from soundtrack import soundtrack
FPS = 40

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500,600))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level1 = Level1(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'level1': self.level1}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)
            

class Start:
    def __init__(self,display, gameStateManager):
        self.display=display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('level1')
            
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

    
if __name__ == '__main__': 
    soundtrack()
    game = Game()
    game.run()

