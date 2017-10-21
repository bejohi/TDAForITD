import math
from PIL import Image


def convert_image_to_brightness_matrix(rgb_image: Image):
    """Converts the given image object to a 2D Matrix with the size of the image """
    brightness_matrix = __init_2d_matrix_with_none(rgb_image.width,rgb_image.height)
    for y in range(rgb_image.height):
        for x in range(rgb_image.width):
            r, g, b = rgb_image.getpixel((x, y))
            brightness = calculate_brightness(r, g, b)
            brightness_matrix[y][x] = brightness
    return brightness_matrix


def __load_image(image_path: str):
    """Loads the image from the hard drive. Can raise FileNotFoundError"""
    image = Image.open(image_path)
    return image.convert("RGB")


def calculate_brightness(r: float, g: float, b: float):
    """Uses the Ignacio Vazquez-Abrams heuristic to calculate the brightness of a single pixel, with rgb values."""
    r_factor = 0.299
    g_factor = 0.587
    b_factor = 0.114
    brightness = math.sqrt(r_factor * r ** 2 + g_factor * g ** 2 + b_factor * b ** 2)
    return brightness


def __init_2d_matrix_with_none(width, height: int):
    """Initializes a 2d matrix with the value None"""
    matrix = [[None for _ in range(width)] for _ in range(height)]
    return matrix


def __calculate_lbp_matrix(lumen_matix):
    pass


def get_image_lbp_matrix(image_path):
    pass


if __name__ == "__main__":
    image = __load_image("../../data_storage/images/example_image_davinci.png")
    convert_image_to_brightness_matrix(image)
