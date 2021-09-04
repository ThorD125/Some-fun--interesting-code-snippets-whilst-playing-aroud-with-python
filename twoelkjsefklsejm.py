from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

while 1:
    if pyautogui.locateOnScreen('testimage.png') != None:
        print("See it")
        time.sleep(0.5)
    else:
        print("Don t see it")
        time.sleep(0.5)