

class Map:
    """
    a class to organize multiple rooms
    """

    def __init__(self, new_map):
        self.__width = 6
        self.__height = 6
        self.__start = None
        self.__destination = None
        self.__map = new_map

    def get_map(self):
        return self.__map

    def generate_map(self):
        """
        generate the map with start and destination
        also add padding area around the map set padding room with value 11
        """
        for row in self.__map:
            for room in row:
                room.set_value(11) #padding room added
        for y in range(1, self.__height - 1):
            for x in range(1, self.__width - 1):
                self.__map[y][x].set_value(0)
        for row in self.__map:
            for room in row:
                if room.get_value()==11:
                    room.set_wall()
        self.__start = self.__map[1][1]
        self.__start.set_start()
        self.__destination = self.__map[self.__height - 2][self.__width - 2]
        self.__destination.set_destination()

    def movement_available(self, y, x):
        print("check room available")
        if x in range(1, self.__width-1) and y in range(1, self.__height-1) \
                and self.__map[y][x].get_value() != 4 \
                and not self.__map[y][x].visited_status():
            print("room available")
            return True
        else:
            print("not available")
            return False

    def block_room(self, y, x):
        """
        block the room(y,x)
        """
        self.__map[y][x].set_block()
        self.__map[y][x].set_visited()

    def has_reach_exit(self, y, x):
        """check if the player has reached the destination"""
        if x == self.__width - 2 and y == self.__height - 2:
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

    def enter_room(self, y, x, player):
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
                print("room has not been visited answer right")
                self.__map[player.get_y()][player.get_x()].set_value(5)
                player.move(y, x)
                player.set_score(10)
                self.__map[y][x].set_value(10)
                self.__map[player.get_y()][player.get_x()].set_visited()
                self.__map[player.get_y()][player.get_x()].set_question_status_true()

    def wrong_answer_block_room(self, y, x, player):
        print("room has not been visited answer wrong")
        player.set_score(-10)
        self.block_room(y, x)
        self.__map[y][x].set_question_status_false()

    def enter_room2(self, player, event, res):
        if not self.has_reach_exit(player.get_y(), player.get_x()) \
                and not self.is_game_over(player.get_y(), player.get_x()):
            if res ==1:
                if event.keysym == "Left":
                    print("l")
                    self.enter_room(player.get_y(), player.get_x() - 1, player)
                if event.keysym == "Right":
                    print("r")
                    self.enter_room(player.get_y(), player.get_x() + 1, player)
                if event.keysym == "Up":
                    self.enter_room(player.get_y() - 1, player.get_x(), player)
                if event.keysym == "Down":
                    self.enter_room(player.get_y() + 1, player.get_x(), player)
                # self.__map.generate_player()
            elif res == 2:
                if event.keysym == "Left":
                    self.wrong_answer_block_room(player.get_y(), player.get_x() - 1, player)
                if event.keysym == "Right":
                    print("r")
                    self.wrong_answer_block_room(player.get_y(), player.get_x() + 1, player)
                if event.keysym == "Up":
                    self.wrong_answer_block_room(player.get_y() - 1, player.get_x(), player)
                if event.keysym == "Down":
                    self.wrong_answer_block_room(player.get_y() + 1, player.get_x(), player)


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