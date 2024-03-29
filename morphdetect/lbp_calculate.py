from PIL import Image

"""
    Provides function to convert a given image step by step into a binary skeleton.
"""

"""A list of (y,x) positions of all neighbours of a pixel."""
__pixel_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def load_image(image_path: str):
    """

    :param image_path: the path + name of the image.
    :return: the image object, converted to a grayscale image.
    :raises FileNotFoundError
    """
    image = Image.open(image_path)
    return image.convert("LA")  # LA == grayscale


def calculate_lbp_pattern(img: Image.Image, x: int, y: int):
    """Calculates the lbp pattern for a single pixel in a given pixel matrix and returns the pattern as an list,
    e.g [1,0,0,0,1,0,1,0]"""
    lbp_pattern = []
    for y_n, x_n in __pixel_neighbours:
        y_neighbour = y_n + y
        x_neighbour = x_n + x

        if x_neighbour < 0 or y_neighbour < 0:
            raise IndexError("The x and y coordinates can not be directly at the image border.")

        neighbour_brightness = img.getpixel((x_neighbour, y_neighbour))
        pixel_brightness = img.getpixel((x, y))
        lbp_pattern.append(__decide_lbp_1_or_0(pixel_brightness, neighbour_brightness))

    return lbp_pattern


def calculate_lbp_pattern_for_complete_image(img: Image.Image):
    """Creates a complete new 2D Matrix out of a given brightness matrix. The new matrix contains the lbp pattern for
    every pixel, expect the once at the direct border """
    lbp_pattern_matrix = __init_2d_matrix_with_none(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            if not __is_coordinates_in_lbp_calculation_range(x, y, img.width, img.height):
                lbp_pattern_matrix[y][x] = []  # The pixel at the direct border get a empty lbp_pattern.
                continue
            lbp_pattern = calculate_lbp_pattern(img, x, y)
            lbp_pattern_matrix[y][x] = lbp_pattern

    return lbp_pattern_matrix


def convert_lbp_matrix_to_binary_skeleton(lbp_matrix: list):
    """Converts a given 2D matrix with lbp-patterns, into a 2D matrix which holds only 1s and 0s, depending on the
    morph relevance of the pattern in each field."""
    height = len(lbp_matrix)
    width = len(lbp_matrix[0])
    binary_skeleton = __init_2d_matrix_with_none(width, height)

    for y in range(height):
        for x in range(width):
            morph_relevant = is_lbp_pattern_morph_relevant(lbp_matrix[y][x])
            binary_skeleton[y][x] = morph_relevant

    return binary_skeleton


def is_lbp_pattern_morph_relevant(lbp_pattern: list):
    """ Only lpb-pattern with exact 2 1s, where both 1s are direct neighbours, are relevant, e.g. [0,1,1,0,0,0,0,0]."""
    sum_of_1s = 0
    has_neighbours = False
    for index in range(len(lbp_pattern)):
        sum_of_1s += lbp_pattern[index]
        if sum_of_1s > 2:
            return False
        if lbp_pattern[index] == 1 and lbp_pattern[index - 1] == 1:
            has_neighbours = True
    return has_neighbours


def __decide_lbp_1_or_0(pixel_brightness: float, neighbour_brightness: float):
    """Decides if the lbp value for a pair of central-, and neighbour- pixel has the lbp value 1, or 0."""
    if neighbour_brightness >= pixel_brightness:
        return 1
    else:
        return 0


def __is_coordinates_in_lbp_calculation_range(x: int, y: int, width: int, height: int):
    """Checks if a lbp-calculation for the given coordinates is possible."""
    if x <= 0 or y <= 0:
        return False
    if x >= width - 1 or y >= height - 1:
        return False
    else:
        return True


def __init_2d_matrix_with_none(width: int, height: int):
    """Initializes a 2d matrix with the value None."""
    matrix = [[None for _ in range(width)] for _ in range(height)]
    return matrix
