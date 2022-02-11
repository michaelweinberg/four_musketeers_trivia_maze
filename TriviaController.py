from map import Map
from TriviaView import TriviaView


class TriviaController:
    def __init__(self, view):
        self.__map = Map()
        self.__map.generate_map()
        self.__map.generate_player()
        self.__map.print_map()
        self.__view = view
        # self.__model = model

    # def print_trivia_maze(self):
    #     return self.__view.print_map(self.__map)
    #
    # def update_map(self):
    #     pass
    #
    # def get_question_from_db(self):
    #     question_data = self.__model.get_question_list()
    #     return self.__view.print_question(question_data)

    def move_character(self):
        while not self.__map.reach_exit():
            input_var = input("Please enter w/s/a/d:")
            self.enter_room(input_var)
            self.__map.generate_player()
            self.__view.print_map(self.__map)

    def enter_room(self, move):
        if move == "a":
            self.__map.west_room_available()
            self.__map.move_west()
        if move == "d":
            self.__map.east_room_available()
            self.__map.move_east()
        if move == "w":
            self.__map.north_room_available()
            self.__map.move_north()
        if move == "s":
            self.__map.south_room_available()
            self.__map.move_south()


def run():
    view = TriviaView()
    newgame = TriviaController(view)
    newgame.move_character()


if __name__ == "__main__":
    run()



