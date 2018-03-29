class Drawable:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def update(self):
        return True

    def updateCanvas(self, pixels,x,y, r,g,b):
      for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
          if col==1:
            if(rowIndex+y > 15 or colIndex +x > 15):
                return
            else:
                self.canvas.set_pixel(rowIndex+y, colIndex+x, r,g,b)


