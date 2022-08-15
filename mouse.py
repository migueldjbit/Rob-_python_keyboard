from pynput.mouse import Button, Controller
import time

mouse = Controller()
time.sleep(3)
mouse.position = (578, 720)
mouse.click(Button.left)