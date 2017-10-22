from morph_skeleton import create_morph_skeleton, count_morph_relevant_pattern
from visualisation import visualize_2D_binary_matrix

if __name__ == "__main__":
    """For test purpose only."""
    image_path = "../data_storage/images/example_image_davinci.png"
    morph_skeleton = create_morph_skeleton(image_path)
    count_morph_pattern = count_morph_relevant_pattern(morph_skeleton)
    print(str(len(morph_skeleton) * len(morph_skeleton[0]) - count_morph_pattern) + " vs. " + str(
        count_morph_pattern))
    visualize_2D_binary_matrix(morph_skeleton)

