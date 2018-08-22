import unicornhathd as display
import time
from ghost.Ghost import Ghost
from threading import Thread
from time import sleep



clyde = (136,221,206)
inky = (247,199,138)
pinky = (244,197,212)
blinky = (235, 0, 0)


ghost = Ghost(display, blinky ,1,1)


class DrawThread(Thread):
    counter = 0
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            display.clear()
            ghost.update()
            ghost.draw()
            display.show()

        display.off()



try:
    print("Starting Ghost animation")
    DrawThread()
    while True:
        pass
    display.off()

except KeyboardInterrupt:
    sleep(1)
    print("Ending ghost animation")
    display.off()
