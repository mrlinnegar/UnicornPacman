from Eyes import Eyes
from Body import Body
from Feet import Feet

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

    def draw(self):
        self.body.draw(self.color)
        self.feet.draw(self.color)
        self.eyes.draw()

    def setColor(self, color):
        self.color = color