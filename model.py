import pygame


class Model(object):
    '''
    classdocs
    '''


    def __init__(self, level, controller_type):
        '''
        Constructor
        '''
        self.controller = controller_type(level.player)

        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(level.player)
        self.sprite_group.add(level.platform_list)
        
    def update(self) -> None:
        self.controller.get()
        self.sprite_group.update()