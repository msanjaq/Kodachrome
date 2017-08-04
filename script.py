from controller import Controller
from model      import Model
from view       import View

if __name__ == '__main__':
    v = View(Model(Controller()))
    v.run()
    pass