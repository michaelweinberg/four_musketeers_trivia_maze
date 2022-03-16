import pickle
from Model import Question
from models.player import Player
from models.room import Room
from models.map import Map
import tkinter as tk
import util.model_functions as mf
import pygame
from pygame import mixer


class TriviaController:
    def __init__(self, view):
        """
        initial a 4x4 maze, a TriviaView to display the maze, a player module and question module
        :param view: tkinter UI
        """
        self.__player = Player()
        self.__map = None
        self.__view = view
        self.windows = self.__view.windows
        self.__question = Question()
        self.__answer_status = None

    def start_new_game(self, name):
        """
        start a new game, set each room value to 0 as initial state,
        set the player to the start point, and redraw the maze in Tk.
        """
        new_map = [[Room(y, x) for x in range(6)] for y in range(6)]
        self.__map = Map(new_map)
        self.__map.generate_map()
        self.__player.generate_player(name)
        self.__view.draw_maze_tk(self.__map.get_map())
        # self.__view.draw_question_box()
        self.__view.draw_menu(self.start_new_game)
        self.move()

    def login(self):
        self.__view.canvas.destroy()
        self.__view.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.__view.canvas.pack()
        self.__player.name = self.__view.entryName.get()
        self.set_name(self.__player.name)
        self.start_new_game(self.__player.name)
        self.__view.entryName.destroy()
        self.__view.labelName.destroy()
        self.__view.buttonOK.destroy()

    def restart_game(self):
        self.__view.canvas.destroy()
        self.__view.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.__view.canvas.pack()
        self.__view.buttonNewGame.destroy()
        self.__view.buttonExit.destroy()
        self.start_new_game(self.__player.get_name())

    def move(self):
        """
        use keyboard left, right, up, down to control the player's movement.
        """
        self.windows.bind_all("<KeyPress-Left>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Right>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Up>", lambda event: self.move_character(event))
        self.windows.bind_all("<KeyPress-Down>", lambda event: self.move_character(event))

    def store_current_game(self):
        map = self.__map
        player = self.__player
        fw = open(str(self.__player.get_name() + ".txt"), "wb")
        pickle.dump(map, fw, -1)
        pickle.dump(player, fw)
        fw.close()

    def recover_previous_game(self, file):
        # fr = open(str(self.__player.get_name() + ".txt"), "rb")
        fr = open(file, "rb")
        self.__map = pickle.load(fr)
        self.__player = pickle.load(fr)
        fr.close()
        self.__view.draw_maze_tk(self.__map.get_map())
        self.__view.draw_menu(self.recover_previous_game)
        self.move()

    def answering_question(self):
        (question, answer) = self.__question.get_question()
        print(self.__question.get_question())
        res = self.__view.messagebox_question(question, answer)
        return res

    def move_character(self, event):
        """
        get the input from the keyboard and move the player to the direction
        according to the input, call enter_west, enter_east, enter_north, enter_south
        then, if accessible, reprint the map with the player in the new room
        """
        if event.keysym == "Left":
            if not self.__map.movement_available(self.__player.get_y(), self.__player.get_x()-1):
                return
            self.enter_room(self.__player.get_y(), self.__player.get_x()-1, self.answering_question())
        if event.keysym == "Right":
            if not self.__map.movement_available(self.__player.get_y(), self.__player.get_x()+1):
                return
            self.enter_room(self.__player.get_y(), self.__player.get_x() + 1, self.answering_question())
        if event.keysym == "Up":
            if not self.__map.movement_available(self.__player.get_y()-1, self.__player.get_x()):
                return
            self.enter_room(self.__player.get_y() - 1, self.__player.get_x(), self.answering_question())
        if event.keysym == "Down":
            if not self.__map.movement_available(self.__player.get_y()+1, self.__player.get_x()):
                return
            self.enter_room(self.__player.get_y() + 1, self.__player.get_x(), self.answering_question())

        self.__player.__str__()
        self.__view.draw_maze_tk(self.__map.get_map())
        if self.__map.has_reach_exit(self.__player.get_y(), self.__player.get_x()):
            self.__view.win_game_page()
            print("end")
            return
        if self.__map.is_game_over(self.__player.get_y(), self.__player.get_x()):
            self.__view.game_over_page()
            print("Game Over!")
            return

    def enter_room(self, y, x, answer):
        """
        move the player to the room on the west
        check to see if the room on the east is available to move in.
        check if the room is in range of the map and not blocked.
        check the room status whether it is visited or not.
        """
        if self.__map.movement_available(y, x):
            cur_room = self.__map.get_room(self.__player.get_y(), self.__player.get_x())
            if self.__map.has_reach_exit(y, x):
                cur_room.set_value(5)
                self.__player.move(y, x)
                self.__map.get_room(y, x).set_value(10)
                print("Congratulation!")
                return
            elif answer is True:
                if cur_room.get_value() != 2:
                    cur_room.set_value(5)
                self.__player.move(y, x)
                self.__player.set_score(10)
                self.__map.get_room(y, x).set_value(10)
                self.__map.get_room(y, x).set_visited()
                self.__map.get_room(y, x).set_question_status_true()
            elif answer is False:
                print("room has not been visited answer wrong")
                self.__player.set_score(-10)
                self.__map.block_room(y, x)
                self.__map.get_room(y, x).set_question_status_false()

    def set_name(self, name):
        self.__player.set_name(name)

    def get_map(self):
        return self.__map
