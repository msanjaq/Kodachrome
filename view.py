import pygame


class View(object):
    '''
    classdocs
    '''

    width = 800
    height = 800

    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.screen = pygame.display.set_mode([View.width, View.height])

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.model.update()
            self.screen.fill((0, 0, 0))

            for sprite in self.model.sprite_group:
                self.screen.blit(sprite.image, sprite.rect.topleft)

            clock.tick(60)
            pygame.display.update()
