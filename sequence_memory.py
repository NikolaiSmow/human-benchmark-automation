import pyautogui
import time
from mss import mss
from PIL import Image

from utils import get_screen

## Config
## Specify the top left and bottom right corners of the grid in pixel positions
top_left = (770, 300)
bottom_right = (1150, 680)
timeout_seconds = 3  # Wait time before replaying the sequence
default_mouse_pos = (
    700,
    300,
)  # Default mouse position after each sequence to avoid the mouse cursor interfering with detection
start_button_color = (100, 82, 33)
start_button_pos = (960, 610)
# --------------------


def get_grid_centers(topleft, bottomright):
    # Calculate the width and height of the entire rectangle
    width = bottomright[0] - topleft[0]
    height = bottomright[1] - topleft[1]

    # Calculate the width and height of a single cell
    cell_width = width / 3
    cell_height = height / 3

    centers = []

    for i in range(3):
        for j in range(3):
            # Calculate the center of each cell
            x_center = round(topleft[0] + (j * cell_width) + (cell_width / 2))
            y_center = round(topleft[1] + (i * cell_height) + (cell_height / 2))

            centers.append((x_center, y_center))

    return centers


def main():
    grid_center_positions = get_grid_centers(top_left, bottom_right)
    detected_sequence = []
    last_detected_time = None
    try:
        print("Monitoring grid for sequence to start...")
        while True:
            for idx, (pos_x, pos_y) in enumerate(grid_center_positions):
                screen = get_screen()
                pixel_color = screen.getpixel((pos_x, pos_y))
                if pixel_color == (255, 255, 255):
                    if len(detected_sequence) == 0 or detected_sequence[-1] != idx:
                        detected_sequence.append(idx)
                        print(detected_sequence)
                        last_detected_time = time.time()
            # If no new cell turns white within a timeout, replay the sequence
            if (
                last_detected_time
                and (time.time() - last_detected_time) >= timeout_seconds
            ):
                print(f"Sequence: {detected_sequence}")
                for idx in detected_sequence:
                    pos_x, pos_y = grid_center_positions[idx]
                    pyautogui.click(pos_x, pos_y)
                detected_sequence.clear()
                last_detected_time = None
                pyautogui.moveTo(default_mouse_pos)
            time.sleep(0.01)  # Pause between clicks

    except KeyboardInterrupt:
        print("Script terminated by user")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script terminated by user")
