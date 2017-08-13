'''
Created on Aug 13, 2017

@author: Moe Sanjaq
'''

from .gravity_sprite import GravitySprite

class SimpleEnemy(GravitySprite):
    '''
    classdocs
    '''


    def __init__(self, x, y, width, height):
        '''
        Constructor
        '''
        GravitySprite.__init__(self, x, y, width, height)
        self.image.fill((165,42,42))


if __name__ == "__main__":
    SimpleEnemy().update()