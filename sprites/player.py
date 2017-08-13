'''
Created on Aug 3, 2017

@author: Moe Sanjaq
'''
import pygame

from .gravity_sprite    import GravitySprite
from .platform          import Platform
from .powerups          import PowerUpColors, PowerUp
from Kodachrome.sprites import gravity_sprite

class Player(GravitySprite):
    '''
    classdocs
    '''

    speed = 5
    def __init__(self, x, y):
        '''
        Constructor
        '''
        GravitySprite.__init__(self)

        self.image  = pygame.Surface((10,30))
        self.image.fill(PowerUpColors.WHITE.value)

        self.rect   = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

        self.dx = 0
        self.dy = 0
        
        self.color = PowerUpColors.WHITE
        
    def jump(self):
        if self.color == PowerUpColors.ORANGE:
            if self.dy in {0, -18, -19, -20}:
                self.dy = 20

        elif self.dy in {0,18,19,20}:
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
    
    def power(self):
        if self.color == PowerUpColors.ORANGE:
            GravitySprite.gravity = -1 if GravitySprite.gravity == 1 else 1
    
    def update(self):
        self._calc_gravity()
        self._update_x_direction()
        self._update_y_direction()
        self._update_color()
    
    def _calc_gravity(self):
        self.dy += GravitySprite.gravity

    def _get_collisions(self):
        for group in self.groups():
            collisions = pygame.sprite.spritecollide(self, group, False)
            return collisions
    
    def _update_x_direction(self):
        self.rect.x += self.dx
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dx > 0:
                    self.rect.right  = sprite.rect.left

                elif self.dx < 0:
                    self.rect.left   = sprite.rect.right
    
    def _update_y_direction(self):
        self.rect.y += self.dy
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dy > 0:
                    self.rect.bottom = sprite.rect.top
                
                elif self.dy < 0:
                    self.rect.top    = sprite.rect.bottom
                
                self.dy = 0
    
    def _update_color(self):
        for sprite in self._get_collisions():
            if isinstance(sprite, PowerUp):
                self.color = sprite.color
                self.image.fill(sprite.color.value)
        
    
        
    
        