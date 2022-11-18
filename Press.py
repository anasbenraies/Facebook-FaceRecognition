import pyautogui as K
import subprocess
from time import sleep

def login():
    site="facebook"
    username="username"
    Password="password"
    K.FAILSAFE=False
    K.hotkey('ctrl', 'alt', 'o')
    sleep(5)
    for letter in site:
        K.press(letter,presses=1)
    K.press("enter")
    sleep(1.5)
    for letter in username:
        K.press(letter,presses=1)
    K.press("tab")
    for letter in Password:
        K.press(letter,presses=1)
    K.press("enter")
                            

