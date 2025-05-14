import pyautogui
import time

def prevent_idle(screenofftime: int):
    while True:
        # x, y = pyautogui.position()  # Get current mouse position
        # pyautogui.moveTo(x + 2, y)   # Move 1 pixel to the right
        # time.sleep(1)
        # x, y = pyautogui.position()  # Get current mouse position
        # pyautogui.moveTo(x - 2, y)   # Move 1 pixel to the right

        pyautogui.keyDown('volumeup')
        pyautogui.keyUp('volumeup')
        time.sleep(0.5)
        pyautogui.keyDown('volumedown')
        pyautogui.keyUp('volumedown')
        time.sleep(0.5)


        # Wait for 295 seconds, since my screen goes off in 5 min
        time.sleep(screenofftime) 


if __name__ == "__main__":
    screenofftime = (60*5) - 5
    # prevent_idle(screenofftime)
    prevent_idle(10)

