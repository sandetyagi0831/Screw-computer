# Screw up anyones computer project

import rotatescreen
screen = rotatescreen.get_primary_display()
screen.rotate_to(90)
for i in range(1000):
    screen.rotate_to(i*90 % 360)

