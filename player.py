'''
Created on Aug 3, 2017

@author: Moe Sanjaq
'''
import pygame

class Player(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    speed = 10
    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image    = pygame.Surface((10,30))
        self.image.fill((255,255,255))

        self.rect   = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

        self.change_x = 0
        self.change_y = 0
        
    
    def left(self):
        self.change_x = -Player.speed
        
    def right(self):
        self.change_x = +Player.speed
    
    def stop(self):
        self.change_x = 0
    
    def update(self):
        self.rect.x += self.change_x
        
    
        