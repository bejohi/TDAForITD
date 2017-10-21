class Image:
    def __init__(self, size: int = 1):
        self.width = size
        self.height = size
        self.pixel_matrix = self.__create_mock_matrix(size)

    @staticmethod
    def __create_mock_matrix(size: int, default_value: float = 1):
        return [[(default_value, default_value, default_value) for _ in range(size)] for _ in range(size)]

    def getpixel(self, tuple: tuple):
        x, y = tuple
        return self.pixel_matrix[x][y]
