

class Map:
    """
    a class to organize multiple rooms
    """

    def __init__(self, new_map):
        self.__width = 4
        self.__height = 4
        self.__start = None
        self.__destination = None
        self.__map = new_map

    def get_map(self):
        return self.__map

    # def print_map(self):
    #     """show the map in the console"""
    #     for row in self.__map:
    #         show_spot = ""
    #         for room in row:
    #             if room.get_value() == 0:
    #                 show_spot += " ."
    #             elif room.get_value() == 1:
    #                 show_spot += " □"
    #             elif room.get_value() == 2:
    #                 show_spot += " S"
    #             elif room.get_value() == 3:
    #                 show_spot += " D"
    #             elif room.get_value() == 10:
    #                 show_spot += " ▲"
    #         print(show_spot)
    #     print(" ")

    def generate_map(self):
        """generate the map with start and destination"""
        for row in self.__map:
            for room in row:
                room.set_value(0)
        self.__start = self.__map[0][0]
        self.__start.set_start()
        self.__destination = self.__map[self.__height - 1][self.__width - 1]
        self.__destination.set_destination()

    def movement_available(self, y, x):
        if x in range(0, self.__width) and y in range(0, self.__height) \
                and self.__map[y][x].get_value() != 4 and not self.__map[y][x].visited_status():
            return True
        else:
            return False

    def block_room(self, y, x):
        """
        block the room(y,x)
        """
        self.__map[y][x].set_block()
        self.__map[y][x].set_visited()

    def has_reach_exit(self, y, x):
        """check if the player has reached the destination"""
        if x == self.__width - 1 and y == self.__height - 1:
            return True
        return False

    def is_game_over(self, y, x):
        """check if there is not room available to move, end the game"""
        if not self.movement_available(y + 1, x) and \
                not self.movement_available(y - 1, x) and \
                not self.movement_available(y, x-1) and \
                not self.movement_available(y, x + 1):
            print("No room available,\n Game Over!")
            return True

    def room_status(self, y, x):
        return self.__map[y][x].visited_status()

    def get_room(self, y, x):
        room = self.__map[y][x]
        return room

    def enter_room(self, y, x, res, player):
        """
        move the player to the room on the west
        check to see if the room on the east is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.movement_available(y, x):
            if self.__map[y][x].visited_status():
                print("room has been visited")
            else:
                print("room has not been visited")
                # res = self.answer_question()
                if res is True:
                    self.__map[player.get_y()][player.get_x()].set_value(5)
                    player.move(y, x)
                    player.set_score(10)
                    self.__map[y][x].set_value(10)
                    self.__map[player.get_y()][player.get_x()].set_visited()
                    self.__map[player.get_y()][player.get_x()].set_question_status_true()
                if res is False:
                    player.set_score(-10)
                    self.block_room(y, x)
                    self.__map[y][x].set_question_status_false()
        else:
            print("room not available")

#
# def run():
#
#     map = Map()
#     map.generate_map()
#     map.generate_player()
#     map.print_map()
#     map.move_player()
#
#
# if __name__ == "__main__":
#     run()