import os
import matplotlib
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt

from image_handling.image_information import ImageInfo

if __name__ == "__main__":
    """For experimental purpose only."""
    matplotlib.rcParams["examples.directory"] = os.getcwd()
    image_path = "data_storage/images/example_image_davinci.png"
    datafile = cbook.get_sample_data(image_path)
    image_info = ImageInfo(image_path)

    image_info.fill_image_matrix_with_with_lbp_morph_values()
    morph_tuple_list = image_info.image_matrix.get_morph_tuple()
    datafile = cbook.get_sample_data(image_path)
    img = plt.imread(datafile)
    plt.scatter(*zip(*morph_tuple_list), zorder=1)
    plt.imshow(img, zorder=0)
    plt.show()
