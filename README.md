# Anti-afk
A Python script to move your mouse when you haven't moved it in a while, to keep your PC awake when you're away.

# How it works
## main.py
The script checks when the last mouse movement happened and then waits a random interval between the min and max time. The mouse will move up to 2 pixels to a random direction afterwards, avoiding the screen boundaries. The time waited will default to a minimum of 10 seconds and a maximum of 60 seconds.

I have built this into my autostart process. I think AFK detection is an annoyance.

## main_ui.py
Same as above but with changeable min and max time. Pressing the "Start Script" button closes the window and runs the script.

## Closing the script
The script can be stopped either via the task manager or by pressing LShift + Escape together, after which it finishes its iterations.

# Dependencies
This software uses:
- pyautogui
- pynput


Optional - Create Virtual Env Step: "python3 -m venv ./Anti-afk" <br> 
"pip install -r requirements.txt"


# Contributing
Contributions are welcome! 
If you have any ideas, suggestions, or bug fixes, please feel free to contribute to this project. You can do so by following these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.

I appreciate any contributions and will review and merge them if they align with the project's goals. 
Thank you for considering contributing to this project!


