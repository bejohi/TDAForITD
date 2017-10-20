import math

from PIL import Image

from image_handling.image_matrix import ImageMatrix
from image_handling.pixel_processor import PixelProcessor


class PixelProcessor(object):
    pass


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

        self.pixel_processor = PixelProcessor(self)
        self.image_matrix = ImageMatrix(self.width, self.height)

    def load_image(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.height, self.width = self.image.size
        self.rgb_image = self.image.convert("RGB")

    def fill_image_matrix_with_brightness(self):
        for w in range(self.width):
            for h in range(self.height):
                self.image_matrix.brightness_matrix[w][h] = self.get_brightness_of_pixel(w, h)

    def fill_image_matrix_with_lbp(self):
        for w in range(self.width):
            for h in range(self.height):
                self.image_matrix.lbp_pattern_matrix[w][h] = self.pixel_processor.calculate_local_binary_pattern(w, h)

    def fill_image_matrix_with_with_lbp_morph_values(self):
        print("DEBUG: Processing fill_image_matrix_with_lbp...")
        self.fill_image_matrix_with_lbp()
        print("DEBUG: fill_image_matrix_with_with_lbp_morph_values...")
        for w in range(self.width):
            for h in range(self.height):
                is_morp = self.pixel_processor.check_if_lbp_is_morph_relevant(
                    self.image_matrix.lbp_pattern_matrix[w][h])
                self.image_matrix.lbp_morph_matrix[w][h] = is_morp

    def get_brightness_of_pixel(self, x, y):
        """Uses the Ignacio Vazquez-Abrams heuristic to calculate the brightness
        of a single pixel, with rgb values."""
        r_factor = 0.299
        g_factor = 0.587
        b_factor = 0.114
        try:
            r, g, b = self.rgb_image.getpixel((x, y))
            brightness = math.sqrt(r_factor * r ** 2 + g_factor * g ** 2 + b_factor * b ** 2)
            return brightness
        except IndexError: # TODO [bejohi] check why the pillow method throws this exception here.
            return -1
