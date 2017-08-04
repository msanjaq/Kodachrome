import pygame


class Model(object):
    '''
    classdocs
    '''


    def __init__(self, controller):
        '''
        Constructor
        '''
        self.controller   = controller
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(controller.player)
        
    def update(self) -> bool:
        self.controller.get()
        self.sprite_group.update()
        return not self.controller.quit