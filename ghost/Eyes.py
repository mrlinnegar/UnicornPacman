from .Drawable import Drawable
import time
class Eyes(Drawable):
    lastUpdate = time.time()
    eyes = [
    [0,1,1,0,0,0,0,1,1,0],
    [1,1,1,1,0,0,1,1,1,1],
    [1,1,1,1,0,0,1,1,1,1],
    [1,1,1,1,0,0,1,1,1,1],
    [0,1,1,0,0,0,0,1,1,0]
    ]

    pupils = [
    [1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1]
    ]

    def __init__(self, canvas):
        Drawable.__init__(self, canvas)

    def update(self):
        return True

    def draw(self):
        self.updateCanvas(self.eyes,3,4,255,255,255)
        self.updateCanvas(self.pupils,4,6,0,0,138)
