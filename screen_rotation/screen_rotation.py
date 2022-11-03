import rotatescreen
import time

screen = rotatescreen.get_primary_display()
for i in range(5):  # 5 second
    time.sleep(1)
    screen.rotate_to(i * 90 % 360)
