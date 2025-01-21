from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# color we are looking for: (R 255)

while keyboard.is_pressed("q") == False:
    pic = pyautogui.screenshot(region=(670,370,630,500))
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))
            if b == 177:
                click(x+670,y+370)
                time.sleep(0.05)
                print("Shot Target")
