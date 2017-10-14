class PixelProcessor:
    """Provides methods to calculate informations about single pixels in an given image and about it's neighbors"""
    def __init__(self, image_info):
        self.image_info = image_info

    def calculate_local_binary_pattern(self, x, y):
        if not self.__coordinates_in_range(x, y):
            raise IndexError(
                "The coordinates (" + str(x) + "," + str(y) + ") where out of range or directly at the border")

        lbp_list = list()
        coordinate_pattern = self.__get_lbp_list_pattern()
        center_brightness = self.image_info.get_brightness_of_pixel(x, y)

        for x_difference, y_difference in coordinate_pattern:
            neighbor_brightness = self.image_info.get_brightness_of_pixel(x + x_difference, y + y_difference)
            lbp_value = self.__calculate_lbp_value(center_brightness, neighbor_brightness)
            lbp_list.append(lbp_value)

        return lbp_list

    def __coordinates_in_range(self, x, y):
        """Checks if the given coordinates are in range for processing
        the local binary pattern (LBP). It is not possible to calculate
        the LBP from a pixel at the direct image border, e.g. for the
        pixel with the coordinates (0,0)."""
        if x < 1 or y < 1:
            return False
        if x > self.image_info.width - 2:
            return False
        if y > self.image_info.height - 2:
            return False
        else:
            return True

    def __calculate_lbp_value(self, center_cell_value, neighbor_cell_value):
        """Calculates the value for the lbp gatter for the given center cell and it's neighbor."""
        if neighbor_cell_value >= center_cell_value:
            return 1
        else:
            return 0

    def __get_lbp_list_pattern(self):
        """Returns a list with the relative coordinates from all neighbors from a central pixel, as a tuple (x,y).
        The first coordinates are in the upper left corner"""
        return [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]