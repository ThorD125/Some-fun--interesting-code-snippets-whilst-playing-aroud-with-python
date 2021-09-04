import pyautogui
import keyboard
import win32api
import win32con
import time

time.sleep(3)

for x in range(5):
    keyboard.press_and_release('w')
    keyboard.press('d')
    time.sleep(0.43)
    keyboard.release('d')
    keyboard.press_and_release('w')
    keyboard.press('f')
    time.sleep(0.45)
    keyboard.release('f')


quit()
