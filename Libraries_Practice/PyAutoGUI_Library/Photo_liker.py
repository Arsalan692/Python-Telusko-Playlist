import pyautogui
import time


time.sleep(3)

for i in range(10):
    pyautogui.doubleClick(720, 494, 0.1)
    time.sleep(2)
    pyautogui.press("right")