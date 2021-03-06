class Room:
    """ a class used to represent a room in the maze"""
    def __init__(self, y, x):
        self.__coordinate_x = x
        self.__coordinate_y = y
        self.__value = 0
        self.__name = None
        self.__is_visited = False
        self.__question_status = None

    def get_name(self):
        return self.__name
        
    def get_x(self):
        """:return the number of the cols of the room in the map"""
        return self.__coordinate_x
          
    
    def get_y(self):
        """:return the number of the rows of the room in the map"""
        return self.__coordinate_y

    def __str__(self):
        """:return str of the name of the room"""
        return "This is a " + "x" + str(self.__coordinate_x) + "y" + str(self.__coordinate_y) + "value" + str(self.__value)

    def set_name(self):
        return self.__name
    
    def set_empty(self):
        """set the room value to zero as an empty room"""
        self.__value = 0
        self.__name = "empty room"

    def set_visited(self):
        """set the room value as visited"""
        self.__name = "visited room"
        self.__is_visited = True

    def set_start(self):
        """set the room value to two as the entrance"""
        self.__value = 2
        self.__name = "start"
        self.__is_visited = True
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

    def set_wall(self):
        self.__is_visited = None

    def visited_status(self):
        return self.__is_visited

    def set_block(self):
        self.__value = 4
        print("room blocked")

    def set_question_status_true(self):
        self.__question_status = True

    def set_question_status_false(self):
        self.__question_status = False


