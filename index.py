import unicornhathd
import time

class Drawable:
    def __init__(self, canvas):
        self.canvas = canvas

    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

class Eyes:
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

    def draw(self):
        self.updateCanvas(self.eyes,2,4,255,255,255)
        self.updateCanvas(self.pupils,2,6,0,0,138)

class Feet:
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

    def __init__(self, canvas, color):
        self.color = color
        Drawable.__init__(self, canvas)

    def draw(self):
        r, g, b = self.color
        if(self.flip):
          self.updateCanvas(self.feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(self.feet,0,13,r,g,b)

        self.flip = not self.flip


class Ghost:

    body = [
    [0,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

    flip = False


    def __init__(self, canvas, color, x=1, y=1):
            Drawable.__init__(self, canvas)
            self.color = color
            self.eyes = Eyes(canvas)
            self.feet = Feet(canvas, color)
            self.position = (x, y)



    def draw(self):
        r, g, b = self.color
        self.updateCanvas(self.body,1,1,r,g,b)
        self.eyes.draw()
        self.feet.draw()

    def update(self):
        return

ghost = Ghost(unicornhathd, (0,255,0),1,1)

try:
    while True:
      unicornhathd.clear()
      ghost.draw()
      unicornhathd.show()
      time.sleep(0.1)

except KeyboardInterrupt:
    unicornhathd.off()
