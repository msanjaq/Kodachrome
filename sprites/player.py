from .gravity_sprite import GravitySprite
from .powerups import PowerUpColors, PowerUp


class Player(GravitySprite):
    '''
    classdocs
    '''

    speed = 5

    def __init__(self, x, y):
        '''
        Constructor
        '''
        GravitySprite.__init__(self, x, y, 10, 30)
        self.image.fill(PowerUpColors.WHITE.value)
        self.color = PowerUpColors.WHITE

    def jump(self):
        if self.color == PowerUpColors.ORANGE:
            if self.dy in {0, -18, -19, -20}:
                self.dy = 20

        elif self.dy in {0, 18, 19, 20}:
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
        GravitySprite.update(self)
        self._update_color()

    def _update_color(self):
        for sprite in self._get_collisions():
            if isinstance(sprite, PowerUp):
                self.color = sprite.color
                self.image.fill(sprite.color.value)
