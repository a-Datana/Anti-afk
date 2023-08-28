import pyautogui
import random
import time
import tkinter as tk
from pynput import keyboard


def move_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Generate random offsets to move the mouse by 2 pixels
    dx = random.randint(-1, 1) * 2
    dy = random.randint(-1, 1) * 2

    # Calculate the new position
    new_x = max(0, min(x + dx, pyautogui.size()[0]))
    new_y = max(0, min(y + dy, pyautogui.size()[1]))

    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.1)


def on_press(key):
    # Check if the key combination is "LShift + Esc"
    if key == keyboard.Key.esc and keyboard.Key.shift_l in key.pressed:
        # Break the main loop
        return False


def start_script():

    # Get the input values from the UI
    min_time = int(min_entry.get()) if min_entry.get() else 10
    max_time = int(max_entry.get()) if max_entry.get() else 60

    # Create a listener for the key combination
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Close the input window
    window.destroy()
    
    # Main loop
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Wait for a random time between min_time and max_time seconds
        wait_time = random.randint(min_time, max_time)
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

# Create the UI window
window = tk.Tk()

# Create labels and entry fields for min and max time
min_label = tk.Label(window, text="Minimum time (defaults to 10 sec):")
min_label.pack()
min_entry = tk.Entry(window)
min_entry.pack()

max_label = tk.Label(window, text="Maximum time (defaults to 60 sec):")
max_label.pack()
max_entry = tk.Entry(window)
max_entry.pack()

# Create a button to start the script
start_button = tk.Button(window, text="Start Script", command=start_script)
start_button.pack()

# Start the UI event loop
window.mainloop()
