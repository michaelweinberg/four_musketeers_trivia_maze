import pickle

from Model import Question
from TriviaView import TriviaView
from models.player import Player
from models.room import Room


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

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def click_handler(self, name):
        print(name.get() + " is moving")

    def set_name(self):
        name = input("Please enter your name:\n")
        self.__player.set_name(name)

    def generate_map(self):
        """generate the map with start and destination"""
        self.__map = [[Room(y, x) for x in range(self.__width)] for y in range(self.__height)]
        self.__start = self.__map[0][0]
        self.__start.set_start()
        self.__destination = self.__map[self.__height - 1][self.__width - 1]
        self.__destination.set_destination()

    def generate_player(self):
        """generate the player"""
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
        if x in range(0, self.__width) and y in range(0, self.__height) \
                and self.__map[y][x].get_value() != 4 and not self.__map[y][x].visited_status():
            return True
        else:
            return False

    def room_status(self, y, x):
        return self.__map[y][x].visited_status()

    def room_value(self, y, x):
        return self.__map[y][x].get_value()

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

    def store_current_game(self):
        map = self.__map
        player = self.__player
        fw = open("triviaDataFile.txt", "wb")
        pickle.dump(map, fw, -1)
        pickle.dump(player, fw)
        fw.close()

    def recover_previous_game(self):
        fr = open("triviaDataFile.txt", "rb")
        self.__map = pickle.load(fr)
        self.__player = pickle.load(fr)
        fr.close()

    def move_character(self):
        """
        get the input from the keyboard and move the player to the direction
        according to the input, call enter_west, enter_east, enter_north, enter_south
        then, if accessible, reprint the map with the player in the new room
        """
        while not self.reach_exit() and not self.game_over():
            input_var = input("Please enter w/s/a/d(press u if you want to quit and store current game):\n")
            if input_var == "a":
                self.enter_west()
            if input_var == "d":
                self.enter_east()
            if input_var == "w":
                self.enter_north()
            if input_var == "s":
                self.enter_south()
            if input_var == "u":
                self.store_current_game()
                self.start_menu()
            self.generate_player()
            self.__player.__str__()
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
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_value(5)
                    self.__player.move_west()
                    self.__player.set_score(10)
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_question_status_true()
                if not res:
                    self.__player.set_score(-10)
                    self.block_room(self.player_y(), self.player_x() - 1)
                    self.__map[self.__player.get_y()][self.__player.get_x()-1].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x()-1].set_question_status_false()
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
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_value(5)
                    self.__player.move_east()
                    self.__player.set_score(10)
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_question_status_true()
                if not res:
                    self.__player.set_score(-10)
                    self.block_room(self.player_y(), self.player_x() + 1)
                    self.__map[self.__player.get_y()][self.__player.get_x() + 1].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x() + 1].set_question_status_false()
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
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_value(5)
                    self.__player.move_north()
                    self.__player.set_score(10)
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_question_status_true()
                if not res:
                    self.__player.set_score(-10)
                    self.block_room(self.player_y()-1, self.player_x())
                    self.__map[self.__player.get_y() - 1][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y() - 1][self.__player.get_x()].set_question_status_false()
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
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_value(5)
                    self.__player.move_south()
                    self.__player.set_score(10)
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y()][self.__player.get_x()].set_question_status_true()
                if not res:
                    self.__player.set_score(-10)
                    self.block_room(self.player_y()+1, self.player_x())
                    self.__map[self.__player.get_y() + 1][self.__player.get_x()].set_visited()
                    self.__map[self.__player.get_y() + 1][self.__player.get_x()].set_question_status_false()
        else:
            print("room not available")

    def get_map(self):
        return self.__map

    def print_map(self):
        self.__view.print_map(self.__map)

    def print_guimap(self):
        self.__view.draw_maze_tk(self.__map)

    def start_menu(self):
        while True:
            menu = input("New Game: 1\nContinue Game: 2\nCheck Score List:3\nQuit The Game:4\nPlease Enter:\n")
            if menu == "1":
                self.generate_map()
                self.generate_player()
                self.set_name()
                self.print_map()
                self.move_character()
            if menu == "2":
                try:
                    self.recover_previous_game()
                    self.print_map()
                    self.move_character()
                except OSError:
                    print("not exist!\nPlease try again!\n")
                # finally:
                #     self.start_menu()
                # name = input("name:\n")
                # game_from_db = self.__question.get_game_info(name)
                # self.__map = game_from_db.map
                # self.__player = game_from_db.player
                self.print_map()
                self.move_character()
            if menu == "3":
                score_list = self.__question.get_score_list()
                print(score_list)
            if menu == "4":
                quit()

    def run(self):
        self.generate_map()
        self.generate_player()
        self.set_name()
        self.print_map()
        self.move_character()
        # newgame.print_guimap()


if __name__ == "__main__":
    newgame = TriviaController()
    newgame.start_menu()



