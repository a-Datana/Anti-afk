import pyautogui
import random
import time
from pynput import keyboard


def move_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Generate random coordinates to move the mouse by 2 pixels
    dx = random.randint(-1, 1) * 2
    dy = random.randint(-1, 1) * 2

    # Calculate the new position
    new_x = x + dx
    new_y = y + dy

    # Check if the new position is within the screen boundaries
    screen_width, screen_height = pyautogui.size()
    new_x = max(0, min(new_x, screen_width))
    new_y = max(0, min(new_y, screen_height))

    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.1)


# Create a listener for the key combination
def on_press(key):
    # Check if the key combination is "LShift + Esc"
    if key == keyboard.Key.esc and keyboard.Key.shift_l in key.pressed:
        # Break the main loop
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()


# Main loop
while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Wait for a random time between 10 and 60 seconds
    wait_time = random.randint(10, 60)
    time.sleep(wait_time)

    # Check if the mouse hasn't moved during the wait time
    if pyautogui.position() == (x, y):
        # Print the time waited
        print(f"Mouse hasn't moved in the past {wait_time} seconds")

        # Move the mouse
        move_mouse()

    # Check if the key combination was pressed
    if not listener.is_alive():
        # Listener stopped, break the main loop
        break
