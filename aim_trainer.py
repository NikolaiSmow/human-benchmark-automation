# Auto-Clicker Script

# Necessary dependencies:
# - Install the required packages using pip:
#   pip install Pillow pyautogui

import pyautogui
from PIL import ImageGrab, Image
import time
from mss import mss

from utils import get_screen

# Config
top_left = (300, 270)
bottom_right = (1500, 650)

region = top_left + bottom_right

# We take the pixel position of A region that will change color when the game starts. This way we now when to start the auto-clicker
start_condition_pixel_pos = (775, 318)


def find_white_pixel(region, tolerance=20):
    """Find the position of a near-white pixel in the given screen region."""
    # Capture the screen region using ImageGrab
    img = ImageGrab.grab(bbox=region)
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b, _ = img.getpixel((x, y))
            if (
                abs(r - 255) <= tolerance
                and abs(g - 255) <= tolerance
                and abs(b - 255) <= tolerance
            ):
                # Return the absolute screen position of the white pixel
                return x + region[0], y + region[1]
    return None


def auto_clicker(region):
    """Auto-clicker that detects a white field in the given screen region and clicks it."""
    print("Auto-clicker started. Press Ctrl+C to stop.")
    try:
        while True:
            white_pixel_pos = find_white_pixel(region)
            if white_pixel_pos:
                print(f"Detected white pixel at {white_pixel_pos}. Clicking...")
                pyautogui.click(white_pixel_pos[0], white_pixel_pos[1])
            # time.sleep(1)  # Check every 100ms
    except KeyboardInterrupt:
        print("Script terminated by user.")


# Example usage
# Define the screen region to monitor (left, top, right, bottom)

if __name__ == "__main__":
    game_start = False
    try:
        while True:
            img = ImageGrab.grab()
            pixel_color = img.getpixel(start_condition_pixel_pos)
            if pixel_color != (255, 255, 255, 255):
                game_start = True
                break
        print("Game Started. Starting auto-clicker...")
        auto_clicker(region)
    except KeyboardInterrupt:
        print("Script ended by user")
