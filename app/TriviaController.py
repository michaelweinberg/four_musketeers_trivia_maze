import pickle

from Model import Question
from TriviaView import TriviaView
from models.player import Player
from models.room import Room
from models.map import Map


class TriviaController:
    def __init__(self, windows):
        """
        initial a 4x4 maze, a TriviaView to display the maze, a player module and question module
        :param windows: tkinter UI
        """
        self.windows = windows
        self.__player = Player()
        self.__map = None
        self.__view = TriviaView(windows, "640x640", "TriviaMaze", 64)
        self.__question = Question()

    def start_new_game(self):
        """
        start a new game, set each room value to 0 as initial state,
        set the player to the start point, and redraw the maze in Tk.
        """
        new_map = [[Room(y, x) for x in range(4)] for y in range(4)]
        self.__map = Map(new_map)
        self.__map.generate_map()
        self.__player.generate_player()
        self.__view.draw_maze_tk(self.__map.get_map())
        # self.__view.draw_question_box()
        self.__view.draw_menu(self.start_new_game)
        self.move()

    def move(self):
        """
        use keyboard left, right, up, down to control the player's movement.
        """
        self.windows.bind_all("<KeyPress-Left>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Right>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Up>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Down>", lambda event: self.move_character(event))

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

    def move_character(self, event):
        """
        get the input from the keyboard and move the player to the direction
        according to the input, call enter_west, enter_east, enter_north, enter_south
        then, if accessible, reprint the map with the player in the new room
        """
        if self.__view.asking_question:
            return
        # if self.__map.has_reached_exit():
        #     exit()
        if not self.__map.has_reach_exit(self.__player.get_y(), self.__player.get_x()) \
                and not self.__map.is_game_over(self.__player.get_y(), self.__player.get_x()):
            res = self.answer_question()
            if event.keysym == "Left":
                self.__map.enter_room(self.__player.get_y(), self.__player.get_x()-1, res, self.__player)
            if event.keysym == "Right":
                self.__map.enter_room(self.__player.get_y(), self.__player.get_x() + 1, res, self.__player)
            if event.keysym == "Up":
                self.__map.enter_room(self.__player.get_y() - 1, self.__player.get_x(), res, self.__player)
            if event.keysym == "Down":
                self.__map.enter_room(self.__player.get_y() + 1, self.__player.get_x(), res, self.__player)
            # self.__map.generate_player()
            self.__player.__str__()
            self.__view.draw_maze_tk(self.__map.get_map())
            # print(self.__question.get_question())
            (question, answer) = self.__question.get_question()
            self.__view.draw_question_box(question, answer)
            self.__view.draw_answer_box()
            
    def answer_question(self):
        return True
    #     """
    #     get question from the database and print it on the screen.
    #     if the player choose the right answer, return True
    #     if not, return False
    #     """
    #     self.__view.print_question(self.get_question_from_db()[0])
    #     if input("answer") == self.get_question_from_db()[1]:
    #         print("right answer")
    #         return True
    #     else:
    #         print("wrong answer")
    #         return False
    #     self.__view.draw_maze_tk(self.__map.get_map())
    #
    # def get_question_from_db(self):
    #     question_data = self.__question.get_question()
    #     question = [question_data[2], question_data[3]]
    #     return question
    #
    # def answer_question(self):
    #     # return True
    #     """
    #     get question from the database and print it on the screen.
    #     if the player choose the right answer, return True
    #     if not, return False
    #     """
    #     # self.__view.draw_question_box(self.get_question_from_db()[0])
    #     self.__view.draw_question_box("question?")
    #     self.__view.draw_answer()
    #     res = self.__view.answer()
    #
    #     # if input("answer") == self.get_question_from_db()[1]:
    #     if res == True:
    #         self.__view.reset_question_box()
    #         print("right answer")
    #         return True
    #     elif res == False:
    #         self.__view.reset_question_box()
    #         print("wrong answer")
    #         return False


    def click_handler(self, name):
        print(name.get() + " is moving")

    def set_name(self):
        name = input("Please enter your name:\n")
        self.__player.set_name(name)

    def room_status(self, y, x):
        return self.__map[y][x].visited_status()

    def room_value(self, y, x):
        return self.__map[y][x].get_value()


    def player_y(self):
        return self.__player.get_y()

    def player_x(self):
        return self.__player.get_x()



