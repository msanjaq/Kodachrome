'''
Created on Aug 12, 2017

@author: Moe Sanjaq
'''

from enum import Enum, unique

import pygame

@unique
class PowerUpColors(Enum):
    WHITE  = (255,255,255)
    ORANGE = (255,165,0  )

class PowerUp(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self, x: float, y: float, 
                 width: float, height: float, 
                 color: PowerUpColors):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.image  = pygame.Surface((width, height))
        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color.value)
        
        self.color = color

if __name__ == "__main__":
    PowerUp(10,10,10,10, PowerUpColors.ORANGE)
    
        
        
        
        