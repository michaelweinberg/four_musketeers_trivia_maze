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
    def sample_Q(self):
        print("QUESTION")

    def move_character(self):
        while not self.__map.reach_exit():
            input_var = input("Please enter w/s/a/d:")
            self.enter_room(input_var)
            self.__map.generate_player()
            self.__view.print_map(self.__map)

    def enter_room(self, move):
        if move == "a":
            if self.__map.west_room_available() != 2:
                if self.__map.west_room_available() == 0:
                    self.sample_Q()
                self.__map.move_west()
        if move == "d":
            if self.__map.east_room_available() != 2:
                if self.__map.east_room_available() == 0:
                    self.sample_Q()
                self.__map.move_east()
        if move == "w":
            if self.__map.north_room_available() != 2:
                if self.__map.north_room_available() == 0:
                    self.sample_Q()
                self.__map.move_north()
        if move == "s":
            if self.__map.south_room_available() != 2:
                if self.__map.south_room_available() == 0:
                    self.sample_Q()
                self.__map.move_south()

    def get_room_info(self):
        current_room = self.__map.get_room(self.__map.player_y(), self.__map.player_x())
        return current_room.get_value()

    def get_map(self):
        return self.__map

def run():
    view = TriviaView()
    newgame = TriviaController(view)
    newgame.move_character()


if __name__ == "__main__":
    run()



