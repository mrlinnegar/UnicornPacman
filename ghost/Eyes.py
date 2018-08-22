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

    eyes_x = 3
    eyes_y = 4

    pupils_x = 4
    pupils_y = 6

    def __init__(self, canvas):
        Drawable.__init__(self, canvas)

    def update(self):
        return True

    def draw(self):
        self.updateCanvas(self.eyes,eyes_x,eyes_y,255,255,255)
        self.updateCanvas(self.pupils,pupils_x,pupils_y,0,0,138)
