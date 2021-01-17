import rotatescreen
import time
screen = rotatescreen.get_primary_display()
time.sleep(10)
for i in range(100):
     time.sleep(1)
     screen.rotate_to(i*60 % 360)

