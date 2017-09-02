from controller import Controller
from level_generator import Level
from model import Model
from view import View

if __name__ == '__main__':
    level0 = Level("./levels/level0.txt", View.width, View.height)
    model = Model(level0, Controller)
    v = View(model)
    v.run()
