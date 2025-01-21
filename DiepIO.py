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

#255, 232
#252, 118
#118, 141
while keyboard.is_pressed("q") is not True:
    pic = pyautogui.screenshot(region=(350,170,1100,600))
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))
            if (r == 255 and g == 232) or (r == 118 and g == 141) or (r == 252 and g == 118):
                click(x+350,y+170)
                time.sleep(0.05)
                break
