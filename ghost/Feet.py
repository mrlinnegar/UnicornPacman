from .Drawable import Drawable 

class Feet(Drawable):
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
        r, g, b = color
        if(self.flip):
          self.updateCanvas(self.feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(self.feet,0,13,r,g,b)

        self.flip = not self.flip
