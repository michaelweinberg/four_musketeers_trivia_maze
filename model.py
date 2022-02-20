import random
import sqlite3

# class Map:
#     """
#     a class to organize multiple rooms
#     """
#
#     def __init__(self, width=4, height=4):
#         self.__width = width
#         self.__height = height
#         self.__start = None
#         self.__destination = None
#         self.__map = None
#         self.__player = Player()
#
#     def print_map(self):
#         """show the map in the console"""
#         for row in self.__map:
#             show_spot = ""
#             for room in row:
#                 if room.get_value() == 0:
#                     show_spot += " ."
#                 elif room.get_value() == 4:
#                     show_spot += " □"
#                 elif room.get_value() == 2:
#                     show_spot += " S"
#                 elif room.get_value() == 3:
#                     show_spot += " D"
#                 elif room.get_value() == 10:
#                     show_spot += " ▲"
#             print(show_spot)
#         print(" ")
#
#     def generate_map(self):
#         """generate the map with start and destination"""
#         self.__map = [[Room(y, x) for x in range(self.__width)] for y in range(self.__height)]
#         self.__start = self.__map[0][0]
#         self.__start.set_start()
#         self.__destination = self.__map[self.__height - 1][self.__width - 1]
#         self.__destination.set_destination()
#
#     def generate_player(self):
#         x = self.__player.get_x()
#         y = self.__player.get_y()
#         self.__map[y][x].set_value(10)
#
#     def movement_available(self, y, x):
#         if x in range(0, self.__width) and y in range(0, self.__height) and self.__map[y][x].get_value() != 4:
#             return True
#         else:
#             return False
#
#     def room_status(self, y, x):
#         return self.__map[y][x].visited_status()
#
#     def get_room(self, y, x):
#         room = self.__map[y][x]
#         return room
#
#     def player_y(self):
#         return self.__player.get_y()
#
#     def player_x(self):
#         return self.__player.get_x()
#
#     def set_room_block(self, y, x):
#         self.__map[y][x].set_block()
#
#     def west_room_available(self):
#         if self.movement_available(self.player_y(), self.player_x() - 1):
#             if self.__map[self.player_y()][self.player_x()-1].visited_status():
#                 print("room has been visited")
#                 return 1
#             else:
#                 print("room has not been visited")
#                 return 0
#         else:
#             print("room not available")
#             return 2
#
#     def block_west(self):
#         self.set_room_block(self.player_y(), self.player_x() - 1)
#         self.__map[self.player_y()][self.player_x() - 1].set_visited()
#
#     def move_west(self):
#         if self.movement_available(self.player_y(), self.player_x() - 1):
#             self.__player.move_west()
#             self.__map[self.player_y()][self.player_x()].set_visited()
#
#     def east_room_available(self):
#         if self.movement_available(self.player_y(), self.player_x() + 1):
#             if self.__map[self.player_y()][self.player_x()+1].visited_status():
#                 print("room has been visited")
#                 return 1
#             else:
#                 print("room has not been visited")
#                 return 0
#         else:
#             print("room not available")
#             return 2
#
#     def block_east(self):
#         self.set_room_block(self.player_y(), self.player_x() + 1)
#         self.__map[self.player_y()][self.player_x() + 1].set_visited()
#
#     def move_east(self):
#         if self.movement_available(self.player_y(), self.player_x() + 1):
#             self.__player.move_east()
#             self.__map[self.player_y()][self.player_x()].set_visited()
#
#     def north_room_available(self):
#         if self.movement_available(self.player_y() - 1, self.player_x()):
#             if self.__map[self.player_y()-1][self.player_x()].visited_status():
#                 print("room has been visited")
#                 return 1
#             else:
#                 print("room has not been visited")
#                 return 0
#         else:
#             print("room not available")
#             return 2
#
#     def block_north(self):
#         self.set_room_block(self.player_y() - 1, self.player_x())
#         self.__map[self.player_y() - 1][self.player_x()].set_visited()
#
#     def move_north(self):
#         if self.movement_available(self.player_y() - 1, self.player_x()):
#             self.__player.move_north()
#             self.__map[self.player_y()][self.player_x()].set_visited()
#
#     def south_room_available(self):
#         if self.movement_available(self.player_y() + 1, self.player_x()):
#             if self.__map[self.player_y()+1][self.player_x()].visited_status():
#                 print("room has been visited")
#                 return 1
#             else:
#                 print("room has not been visited")
#                 return 0
#         else:
#             print("room not available")
#             return 2
#
#     def block_south(self):
#         self.set_room_block(self.player_y() + 1, self.player_x())
#         self.__map[self.player_y() + 1][self.player_x()].set_visited()
#
#     def move_south(self):
#         if self.movement_available(self.player_y() + 1, self.player_x()):
#             self.__player.move_south()
#             self.__map[self.player_y()][self.player_x()].set_visited()
#
#     def reach_exit(self):
#         if self.player_x() == self.__width - 1 and self.player_y() == self.__height - 1:
#             return True
#         return False
#
#     def game_over(self):
#         if self.__map[self.player_y() + 1][self.player_x()].visited_status() and  self.__map[self.player_y() - 1][self.player_x()].visited_status() and  self.__map[self.player_y()][self.player_x()-1].visited_status() and  self.__map[self.player_y()][self.player_x() + 1].visited_status():
#             return True


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

    def get_player_info(self, name):
        pass

#
# def run():
#
#     map = Map()
#     map.generate_map()
#     map.generate_player()
#     map.print_map()
#
#
# if __name__ == "__main__":
#     run()