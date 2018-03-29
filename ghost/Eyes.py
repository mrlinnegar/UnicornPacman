from .Drawable import Drawable

class Eyes(Drawable):
    closed = False
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
        now = time.time()
        if((now - self.lastUpdate) > 1000):
            self.closed = not self.closedflip
            self.lastUpdate = now
            
        return True

    def draw(self):
        if not self.closed:
            self.updateCanvas(self.eyes,4,4,255,255,255)
            self.updateCanvas(self.pupils,6,6,0,0,138)
