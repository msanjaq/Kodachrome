import sys

import pygame

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, player):
        '''
        Constructor
        '''
        self.player = player
        
        self.controls = {
            pygame.KEYDOWN : { 
                pygame.K_LEFT    : self.player.left ,
                pygame.K_RIGHT   : self.player.right,
                pygame.K_UP      : self.player.jump ,
                pygame.K_ESCAPE  : sys.exit
                },
            
            pygame.KEYUP : {
                pygame.K_LEFT   : self.player.stop_left,
                pygame.K_RIGHT  : self.player.stop_right 
                }
        }

    def get(self) -> None:
        for event in pygame.event.get():
            if self._is_valid_event(event):
                self.controls[event.type][event.key]()
    
    def _is_valid_event(self, event) -> bool:
        return (event.type in self.controls 
               and event.key in self.controls[event.type])