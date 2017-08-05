import pygame

class Platform(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self, x, y, width, height, color=(0,255,0)):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image  = pygame.Surface([width, height])
        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)