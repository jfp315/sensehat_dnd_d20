from sense_hat import SenseHat
import random

speed = 0.05

sense = SenseHat()
sense.clear()

sense.show_message("Let's Roll!", speed)
def roll_dice():
    r = random.randint(1, 20)
    if r < 20:
    for r in roll_dice     
        sense.show_message(str(r), speed)
    elif r == 20:
        sense.show_message("Critical Hit!")

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1.4 or y > 1.4 or z > 1.4:
        roll_dice()
