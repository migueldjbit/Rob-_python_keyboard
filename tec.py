import keyboard
import time
from pynput.mouse import Button, Controller


mouse = Controller()
time.sleep(1)
print(mouse.position)