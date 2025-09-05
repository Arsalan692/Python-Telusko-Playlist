
import pyautogui
from time import sleep


user_input = input("Enter the website URL to open: ")

pyautogui.hotkey("winright", "d")
pyautogui.press("winright")
pyautogui.write("google chrome", interval=0.03)
pyautogui.press("enter")
sleep(0.15)
pyautogui.hotkey("winright", "up")
sleep(0.2)
pyautogui.write(user_input)
pyautogui.press("enter")





