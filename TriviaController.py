from model import Question
from TriviaView import TriviaView
from player import Player
from room import Room


class TriviaController:
    def __init__(self, width=4, height=4):
        self.__width = width
        self.__height = height
        self.__start = None
        self.__destination = None
        self.__map = None
        self.__player = Player()
        self.__view = TriviaView()
        self.__question = Question()

    def generate_map(self):
        """generate the map with start and destination"""
        self.__map = [[Room(y, x) for x in range(self.__width)] for y in range(self.__height)]
        self.__start = self.__map[0][0]
        self.__start.set_start()
        self.__destination = self.__map[self.__height - 1][self.__width - 1]
        self.__destination.set_destination()

    def generate_player(self):
        """generate the player at the start point"""
        x = self.__player.get_x()
        y = self.__player.get_y()
        self.__map[y][x].set_value(10)

    def movement_available(self, y, x):
        """
        check if the room(y,x) is in range of the map and is not blocked
        :return:
        :return true if the room is in range and not blocked
        :return false if the room is not in range or blocked
        """
        if x in range(0, self.__width) and y in range(0, self.__height) and self.__map[y][x].get_value() != 4:
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

    def block_room(self, y, x):
        """
        block the room(y,x)
        """
        self.__map[y][x].set_block()
        self.__map[y][x].set_visited()

    def reach_exit(self):
        """check if the player has reached the destination"""
        if self.__player.get_x() == self.__width - 1 and self.__player.get_y() == self.__height - 1:
            return True
        return False

    def game_over(self):
        """check if there is not room available to move, end the game"""
        if not self.movement_available(self.player_y() + 1, self.player_x()) and \
                not self.movement_available(self.player_y() - 1, self.player_x()) and \
                not self.movement_available(self.player_y(), self.player_x()-1) and \
                not self.movement_available(self.player_y(), self.player_x() + 1):
            print("No room available,\n Game Over!")
            return True

    def get_question_from_db(self):
        # question_data = self.__question.get_question()
        question_data = ["question", "answer"]
        return question_data

    def move_character(self):
        """
        get the input from the keyboard and move the player to the direction
        according to the input, call enter_west, enter_east, enter_north, enter_south
        then, if accessible, reprint the map with the player in the new room
        """
        while not self.reach_exit() and not self.game_over():
            input_var = input("Please enter w/s/a/d:")
            if input_var == "a":
                self.enter_west()
            if input_var == "d":
                self.enter_east()
            if input_var == "w":
                self.enter_north()
            if input_var == "s":
                self.enter_south()
            self.generate_player()
            self.__view.print_map(self.__map)

    def answer_question(self):
        """
        get question from the database and print it on the screen.
        if the player choose the right answer, return True
        if not, return False
        """
        self.__view.print_question(self.get_question_from_db()[0])
        if input("answer") == self.get_question_from_db()[1]:
            print("right answer")
            return True
        else:
            print("wrong answer")
            return False

    def enter_west(self):
        """
        move the player to the room on the west
        check to see if the room on the east is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.movement_available(self.__player.get_y(), self.__player.get_x() - 1):
            if self.__map[self.__player.get_y()][self.__player.get_x() - 1].visited_status():
                print("room has been visited")
            else:
                print("room has not been visited")
                res = self.answer_question()
                if res:
                    self.__player.move_west()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                if not res:
                    self.block_room(self.player_y(), self.player_x() - 1)
        else:
            print("room not available")

    def enter_east(self):
        """
        move the player to the room on the east
        check to see if the room on the east is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.movement_available(self.__player.get_y(), self.__player.get_x() + 1):
            if self.__map[self.__player.get_y()][self.__player.get_x() + 1].visited_status():
                print("room has been visited")
            else:
                print("room has not been visited")
                res = self.answer_question()
                if res:
                    self.__player.move_east()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                if not res:
                    self.block_room(self.player_y(), self.player_x() + 1)
        else:
            print("room not available")

    def enter_north(self):
        """
        move the player to the room on the north
        check to see if the room on the north is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.movement_available(self.__player.get_y() - 1, self.__player.get_x()):
            if self.__map[self.__player.get_y() - 1][self.__player.get_x()].visited_status():
                print("room has been visited")
            else:
                print("room has not been visited")
                res = self.answer_question()
                if res:
                    self.__player.move_north()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                if not res:
                    self.block_room(self.player_y()-1, self.player_x())
        else:
            print("room not available")

    def enter_south(self):
        """
        move the player to the room on the south
        check to see if the room on the south is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.movement_available(self.__player.get_y() + 1, self.__player.get_x()):
            if self.__map[self.__player.get_y() + 1][self.__player.get_x()].visited_status():
                print("room has been visited")
            else:
                print("room has not been visited")
                res = self.answer_question()
                if res:
                    self.__player.move_south()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                if not res:
                    self.block_room(self.player_y()+1, self.player_x())
        else:
            print("room not available")

    def get_map(self):
        return self.__map

    def print_map(self):
        self.__view.print_map(self.__map)


def run():
    newgame = TriviaController()
    newgame.generate_map()
    newgame.generate_player()
    newgame.print_map()
    newgame.move_character()


if __name__ == "__main__":
    run()



