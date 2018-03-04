import unicornhathd
import time
unicornhathd.rotation(0)
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

class Ghost:
    def __init__(self, canvas, x=1, y=1, color):
            self.color = color
            self.position = (x, y)
            self.canvas = canvas
            self.flip = False



    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

    def draw(self):
        r, g, b = self.color
        self.updateCanvas(body,1,1,r,g,b)
        self.updateCanvas(eyes,3,4,255,255,255)
        self.updateCanvas(pupils,4,6,0,0,138)

        if(self.flip):
          self.updateCanvas(feet2, 0,13,r,g,b)
        else:
          self.updateCanvas(feet,0,13,r,g,b)

        self.flip = not self.flip

    def update(self):
        return

ghost = Ghost(unicornhathd,1,1, (0,255,0))

while True:
  unicornhathd.clear()
  ghost.draw()
  unicornhathd.show()
  time.sleep(0.1)
