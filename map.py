from room import Room


class Map:
    """
    a class to organize multiple rooms
    """

    def __init__(self, width=4, height=4):
        self.__width = width
        self.__height = height
        self.__start = None
        self.__destination = None
        self.__map = None

    def print_map(self):
        """show the map in the console"""
        for row in self.__map:
            show_spot = ""
            for room in row:
                if room.get_value() == 0:
                    show_spot += " ."
                elif room.get_value() == 1:
                    show_spot += " □"
                elif room.get_value() == 2:
                    show_spot += " S"
                elif room.get_value() == 3:
                    show_spot += " D"
                elif room.get_value() == 10:
                    show_spot += " ▲"
            print(show_spot)
        print(" ")

    def generate_map(self):
        """generate the map with start and destination"""
        self.__map = [[Room(y, x) for x in range(self.__width)] for y in range(self.__height)]
        self.__start = self.__map[0][0]
        self.__start.set_start()
        self.__destination = self.__map[self.__height - 1][self.__width - 1]
        self.__destination.set_destination()


def run():

    map = Map()
    map.generate_map()
    map.print_map()


if __name__ == "__main__":
    run()