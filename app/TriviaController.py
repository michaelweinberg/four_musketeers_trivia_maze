import pickle
import time
import threading
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
        self.cond = None
        self.windows = windows
        self.__player = Player()
        self.__map = None
        self.__view = TriviaView(windows, "640x640", "TriviaMaze", 64)
        self.__question = Question()
        self.__answer_status = None

    def start_new_game(self):
        """
        start a new game, set each room value to 0 as initial state,
        set the player to the start point, and redraw the maze in Tk.
        """
        new_map = [[Room(y, x) for x in range(6)] for y in range(6)]
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
        if self.__map.has_reached_exit():
            exit()
        if not self.__map.has_reach_exit(self.__player.get_y(), self.__player.get_x()) \
                and not self.__map.is_game_over(self.__player.get_y(), self.__player.get_x()):
            if self.get_answer_status():
                if event.keysym == "Left":
                    print("l")
                    self.__map.movement_available(self.__player.get_y(), self.__player.get_x()-1)
                    self.__map.enter_room(self.__player.get_y(), self.__player.get_x()-1, self.__player)
                if event.keysym == "Right":
                    print("r")
                    self.__map.movement_available(self.__player.get_y(), self.__player.get_x()+1)
                    self.__map.enter_room(self.__player.get_y(), self.__player.get_x() + 1, self.__player)
                if event.keysym == "Up":
                    self.__map.movement_available(self.__player.get_y()-1, self.__player.get_x())
                    self.__map.enter_room(self.__player.get_y() - 1, self.__player.get_x(), self.__player)
                if event.keysym == "Down":
                    self.__map.movement_available(self.__player.get_y()+1, self.__player.get_x())
                    self.__map.enter_room(self.__player.get_y() + 1, self.__player.get_x(), self.__player)
                # self.__map.generate_player()
            else:
                if event.keysym == "Left":
                    self.__map.wrong_answer_block_room(self.__player.get_y(), self.__player.get_x()-1, self.__player)
                if event.keysym == "Right":
                    print("r")
                    self.__map.wrong_answer_block_room(self.__player.get_y(), self.__player.get_x() + 1, self.__player)
                if event.keysym == "Up":
                    self.__map.wrong_answer_block_room(self.__player.get_y() - 1, self.__player.get_x(), self.__player)
                if event.keysym == "Down":
                    self.__map.wrong_answer_block_room(self.__player.get_y() + 1, self.__player.get_x(), self.__player)
    #     self.cond = threading.Condition()
    #     threading.Thread(target=self.move_step1(event)).start()
    #     threading.Thread(target=self.move_step2()).start()
    #
    # def move_step1(self, event):
    #     with self.cond:
    #         # for i in range(1):
    #         #     time.sleep(1)
    #         print(threading.currentThread().name,"move_step1")
    #         (question, answer) = self.__question.get_question()
    #         print(self.__question.get_question())
    #         self.__view.draw_question_box(question, answer)
    #         self.__view.draw_answer_box()
    #         # if i ==0:
    #         self.cond.wait()
    #         res = self.__view.answer_to_pass
    #         self.__map.enter_room2(self.__player, event, res)
    #         self.__player.__str__()
    #         self.__view.draw_maze_tk(self.__map.get_map())
    #
    # def move_step2(self):
    #     with self.cond:
    #         # for i in range(1):
    #         #     time.sleep(1)
    #         print(threading.currentThread().name, "move_step2")
    #         if self.__view.answer_to_pass != 0:
    #             print("get_answer_status in step2")
    #             print(self.__view.answer_to_pass)
    #             self.cond.notify()

    # def get_answer_status(self):
    #     (question, answer) = self.__question.get_question()
    #     print(self.__question.get_question())
    #     self.__view.draw_question_box(question, answer)
    #     self.__view.draw_answer_box()
    #     if self.__view.asking_question:
    #         print("asking question true")
    #         return
    #     else:
    #         print("asking question wrong")
    #
    #         print("get_answer_status")
    #         print(self.__view.answer_to_pass)
    #         if self.__view.answer_to_pass == 1:
    #             return True
    #         if self.__view.answer_to_pass == 2:
    #             return False
            


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



