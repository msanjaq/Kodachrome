'''
Created on Aug 3, 2017

@author: Moe Sanjaq
'''
import pygame
from .platform import Platform


class Player(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    speed = 5
    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image    = pygame.Surface((10,30))
        self.image.fill((255,255,255))

        self.rect   = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

        self.dx = 0
        self.dy = 0
        
    def jump(self):
        if self.dy in {0,18,19,20}:
            self.dy = -20
    
    def left(self):
        self.dx = -Player.speed
        
    def right(self):
        self.dx = +Player.speed
    
    def stop_left(self):
        if self.dx == -Player.speed:
            self.dx = 0
    
    def stop_right(self):
        if self.dx == Player.speed:
            self.dx = 0
    
    def update(self):
        self._calc_gravity()

        self.rect.x += self.dx
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dx > 0:
                    self.rect.right  = sprite.rect.left

                elif self.dx < 0:
                    self.rect.left   = sprite.rect.right
        
        
        self.rect.y += self.dy
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dy > 0:
                    self.rect.bottom = sprite.rect.top
                
                elif self.dy < 0:
                    self.rect.top    = sprite.rect.bottom
                
                self.dy = 0

    def _calc_gravity(self):
        self.dy += 1

    def _get_collisions(self):
        for group in self.groups():
            collisions = pygame.sprite.spritecollide(self, group, False)
            return collisions
        
    
        
    
        