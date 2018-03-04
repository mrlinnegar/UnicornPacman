import unicornhathd
import time

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
        self.canvas = canvas

    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

    def draw():
        self.updateCanvas(self.eyes,3,4,255,255,255)
        self.updateCanvas(self.pupils,4,6,0,0,138)

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


    def __init__(self, canvas, color, x=1, y=1):
            self.color = color
            self.eyes = Eyes(canvas)
            self.position = (x, y)
            self.canvas = canvas

    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

    def draw(self):
        r, g, b = self.color
        self.updateCanvas(self.body,1,1,r,g,b)
        self.eyes.draw()
        if(self.flip):
          self.updateCanvas(self.feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(self.feet,0,13,r,g,b)

        self.flip = not self.flip

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
