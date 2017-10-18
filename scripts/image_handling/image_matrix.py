class ImageMatrix:
    def __init__(self, width, height):
        self.__check_width_and_height(width, height)
        self.height = height
        self.width = width
        self.brightness_matrix = self.__init_brightness_matrix()

    def __init_brightness_matrix(self):
        """Initializes the 2d pixel matrix withe the value None"""
        matrix = [[None for _ in range(self.height)] for _ in range(self.width)]
        return matrix

    @staticmethod
    def __check_width_and_height(width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be greater or equal to zero.")
