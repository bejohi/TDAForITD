class Pixel:
    """Represents a pixel at the coordinates (x,y) (width,height) and stores additional information."""
    def __init__(self, brightness, x, y):
        self.brightness = brightness
        self.__check_coordinates(x, y)
        self.x = x
        self.y = y

    @staticmethod
    def __check_coordinates(x, y):
        """Checks if the given coordinates are valid and raises an index error if they are not."""
        if x < 0 or y < 0:
            raise IndexError("The given pixel coordinates are out of range")
