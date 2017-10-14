import math
from PIL import Image


class ImageInfo:
    """ Stores one image and provides processing operations on it"""

    def __init__(self, image_path=None):
        if image_path is not None:
            self.load_image(image_path)
        else:
            self.image = None
            self.pixels = None
            self.width = None
            self.height = None
            self.brightness = None
            self.rgb_image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.height, self.width = self.image.size
        self.rgb_image = self.image.convert("RGB")

    def get_brightness_of_pixel(self, x, y):
        """Uses the Ignacio Vazquez-Abrams heuristic to calculate the brightness
        of a single pixel, with rgb values."""
        r_factor = 0.299
        g_factor = 0.587
        b_factor = 0.114
        r, g, b = self.rgb_image.getpixel((x, y))
        brightness = math.sqrt(r_factor * r**2 + g_factor * g**2 + b_factor * b**2)
        return brightness