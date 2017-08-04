import pygame

class Model(object):
    '''
    classdocs
    '''


    def __init__(self, controller):
        '''
        Constructor
        '''
        self.controller = controller
        
    def update(self) -> bool:
        self.controller.get()
        return not self.controller.quit