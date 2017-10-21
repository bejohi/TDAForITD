class ImageMatrix:
    def __init__(self, width, height):
        self.__check_width_and_height(width, height)
        self.height = height
        self.width = width
        self.brightness_matrix = self.__init_2d_matrix_with_none()
        self.lbp_pattern_matrix = self.__init_2d_matrix_with_none()
        self.lbp_morph_matrix = self.__init_2d_matrix_with_none()

    def __init_2d_matrix_with_none(self):
        """Initializes a 2d matrix with the value None"""
        matrix = [[None for _ in range(self.height)] for _ in range(self.width)]
        return matrix

    # TODO [bejohi]: check if the pixels on the y axis are face down and document this method!
    def get_morph_tuple(self):
        print("DEBUG: processing get_morph_tuple...")
        image_tuple = []
        for x in range(self.width):
            for y in range(self.height):
                if self.lbp_morph_matrix[x][y]:
                    image_tuple.append((x, self.height - y))  # Turn th y axis around.
        return image_tuple

    @staticmethod
    def __check_width_and_height(width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be greater or equal to zero.")
