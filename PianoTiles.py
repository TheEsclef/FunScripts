from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X: 620,  710, 790, 880
#Y: 600

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(620, 600)[0] == 0:
        click(620, 600)
    if pyautogui.pixel(710, 600)[0] == 0:
        click(710, 600)
    if pyautogui.pixel(790, 600)[0] == 0:
        click(790, 600)
    if pyautogui.pixel(880, 600)[0] == 0:
        click(880, 600)
    
