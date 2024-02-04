import keyboard
import time


counter = 0

def update_counter():
    global counter
    
    while True:
        if (keyboard.is_pressed('right')):
            counter += 1
            time.sleep(0.2)
        elif(keyboard.is_pressed('left')):
            counter -= 1
            time.sleep(0.2)