class Picture:
    """Represents an picture with a 2d matrix which stores pixel objects with additional information. (We gave this class
    the name 'Picture' and not 'Image' because this keyword is used by a height amount of other libraries.)"""
    def __init__(self, width, height):
        self.pixel_matrix = self.__init_pixel_matrix(width, height)
        self.width = width
        self.height = height

    def add_pixel(self, pixel):
        """Adds a pixel to the image pixel matrix. Returns True if there already was a pixel at the given position,
        and False otherwise."""
        self.__check_pixel_in_range(pixel)
        if self.pixel_matrix[pixel.x][pixel.y] is not None:
            return True
        self.pixel_matrix[pixel.x][pixel.y] = pixel
        return False

    @staticmethod
    def __init_pixel_matrix(width, height):
        """Initializes the 2d pixel matrix withe the value None"""
        matrix = [[None for _ in range(height)] for _ in range(width)]
        return matrix

    def __check_pixel_in_range(self, pixel):
        """Checks if the given pixel has valid formed coordinates and raises an IndexError if it has not."""
        if pixel.x > self.width or pixel.y > self.height:
            raise IndexError("Pixel out of range")
        if pixel.x < 0 or pixel.y < 0:
            raise IndexError("Pixel position must not be negative")
