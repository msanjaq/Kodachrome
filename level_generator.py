from sprites.platform import Platform
from sprites.player import Player
from sprites.powerups import PowerUp, PowerUpColors
from sprites.simple_enemy import SimpleEnemy


class LevelGeneratorException(Exception):
    pass


class Level(object):
    '''
    classdocs
    '''

    def __init__(self, level_file, level_width, level_height):
        '''
        Constructor
        '''
        self.platform_list = []
        self.player = None
        self.mobile_sprites = []

        with open(level_file) as file:
            self._level = file.readlines()

        self._width_scale = level_width / _get_longest_line_len(self._level)
        self._height_scale = level_height / len(self._level)

        for line_num in range(len(self._level)):
            for col_num in range(len(self._level[line_num])):
                if self._level[line_num][col_num] == "P":
                    self._add_platform(line_num, col_num)

                elif self._level[line_num][col_num] == "p":
                    x = col_num * self._width_scale
                    y = line_num * self._height_scale
                    self.player = Player(x, y)

                elif self._level[line_num][col_num] == "O":
                    self._add_power_up(line_num, col_num, PowerUpColors.ORANGE)

                elif self._level[line_num][col_num] == "s":
                    self._add_enemy(line_num, col_num, SimpleEnemy)

    def _get_dimension_tuple(self, line_num, col_num):
        '''Returns (x_coordinate, y_coordinate, width, height'''
        x = self._width_scale * col_num
        y = self._height_scale * line_num

        text_width = _get_platform_width(self._level[line_num][col_num+1:],
                                         line_num, col_num)

        text_height = _get_platform_height(self._level[line_num+1:],
                                           line_num, col_num)

        width = self._width_scale * text_width
        height = self._height_scale * text_height
        return (x, y, width, height)

    def _add_platform(self, line_num, col_num):
        x = self._width_scale * col_num
        y = self._height_scale * line_num

        text_width = _get_platform_width(self._level[line_num][col_num+1:],
                                         line_num, col_num)
        text_height = _get_platform_height(self._level[line_num+1:],
                                           line_num, col_num)

        width = self._width_scale * text_width
        height = self._height_scale * text_height
        self.platform_list.append(Platform(x, y, width, height))

    def _add_power_up(self, line_num, col_num, color):
        x = self._width_scale * col_num
        y = self._height_scale * line_num

        text_width = _get_platform_width(self._level[line_num][col_num+1:],
                                         line_num, col_num)
        text_height = _get_platform_height(self._level[line_num+1:],
                                           line_num, col_num)

        width = self._width_scale * text_width
        height = self._height_scale * text_height
        self.platform_list.append(PowerUp(x, y, width, height, color))

    def _add_enemy(self, line_num, col_num, enemy_type):
        dim = self._get_dimension_tuple(line_num, col_num)
        self.mobile_sprites.append(enemy_type(*dim))


def _get_platform_width(line, line_num, col_num):
    result = 2
    for c in line:
        if c == "E":
            return result
        result += 1

    raise LevelGeneratorException('''
        Missing horizontal endpoint ('E')
        for the platform on line {} column {}
        '''.format(line_num, col_num))


def _get_platform_height(lines, line_num, col_num):
    result = 2
    for line in lines:
        if len(line) > col_num and line[col_num] == "E":
            return result
        result += 1

    raise LevelGeneratorException('''
        Missing vertical endpoint ('E') for
        the platform on line {} and column {}
        '''.format(line_num, col_num))


def _get_longest_line_len(lines):
    return len(max(lines, key=lambda line: len(line)).strip())


if __name__ == "__main__":
    l = Level("./levels/level0.txt", 800, 800)
    print(l.platform_list)
    print(l.mobile_sprites)
