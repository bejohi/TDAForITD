import matplotlib.pyplot as plt
import morphdetect.loging as log


def visualize_2D_binary_matrix(binary_matrix: list):
    """Visualizes a given 2D Matrix which stores only binary values"""
    log.log_info(
        str(visualize_2D_binary_matrix.__name__) + ": visualize matrix with height: " + str(len(binary_matrix)))
    tuple_list = convert_2d_binary_matrix_to_tuple_list(binary_matrix)
    plt.scatter(*zip(*tuple_list))
    log.log_info(str(visualize_2D_binary_matrix.__name__) + ": calculations finished. Init show.")
    plt.show()
    log.log_info(str(visualize_2D_binary_matrix.__name__) + ": init of show finished.")


def convert_2d_binary_matrix_to_tuple_list(binary_matrix: list):
    """ Creates a list of tuples (x,y) from a given binary pattern, where only the 1s are part of the tuple list."""
    image_tuple = []
    height = len(binary_matrix)
    width = len(binary_matrix[0])
    for y in range(height):
        for x in range(width):
            if binary_matrix[y][x]:
                image_tuple.append((x, y))
    return image_tuple
