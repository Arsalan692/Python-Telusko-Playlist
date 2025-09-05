
import pyautogui
from time import sleep

def get_specs():
    pyautogui.hotkey("winright", "r")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write("systeminfo", interval=0.01)
    pyautogui.press("enter")

def open_application(name):
    pyautogui.hotkey("winright", "d")
    pyautogui.press("winright")
    pyautogui.write(name, interval=0.01)
    pyautogui.press("enter")



