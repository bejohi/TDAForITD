"""
    Provide functions to create and calculate a binary skeleton with morph relevant lbp- pattern from a given image.
"""
import morphdetect.lbp_calculate as lbp
import morphdetect.loging as log


def create_morph_skeleton(image_path: str):
    """ Creates a morph skeleton from a image from the given image path. Might raise FileNotFound error."""
    log.log_info(str(create_morph_skeleton.__name__) + ": Load image from: " + image_path)
    gray_image = lbp.load_image(image_path)
    log.log_info(str(create_morph_skeleton.__name__) + ": Create lbp matrix.")
    lbp_matrix = lbp.calculate_lbp_pattern_for_complete_image(gray_image)
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
