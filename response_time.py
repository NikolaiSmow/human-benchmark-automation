import pyautogui
from PIL import ImageGrab
import time

def get_pixel_color(x, y):
    """Return the RGB color of the pixel at the given position."""
    screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return screen.getpixel((0, 0))

def main():
    print("Monitoring mouse position for color change...")
    prev_color = get_pixel_color(*pyautogui.position())

    while True:
        x, y = pyautogui.position()
        current_color = get_pixel_color(x, y)
        print(current_color)

        RED_WAIT = (206, 38, 54, 255)
        GREEN_CLICK = (75, 219, 106, 255)
        if prev_color == RED_WAIT  and current_color == GREEN_CLICK :  # from RED to GREEN
            print("Color changed from RED to GREEN. Clicking now!")
            pyautogui.click()
        
        prev_color = current_color
        # time.sleep(0.0001)  # Check every 100ms to reduce CPU usage.

if __name__ == '__main__':
    main()
