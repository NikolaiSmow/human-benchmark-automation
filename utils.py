from PIL import Image
from mss import mss


def get_screen():
    # Capture entire screen
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
