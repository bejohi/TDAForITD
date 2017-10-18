from image_handling.image_information import ImageInfo

if __name__ == "__main__":
    """For experimental purpose only."""
    image_path = "data_storage/images/example_image_davinci.png"
    image_info = ImageInfo(image_path)
    image_matrix = image_info.create_image_matrix_with_brightness()
    print(str(image_matrix.brightness_matrix[100][100]))