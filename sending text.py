import pyautogui
import time
while True:
    time.sleep(3)
    pyautogui.typewrite('hello world')
    time.sleep(3)
    pyautogui.press("enter")