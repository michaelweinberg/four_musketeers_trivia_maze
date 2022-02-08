class Room:
    """ a class used to represent a room in the maze"""
    def __init__(self, y, x):
        self.__coordinate_x = x
        self.__coordinate_y = y
        self.__value = 0
        self.__name = None
        self.__do = None
        self.__is_visited = False

    def get_x(self):
        """:return the number of the cols of the room in the map"""
        return self.__coordinate_x

    def get_y(self):
        """:return the number of the rows of the room in the map"""
        return self.__coordinate_y

    def __str__(self):
        """:return str of the name of the room"""
        return "This is a " + "x" + str(self.__coordinate_x) + "y" + str(self.__coordinate_y) + "value" + str(self.__value)

    def set_empty(self):
        """set the room value to zero as an empty room"""
        self.__value = 0
        self.__name = "empty room"

    def set_block(self):
        """set the room value to one as a block"""
        self.__value = 1
        self.__name = "blocked room"

    def set_start(self):
        """set the room value to two as the entrance"""
        self.__value = 2
        self.__name = "start"
        print("start is set")

    def set_destination(self):
        """set the room value to three as the exit"""
        self.__value = 3
        self.__name = "destination"
        print("destination is set")

    def get_value(self):
        """:return the value of the room"""
        return self.__value

    def set_value(self, num):
        """set the room value"""
        self.__value = num
