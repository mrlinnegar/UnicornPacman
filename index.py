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

def Ghost:
    def __init__(self, canvas, x=1, y=1):
            self.position = (x, y)
            self.canvas = canvas
            self.flip = False



    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)

    def draw(self):
        updateCanvas(body,1,1,255,0,0)
        updateCanvas(eyes,3,4,255,255,255)
        updateCanvas(pupils,4,6,0,0,138)
        if(self.flip):
          updateCanvas(feet2, 0,13,255,0,0)
        else:
          updateCanvas(feet,0,13,255,0,0)
        self.flip = not self.flip

    def update(self):

ghost = Ghost(unicornhathd,1,1)

while True:
  unicornhathd.clear()
  ghost.draw()
  unicornhathd.show()
  time.sleep(0.1)
