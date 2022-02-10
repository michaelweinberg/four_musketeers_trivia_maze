from room import Room
from player import Player


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
        self.__player = Player()

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

    def generate_player(self):
        x = self.__player.get_x()
        y = self.__player.get_y()
        self.__map[y][x].set_value(10)

    def movement_available(self, y, x):
        if x in range(0, self.__width) and y in range(0, self.__height):
            return True
        else:
            return False

    def update_player(self, move):
        print("update_player")
        if move == "a":
            if self.movement_available(self.__player.get_y(), self.__player.get_x() - 1):
                self.__player.move_west()
        if move == "d":
            if self.movement_available(self.__player.get_y(), self.__player.get_x() + 1):
                self.__player.move_east()
        if move == "w":
            if self.movement_available(self.__player.get_y() - 1, self.__player.get_x()):
                self.__player.move_north()
        if move == "s":
            if self.movement_available(self.__player.get_y() + 1, self.__player.get_x()):
                self.__player.move_south()
                print("update_player_s")

    def move_player(self):
        while not self.reach_exit():
            input_var = input("please enter w/s/a/d:")
            self.update_player(input_var)
            self.generate_player()
            print(self.__player.__str__())
            self.print_map()

    def reach_exit(self):
        if self.__player.get_x() == self.__width - 1 and self.__player.get_y() == self.__height - 1:
            return True
        return False


def run():

    map = Map()
    map.generate_map()
    map.generate_player()
    map.print_map()
    map.move_player()


if __name__ == "__main__":
    run()