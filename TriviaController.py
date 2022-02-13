from model import Map, Question
from TriviaView import TriviaView


class TriviaController:
    def __init__(self):
        self.__map = Map()
        self.__map.generate_map()
        self.__map.generate_player()
        self.__map.print_map()
        self.__view = TriviaView()
        self.__question = Question()

    # def print_trivia_maze(self):
    #     return self.__view.print_map(self.__map)
    #
    # def update_map(self):
    #     pass
    #
    def get_question_from_db(self):
        # question_data = self.__question.get_question()
        question_data = ["question", "answer"]
        return question_data

    def move_character(self):
        while not self.__map.reach_exit():
            input_var = input("Please enter w/s/a/d:")
            self.enter_room(input_var)
            self.__map.generate_player()
            self.__view.print_map(self.__map)

    def answer_question(self):
        self.__view.print_question(self.get_question_from_db()[0])
        if input("answer") == self.get_question_from_db()[1]:
            print("right answer")
            return True
        else:
            print("wrong answer")
            return False

    def enter_room(self, move):
        if move == "a":
            if self.__map.west_room_available() != 2:
                if self.__map.west_room_available() == 0:
                    self.answer_question()
                self.__map.move_west()
        if move == "d":
            if self.__map.east_room_available() != 2:
                if self.__map.east_room_available() == 0:
                    self.answer_question()
                self.__map.move_east()
        if move == "w":
            if self.__map.north_room_available() != 2:
                if self.__map.north_room_available() == 0:
                    self.answer_question()
                self.__map.move_north()
        if move == "s":
            if self.__map.south_room_available() != 2:
                if self.__map.south_room_available() == 0:
                    self.answer_question()
                self.__map.move_south()

    def get_room_info(self):
        current_room = self.__map.get_room(self.__map.player_y(), self.__map.player_x())
        return current_room.get_value()

    def get_map(self):
        return self.__map


def run():
    newgame = TriviaController()
    newgame.move_character()


if __name__ == "__main__":
    run()



