from sprites.platform import Platform
from sprites.player   import Player

class LevelGeneratorException(Exception):
    pass
    

class Level(object):
    '''
    classdocs
    '''

    def __init__(self, 
                level_file  : str, 
                level_width : int,
                level_height: int, 
                player_start_coord = (0,0)):
        '''
        Constructor
        '''
        self.platform_list = []
        #self.player        = Player(player_start_coord)
        self.player = None
        
        with open(level_file) as file:
            self._level = file.readlines()
        
        self._width_scale  = level_width  / _get_longest_line_len(self._level)
        print(_get_longest_line_len(self._level))
        self._height_scale = level_height / len(self._level)
        
        for line_num in range(len(self._level)):
            for col_num in range(len(self._level[line_num])):
                if self._level[line_num][col_num] == "P":
                    self._add_platform(line_num, col_num)
                
                elif self._level[line_num][col_num] == "p":
                    x = col_num   * self._width_scale 
                    y = line_num  * self._height_scale
                    self.player = Player((x,y))
        
        
    
    def _add_platform(self, line_num: int, col_num: int) -> None:
        x           = self._width_scale  * col_num
        y           = self._height_scale * line_num
        text_width  = _get_platform_width(self._level[line_num][col_num+1:], line_num, col_num)
        text_height = _get_platform_height(self._level[line_num+1:], line_num, col_num)
        width       = self._width_scale  * text_width
        height      = self._height_scale * text_height
        print("scale: ",self._width_scale, self._height_scale)
        print(x,y,width,height)
        self.platform_list.append(Platform(x, y, width, height))
    

def _get_platform_width(line: str, line_num: int, col_num: int) -> int:
    result = 2
    for c in line:
        if c == "E":
            return result
        result += 1

    raise LevelGeneratorException('''
        Missing horizontal endpoint ('E')
        for the platform on line {} column {}
        '''.format(line_num, col_num))
             

def _get_platform_height(lines: [str], line_num: int, col_num: int) -> int:
    result = 2
    for line in lines:
        if len(line) > col_num and line[col_num] == "E":
            return result
        result += 1

    raise LevelGeneratorException('''
        Missing vertical endpoint ('E') for 
        the platform on line {} and column {}
        '''.format(line_num, col_num))
    

def _get_longest_line_len(lines: [str]) -> int:
    return len(max(lines, key=lambda line : len(line)).strip())
        

if __name__ == "__main__":
    Level("./levels/level0.txt", 800, 800)
        