import unicornhathd
import time

class Drawable:
    def __init__(self, canvas):
        self.canvas = canvas

    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            if(rowIndex+y > 15 or colIndex +x > 15):
                return
            else:
                self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

class Eyes(Drawable):
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
        self.updateCanvas(self.eyes,4,4,255,255,255)
        self.updateCanvas(self.pupils,5,6,0,0,138)

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

class Body(Drawable):

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
    def __init__(self, canvas):
        Drawable.__init__(self, canvas)

    def draw(self, color):
        r, g, b = color
        self.updateCanvas(self.body,1,1,r,g,b)

class Ghost():

    def __init__(self, canvas, color, x=1, y=1):
            self.color = color
            self.body = Body(canvas)
            self.feet = Feet(canvas)
            self.eyes = Eyes(canvas)
            self.position = (x, y)

    def update(self):
        self.eyes.update()
        self.feet.update()
        return True

    def draw(self):
        self.body.draw(self.color)
        self.feet.draw(self.color)
        self.eyes.draw()

    def setColor(self, color):
        self.color = color

clyde = (136,221,206)
inky = (247,199,138)
pinky = (244,197,212)
blinky = (235, 86, 58)


ghost = Ghost(unicornhathd, clyde ,1,1)

try:
    while True:
      unicornhathd.clear()
      ghost.update()
      #ghost.setColor((0,255,255))
      ghost.draw()
      unicornhathd.show()
      time.sleep(0.1)

except KeyboardInterrupt:
    unicornhathd.off()
