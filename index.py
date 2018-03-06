import unicornhathd
import time
from Ghost import Ghost
from threading import Thread

clyde = (136,221,206)
inky = (247,199,138)
pinky = (244,197,212)
blinky = (235, 0, 0)


ghost = Ghost(unicornhathd, blinky ,1,1)


class DrawThread(Thread):
    counter = 0
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            unicornhathd.clear()
            ghost.update()
            ghost.draw()
            unicornhathd.show()
            time.sleep(0.1)


try:
    print "Starting Ghost animation"
    DrawThread()
    while True:
        pass

except KeyboardInterrupt:
    unicornhathd.off()
