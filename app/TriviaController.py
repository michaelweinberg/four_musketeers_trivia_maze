import pickle
from Model import Question
from models.player import Player
from models.room import Room
from models.map import Map


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
        if self.__map.has_reach_exit(self.__player.get_y(), self.__player.get_x()):
            print("end")
            return
        if event.keysym == "Left":
            if not self.__map.movement_available(self.__player.get_y(), self.__player.get_x()-1):
                return
            self.__map.enter_room(self.__player.get_y(), self.__player.get_x()-1, self.__player, self.answering_question())
        if event.keysym == "Right":
            if not self.__map.movement_available(self.__player.get_y(), self.__player.get_x()+1):
                return
            self.__map.enter_room(self.__player.get_y(), self.__player.get_x() + 1, self.__player, self.answering_question())
        if event.keysym == "Up":
            if not self.__map.movement_available(self.__player.get_y()-1, self.__player.get_x()):
                return
            self.__map.enter_room(self.__player.get_y() - 1, self.__player.get_x(), self.__player, self.answering_question())
        if event.keysym == "Down":
            if not self.__map.movement_available(self.__player.get_y()+1, self.__player.get_x()):
                return
            self.__map.enter_room(self.__player.get_y() + 1, self.__player.get_x(), self.__player, self.answering_question())

        self.__player.__str__()
        self.__view.draw_maze_tk(self.__map.get_map())
        if self.__map.is_game_over(self.__player.get_y(), self.__player.get_x()):
            print("Game Over!")
            return

    def set_name(self, name):
        self.__player.set_name(name)

    def room_status(self, y, x):
        return self.__map[y][x].visited_status()

    def room_value(self, y, x):
        return self.__map[y][x].get_value()

    def player_y(self):
        return self.__player.get_y()

    def player_x(self):
        return self.__player.get_x()



