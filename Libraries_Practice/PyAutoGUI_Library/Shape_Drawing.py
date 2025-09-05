import pyautogui

import time
time.sleep(3)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0,0.2)
    distance -= 20
    pyautogui.dragRel(0, distance, 0.2)
    pyautogui.dragRel(-distance,0, 0.2)
    distance -= 20
    pyautogui.dragRel(0, -distance, 0.2)

