import pygame

class View(object):
    '''
    classdocs
    '''


    def __init__(self, model, height=800, width=400):
        '''
        Constructor
        '''
        self.model  = model
        self.screen = pygame.display.set_mode([height,width])
        print(type(self.screen))
    
    def run(self):
        clock = pygame.time.Clock()
        
        while self.model.update():
            self.screen.fill((0,0,0))
            for sprite in self.model.sprite_group:
                self.screen.blit(sprite.image, sprite.rect.topleft)
            clock.tick(60)
            pygame.display.update()
