import random


a = 0
while a < 20:
    angle = random.randint(0, 360)
    while 145 > angle > 35 or 325 > angle > 205:
        angle = random.randint(0, 360)
    print(angle)
    a += 1