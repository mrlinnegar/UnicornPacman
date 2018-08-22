import unicornhathd as display
import time
from ghost.Ghost import Ghost
from time import sleep



clyde = (136,221,206)
inky = (247,199,138)
pinky = (244,197,212)
blinky = (235, 0, 0)


ghost = Ghost(display, inky ,1,1)


try:
    print("Starting Ghost animation")

    while True:
        display.clear()
        ghost.update()
        ghost.draw()
        display.show()

except KeyboardInterrupt:
    sleep(1)
    display.off()
    print("Ending ghost animation")
