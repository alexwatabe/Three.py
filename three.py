from graphics import graphics 
from random import random
import random

def main():
    gui = graphics(700, 700, 'Three')
# random height of the objects
    while True:
        y_coord = random.randint(0,600)
        ellip_y = random. randint(0,600)
        y1 = random. randint(0,600)
        x_coord = 0
        ellip_x = 25
        x1 = 25
# shape
        while x_coord < 700 :
            gui.clear()
            gui.rectangle(x_coord, y_coord, 100, 100, 'dark green')
            gui.ellipse(ellip_x, ellip_y, 100, 100, 'orange')
            gui.triangle(x1, y1, x1 - 50 , y1 + 100, x1 + 50, y1 + 100, 'blue')
            x_coord += 10
            ellip_x += 10
            x1 += 10
            gui.update_frame(100)


main()