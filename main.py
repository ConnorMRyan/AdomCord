import time
import os
import pytesseract
import win32gui
from PIL import ImageGrab


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def take_screen(windows_rect):
    ss_reg = (windows_rect[0], windows_rect[1], windows_rect[2], windows_rect[3])
    frame = ImageGrab.grab(ss_reg)
    text = pytesseract.image_to_string(frame)
    print(f'{text}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_hwnd(window_title):
    return win32gui.FindWindow(None, window_title)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window_name = "ADOM (version 3.3.3) - © 1994-2019 by Thomas Biskup"
    hwnd = get_hwnd(window_name)
    window_rect = win32gui.GetWindowRect(hwnd)
    while True:
        time.sleep(2)
        os.system('cls')
        take_screen(window_rect)
