class Image:
    """A mock for the pillow Image class."""
    def __init__(self, width: int, height:int):
        self.width = width
        self.height = height
        self.pixel_matrix = self.__create_mock_matrix(width,height)

    @staticmethod
    def __create_mock_matrix(width: int, height: int, default_value: float = 1):
        return [[(default_value, default_value, default_value) for _ in range(width)] for _ in range(height)]

    def getpixel(self, tuple: tuple):
        x, y = tuple
        return self.pixel_matrix[y][x]
