import random
import sqlite3

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

    def room_status(self, y, x):
        return self.__map[y][x].visited_status()

    def get_room(self, y, x):
        room = self.__map[y][x]
        return room

    def player_y(self):
        return self.__player.get_y()

    def player_x(self):
        return self.__player.get_x()

    def west_room_available(self):
        if self.movement_available(self.player_y(), self.player_x() - 1):
            if self.__map[self.player_y()][self.player_x()-1].visited_status():
                print("room has been visited")
                return 1
            else:
                print("room has not been visited")
                return 0
        else:
            print("room not available")
            return 2

    def move_west(self):
        if self.movement_available(self.player_y(), self.player_x() - 1):
            self.__player.move_west()
            self.__map[self.player_y()][self.player_x()].set_visited()

    def east_room_available(self):
        if self.movement_available(self.player_y(), self.player_x() + 1):
            if self.__map[self.player_y()][self.player_x()+1].visited_status():
                print("room has been visited")
                return 1
            else:
                print("room has not been visited")
                return 0
        else:
            print("room not available")
            return 2

    def move_east(self):
        if self.movement_available(self.player_y(), self.player_x() + 1):
            self.__player.move_east()
            self.__map[self.player_y()][self.player_x()].set_visited()

    def north_room_available(self):
        if self.movement_available(self.player_y() - 1, self.player_x()):
            if self.__map[self.player_y()-1][self.player_x()].visited_status():
                print("room has been visited")
                return 1
            else:
                print("room has not been visited")
                return 0
        else:
            print("room not available")
            return 2

    def move_north(self):
        if self.movement_available(self.player_y() - 1, self.player_x()):
            self.__player.move_north()
            self.__map[self.player_y()][self.player_x()].set_visited()

    def south_room_available(self):
        if self.movement_available(self.player_y() + 1, self.player_x()):
            if self.__map[self.player_y()+1][self.player_x()].visited_status():
                print("room has been visited")
                return 1
            else:
                print("room has not been visited")
                return 0
        else:
            print("room not available")
            return 2

    def move_south(self):
        if self.movement_available(self.player_y() + 1, self.player_x()):
            self.__player.move_south()
            self.__map[self.player_y()][self.player_x()].set_visited()

    def reach_exit(self):
        if self.player_x() == self.__width - 1 and self.player_y() == self.__height - 1:
            return True
        return False


class Question:
    def get_question(self):
        summary = self._dbselect()
        result = []
        for row in summary:
            result.append(row[0])
            result.append(row[1])
        return result

    def _dbselect(self):
        connection = sqlite3.connect("mydb.db")
        cursorObj = connection.cursor()
        id = random.Random(0, 60)
        result = cursorObj.execute("select * from question where id=%id " %id)
        results = result.fetchall()
        connection.close()
        cursorObj.close()
        return results


def run():

    map = Map()
    map.generate_map()
    map.generate_player()
    map.print_map()


if __name__ == "__main__":
    run()