import pygame

class View(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        self.model  = model
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    
    def run(self):
        clock = pygame.time.Clock()
        
        while self.model.update():
            clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    import model
    import controller
    v = View(model.Model(controller.Controller()))
    v.run()