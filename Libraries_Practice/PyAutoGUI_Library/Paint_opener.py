
import pyautogui
from time import sleep


def open_paint():
    pyautogui.press("winright")
    pyautogui.write("paint", interval=0.05)
    pyautogui.press("Enter")
    sleep(0.7)
    pyautogui.hotkey("winright", "up")
    pyautogui.moveTo(555, 555)
    sleep(1)
    pyautogui.drag(300, 0, 2)
    pyautogui.drag(-150, -150, 2)
    pyautogui.drag(-150, 150, 2)





















