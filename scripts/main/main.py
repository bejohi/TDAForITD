import os

from scripts.image_processing.image_processing import ImageProcessor

if __name__ == "__main__":
    image_path = os.path.join("../../data_storage/images/example_image_davinci.png")
    image_processor = ImageProcessor(image_path)
    print(image_processor.width)
    print(image_processor.height)
    print(image_processor.pixels[0, 0])
    print(image_processor.get_brightness_of_pixel(0,0))
