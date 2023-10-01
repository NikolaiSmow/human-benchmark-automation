import pyautogui
from PIL import ImageGrab
import pytesseract

import time

## Needs rework because Object Detection is not accurate enough


def capture_screen(region=None):
    """Capture the screen image for the given region."""
    return ImageGrab.grab(bbox=region)


def extract_text_from_image(image):
    """Extract text from the given image using pytesseract."""
    return pytesseract.image_to_string(image)


def type_text(text):
    """Type the given text using pyautogui."""
    pyautogui.write(text)


def main():
    # Define the screen region to capture (left, top, right, bottom)
    # If set to None, it will capture the full screen
    region_to_capture = (
        470,
        450,
        1430,
        580,
    )  # Adjust this if you want to capture a specific region

    # Capture the screen and extract text
    screen_img = capture_screen(region_to_capture)
    recognized_text = extract_text_from_image(screen_img)

    print("Recognized Text:", recognized_text)
    recognized_text = recognized_text.replace("[", "").replace("(", "")

    time.sleep(2)
    print("Writing....")
    # Type the recognized text
    type_text(recognized_text)


if __name__ == "__main__":
    main()
