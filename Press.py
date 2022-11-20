import pyautogui as K
import subprocess
from time import sleep

def login():
    site="facebook"
    username="username"
    Password="password"
    K.FAILSAFE=False
    K.hotkey('ctrl', 'alt', 'o')
    sleep(4)
    K.write('facebook')
    K.press("enter")
    K.sleep(3)
    K.write(username)
    K.press("tab")
    K.write(Password)
    K.press("enter")
    # for letter in username:
    #     K.press(letter,presses=1)
    # K.press("tab")
    # for letter in Password:
    #     K.press(letter,presses=1)
    # K.press("enter")
