import pyautogui
from PIL import ImageGrab
import time

# Place mouse cursor on the red field during the test and run the script
## TODO: Speedup by using mss instead of pillow


red_wait = (206, 38, 54, 255)
green_click = (75, 219, 106, 255)


def get_pixel_color(x: int, y: int):
    """Return the RGB color of the pixel at the given position."""
    screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    return screen.getpixel((0, 0))


def main():
    print("Monitoring mouse position for color change...")
    prev_color = get_pixel_color(*pyautogui.position())

    while True:
        x, y = pyautogui.position()
        current_color = get_pixel_color(x, y)

        if prev_color == red_wait and current_color == green_click:  # from RED to GREEN
            print("Color changed from red to green. Clicking now!")
            pyautogui.click()

        prev_color = current_color


if __name__ == "__main__":
    main()
