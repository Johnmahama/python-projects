import os
import pyautogui

path = os.path.join(os.path.expanduser('~'), 'Pictures')


def screen_shot():
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(f"{path}\\new_screenshots.png")
    print("Screenshot saved")


if __name__=="__main__":
    screen_shot()