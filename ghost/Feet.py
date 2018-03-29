from .Drawable import Drawable 
import time

class Feet(Drawable):
    lastUpdate = time.time()

    feet = [
    [0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0],
    [0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

    feet2 = [
    [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
    [0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    flip = False

    def __init__(self, canvas):
        Drawable.__init__(self, canvas)

    def update(self):
        return True

    def draw(self, color):
        now = time.time()
        r, g, b = color
        if(self.flip):
          self.updateCanvas(self.feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(self.feet,0,13,r,g,b)

        if((now - self.lastUpdate)> 1000):
            self.flip = not self.flip
            self.last_update = time.time()