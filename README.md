# About
Ever had an annoying problem where your device is administerd by company admin and no matter what you do your screen will lock after some idle time?

Thats for safety reasons, but what if you are home alone and there is no one to peer into your screen and steal company secrets?

Easy solution: buy a mouse mover!, place your mouse on it and voila, your mouse keeps movind and the device doesnt lock...
 or
Keep youtube running on another screen 


But hey!...


What if we make the OS simulate that?

Presenting......

a tool to keep your screen awake

You can move the mouse 

or you can use keyboard for regulated keypresses.



In this repo we use the volume keys to keep the screen awake, thereby not disrupting the users typing experience (given that you are probably coding)


The volume will increase and decrease by 2 points, every n seconds. This n is determined by the user
# Imports
Uses

- python 3.13
- pyautogui
- pyinstaller

# Build

Use the following commands in powershell to:

To build your exe file:
>    pyinstaller --noconfirm --onefile --windowed keep_screen_awake.py    

To check the if the exe is running in your tasks:
>    tasklist | sort

To kill the task:
>    taskkill /F /im keep_screen_awake.exe