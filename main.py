# GPT-4: could you help me write a small windows application in python which runs in the background, in the system tray, and executes one task, which is: when the user uses its mouse to hover over the bottom left part of the screen, it then would lock windows (like when pressing WINDOWS + L). by the 'bottom left' i mean, a square, with each side having the length of the height of the taskbar.
import threading
import pyautogui
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import os
import time

from getTaskBarHeight import get_taskbar_height


def lock_windows():
    os.system('rundll32.exe user32.dll,LockWorkStation')


active = True


def create_image(width, height, color1, color2):
    # Create an image with the given size and color
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        [width // 2, 0, width, height // 2],
        fill=color2
    )
    return image


def check_mouse_position():
    # Dynamically determine the taskbar size
    taskbar_height = get_taskbar_height()
    screen_width, screen_height = pyautogui.size()

    while active:
        x, y = pyautogui.position()
        if x <= taskbar_height and (screen_height - y) <= taskbar_height:
            print('Mouse is in the bottom left corner')
            lock_windows()
            time.sleep(1)


def on_clicked(icon, item):
    print('Exiting...')
    global active
    active = False
    icon.stop()


# Icon for the system tray
icon = pystray.Icon("test_icon", create_image(
    64, 64, 'black', 'blue'), menu=pystray.Menu(item('Exit', on_clicked)))

# Start the mouse position check in a separate thread
thread = threading.Thread(target=check_mouse_position)
thread.start()

# Run the system tray icon
icon.run()
