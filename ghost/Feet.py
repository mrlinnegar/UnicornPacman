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
        now = time.time()
        if((now - self.lastUpdate) > 0.10):
            self.flip = not self.flip
            self.lastUpdate = now
            
        return True

    def draw(self, color):

        r, g, b = color
        if(self.flip):
          self.updateCanvas(self.feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(self.feet,0,13,r,g,b)