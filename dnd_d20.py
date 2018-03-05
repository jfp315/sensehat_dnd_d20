from sense_hat import SenseHat
import random
import time


sense = SenseHat()
sense.clear()

speed = 0.05
x = [255,255,0]
o = [0,0,0]

skull = [
o,o,x,x,x,x,o,o,
o,x,x,x,x,x,x,o,
o,x,o,x,x,o,x,o,
o,x,x,x,x,x,x,o,
o,x,x,o,o,x,x,o,
o,o,x,x,x,x,o,o,
o,o,x,o,o,x,o,o,
o,o,o,o,o,o,o,o
]

sense.show_message("Let's Roll!", speed)
def roll_dice():
    r = random.randint(1, 20)
    if r < 20:
        sense.show_message(str(r), speed)
    elif r == 20:
        sense.show_message("Critical Hit!", speed,
                text_colour=[255,255,0],
                back_colour=[0,0,0])
        sense.set_pixels(skull)

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1.4 or y > 1.4 or z > 1.4:
        roll_dice()
