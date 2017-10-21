import math
from PIL import Image

"""A list of (y,x) positions of all neighbours of a pixel."""
__pixel_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def convert_image_to_brightness_matrix(rgb_image: Image):
    """Converts the given image object to a 2D Matrix with height and width of the image """
    brightness_matrix = __init_2d_matrix_with_none(rgb_image.width, rgb_image.height)
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


def calculate_lbp_pattern(brightness_matrix: list(list()), x: int, y: int):
    """Calculates the lbp pattern for a single pixel in a given pixel matrix and returns the pattern as an list,
    e.g [1,0,0,0,1,0,1,0]"""
    lbp_pattern = []
    for y_n, x_n in __pixel_neighbours:
        y_neighbour = y_n + y
        x_neighbour = x_n + x

        if x_neighbour < 0 or y_neighbour < 0:
            raise IndexError("The x and y coordinates can not be directly at the image border.")

        neighbour_brightness = brightness_matrix[y_neighbour][x_neighbour]
        pixel_brightness = brightness_matrix[y][x]
        lbp_pattern.append(__decide_lbp_1_or_0(pixel_brightness, neighbour_brightness))

    return lbp_pattern


def __decide_lbp_1_or_0(pixel_brightness: float, neighbour_brightness: float):
    if neighbour_brightness >= pixel_brightness:
        return 1
    else:
        return 0


def get_image_lbp_matrix(image_path):
    pass


def __init_2d_matrix_with_none(width, height: int):
    """Initializes a 2d matrix with the value None"""
    matrix = [[None for _ in range(width)] for _ in range(height)]
    return matrix


def __get_pixel_neighbour_positions():
    """Returns a list with the relative coordinates from all neighbors from a central pixel, as a tuple (x,y).
    The first coordinates are in the upper left corner"""


if __name__ == "__main__":
    image = __load_image("../../data_storage/images/example_image_davinci.png")
    convert_image_to_brightness_matrix(image)
