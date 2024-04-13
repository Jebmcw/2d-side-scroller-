
import pygame
#"Main/Level1_img/weapons/18.png"
class Sword():
    def __init__(self,display,freddy):
        super().__init__()
        
        self.display = display
        self.freddy = freddy
        self.sword_img = pygame.image.load("Main/Level1_img/weapons/18.png").convert_alpha()
        self.scaled_width = 20  # Desired width after scaling
        self.scaled_height =90  # Desired height after scaling
        
        self.sword_img1 = pygame.transform.scale(self.sword_img, (self.scaled_width, self.scaled_height))
        self.sword_rect = self.sword_img.get_rect()
        print('Sword dimensions: ', self.sword_rect.width, ',', self.sword_rect.height)
        self.sword_img2 = pygame.transform.rotate(self.sword_img1, 270)
        self.sword_img3 = pygame.transform.rotate(self.sword_img1, 240)
        self.sword_img4 = pygame.transform.rotate(self.sword_img1,225)
        self.sword_img5 = pygame.transform.rotate(self.sword_img1,210)
        self.sword_img6 = pygame.transform.rotate(self.sword_img1,180)
        self.SwordFrame = 0
        
        
   
    
    
    
    def update(self):
        pass
        