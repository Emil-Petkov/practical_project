import os
import time

def desktop_locker():
    time.sleep(10)
    winpath = r"C:\Windows\System32"
    os.system(winpath + r"\rundll32.exe " + winpath + r"\user32.dll,LockWorkStation")

while True:
    desktop_locker()
