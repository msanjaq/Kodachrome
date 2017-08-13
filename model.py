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
        self.sprite_group.add(level.mobile_sprites)
        
        self.updateable_sprites = level.mobile_sprites
        self.updateable_sprites.append(level.player)
        
        
    def update(self) -> None:
        self.controller.get()
        #self.sprite_group.update()
        for sprite in self.updateable_sprites:
            sprite.update()