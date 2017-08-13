import pygame

class GravitySprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    gravity = 1
    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        