from map import Map


class TriviaController:
    def __init__(self, model, view):
        self.__map = Map()
        self.__view = view
        self.__model = model

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
        self.__map.move_player()