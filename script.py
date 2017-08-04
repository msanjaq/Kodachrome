from controller import Controller
from model      import Model
from view       import View
from player     import Player

if __name__ == '__main__':
    v = View(Model(Controller(Player())))
    v.run()
    pass