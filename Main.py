##################################################
# Description
"""
This is a copy cat program. You can record your
mouse and keystrokes and then play them. This
allows redundant tasks to be auto completed by
your computer.

How to use:
1. Select a channel. 1-10
2. Select a mode. Record or Play
3. Arrange desktop windows and press CRTL + s to start.
4. If you are recording you will need to press CRTL + e to end the recording process.
5. Program should reset so that it can be used again.
"""
##################################################
# License_info:
# This code is free to use.
##################################################
# Author: Kevin Haston
# Credits: pynput library (https://pypi.org/project/pynput/)
# Maintainer: Kevin Haston
# Email: kevohaston@gmail.com
##################################################

import time
from pynput.mouse import Listener
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from Functions import*

# variables
running = True
mouse = Controller()
move_mouse_position = [0, 0]
click_mouse_position = [0, 0]
channel = 0
mode = "NonSelected"


def listen_on_press_for_start(key):
    if key.char == 's':
        print("Recording...")
    else:
        print("Not A Valid Input")


##################################################
# Main Loop
while running:
    main_display(channel)
    channel = ask_question_int("Select Channel: ", [1, 2, 3])
    mode = ask_question_string("Select Mode: ", ["record", "r", "play", "p"])

    if mode == "record" or mode == "r":

        # Collect events until released
        with Listener(on_press=listen_on_press_for_start, on_release=listen_on_release) as listener:
            listener.join()

    elif mode == "play" or mode == "p":
        print("In play mode.")




