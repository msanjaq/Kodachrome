import pygame

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, player):
        '''
        Constructor
        '''
        self.quit   = False
        self.player = player
        
        
    def get(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.left()

                if event.key == pygame.K_RIGHT:
                    self.player.right()

                if event.key == pygame.K_ESCAPE:
                    self.quit = True
            
            elif event.type == pygame.KEYUP:
                self.player.stop()