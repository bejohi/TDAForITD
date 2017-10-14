from PIL import Image


class ImageProcessor:
    """ Stores one image and provides processing operations on it"""

    def __init__(self, image_path=None):
        if image_path is not None:
            self.load_image(image_path)
        else:
            self.image = None
            self.pixels = None
            self.width = None
            self.height = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.height, self.width = self.image.size
