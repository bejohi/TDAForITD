"""
    Provide functions to create and calculate a binary skeleton with morph relevant lbp- pattern from a given image.
"""
import lbp_calculate as lbp
import loging as log


def create_morph_skeleton(image_path: str):
    """ Creates a morph skeleton from a image from the given image path. Might raise FileNotFound error."""
    log.log_info(str(create_morph_skeleton.__name__) + ": Load image from: " + image_path)
    rgb_image = lbp.load_image(image_path)
    log.log_info(str(create_morph_skeleton.__name__) + ": Create brightness matrix.")
    brightness_matrix = lbp.convert_image_to_brightness_matrix(rgb_image)
    log.log_info(str(create_morph_skeleton.__name__) + ": Create lbp matrix.")
    lbp_matrix = lbp.calculate_lbp_pattern_for_complete_image(brightness_matrix)
    log.log_info(str(create_morph_skeleton.__name__) + ": Create morph skeleton.")
    morph_skeleton = lbp.convert_lbp_matrix_to_binary_skeleton(lbp_matrix)
    log.log_info(str(create_morph_skeleton.__name__) + ": Calculations completed.")
    return morph_skeleton


def count_morph_relevant_pattern(morph_skeleton):
    sum_1s = 0
    for row in morph_skeleton:
        for binary_value in row:
            sum_1s += binary_value
    return sum_1s


if __name__ == "__main__":
    """For test purpose only."""
    image_path = "../../data_storage/images/example_image_davinci.png"
    morph_skeleton = create_morph_skeleton(image_path)
    count_morph_pattern = count_morph_relevant_pattern(morph_skeleton)
    print(str(len(morph_skeleton) * len(morph_skeleton[0]) - count_morph_pattern) + " vs. " + str(count_morph_pattern))
