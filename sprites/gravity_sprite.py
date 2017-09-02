import pygame

from .platform import Platform


class GravitySprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''

    gravity = 1

    def __init__(self, x, y, width, height):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dx = 0
        self.dy = 0

    def update(self):
        self. _calc_gravity()
        self._update_x_direction()
        self._update_y_direction()

    def _get_collisions(self):
        for group in self.groups():
            collisions = pygame.sprite.spritecollide(self, group, False)
            return collisions

    def _calc_gravity(self):
        self.dy += GravitySprite.gravity

    def _update_x_direction(self):
        self.rect.x += self.dx
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dx > 0:
                    self.rect.right = sprite.rect.left

                elif self.dx < 0:
                    self.rect.left = sprite.rect.right

    def _update_y_direction(self):
        self.rect.y += self.dy
        for sprite in self._get_collisions():
            if isinstance(sprite, Platform):
                if self.dy > 0:
                    self.rect.bottom = sprite.rect.top

                elif self.dy < 0:
                    self.rect.top = sprite.rect.bottom
                self.dy = 0
