import os

from scripts.image_handling.image_information import ImageInfo
from scripts.image_handling.pixel_processor import PixelProcessor

if __name__ == "__main__":
    image_path = os.path.join("../../data_storage/images/example_image_davinci.png")
    image_processor = ImageInfo(image_path)
    print(image_processor.width)
    print(image_processor.height)
    print(image_processor.pixels[0, 0])
    print(image_processor.get_brightness_of_pixel(0, 0))
    print(type(image_processor.pixels))
    pixel_processor = PixelProcessor(image_processor)
    print(pixel_processor.calculate_local_binary_pattern(100, 200))
