
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
        self.sword_img1 = pygame.transform.rotate(self.sword_img1, 270)
        self.sword_rect = self.sword_img.get_rect()
        print('Sword dimensions: ', self.sword_rect.width, ',', self.sword_rect.height)
        
        '''
        self.sword_img2 = pygame.transform.rotate(self.sword_img1, 270)
        self.sword_img3 = pygame.transform.rotate(self.sword_img1, 240)
        self.sword_img4 = pygame.transform.rotate(self.sword_img1,225)
        self.sword_img5 = pygame.transform.rotate(self.sword_img1,210)
        self.sword_img6 = pygame.transform.rotate(self.sword_img1,180)
        self.SwordFrame = 0
        '''
        
   
    
    
    
    def update(self,keys):
        sword_x_offset = -10  # Adjust so the sword appears correctly relative to Freddy
        sword_y_offset = 20  # Adjust based on your game's needs
    
        sword_position = (self.freddy.rect.x + sword_x_offset, self.freddy.rect.y + sword_y_offset)
        
        # Update the rect for the sword image after transformations
        self.sword_img1_rect = self.sword_img1.get_rect(topleft=sword_position)
        
        if keys[pygame.K_LSHIFT]: 
            self.display.blit(self.sword_img1,self.sword_img1_rect.topleft)
                
        