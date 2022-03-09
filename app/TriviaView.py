import tkinter
import tkinter as tk


class TriviaView:
    def __init__(self, windows, size,title,s):
        self.windows = windows
        self.size = size
        self.title = title
        self.s = s
        self.windows.geometry(self.size)
        self.windows.title(string=self.title)
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.canvas.pack()
        self.asking_question = False
        self.question_text = tk.StringVar()
        self.answer_text = tk.StringVar()
        # self.question_box = tk.Label(self.windows, textvariable= self.question_text, wraplength=300)
        # self.answer_box = tk.Label(self.windows, textvariable= self.answer_text, wraplength=300)
        # self.button_true = tk.Button(self.windows, text="True",command=self.answered_true)
        # self.button_false = tk.Button(self.windows, text="False", command=self.answered_false)
        # self.button_true.place(x=-300, y=600)
        # self.button_false.place(x=-340, y=600)
        # self.question_box.place(x=100, y=450)
        self.question_text.set("Please use the arrow keys to move")
        self.answer_to_pass = 0
        self.answer = None
        
        # self.button_true["state"] == "disabled"
        # self.button_false["state"] == "disabled"
    #
    # def answered_true(self):
    #     # self.button_true["state"] == "disabled"
    #     # self.button_false["state"] == "disabled"
    #     self.button_true.place(x=-300, y=600)
    #     self.button_false.place(x=-340, y=600)
    #     self.asking_question = False
    #     self.question_text.set("Please use the arrow keys to move")
    #
    #
    #     if self.answer == True:
    #         # print("You are correct and you may enter")
    #         self.answer_text.set("You are correct and you may enter")
    #         self.answer_to_pass = 1
    #     else:
    #         # print("You are incorrect and the door is locked")
    #         self.answer_to_pass = 2
    #         self.answer_text.set("You are incorrect and the door is locked")
    #
    # def answered_false(self):
    #     # self.button_true["state"] == "disabled"
    #     # self.button_false["state"] == "disabled"
    #     self.button_true.place(x=-300, y=600)
    #     self.button_false.place(x=-340, y=600)
    #     self.asking_question = False
    #     self.question_text.set("Please use the arrow keys to move")
    #
    #
    #     if self.answer == False:
    #         # print("You are correct and you may enter")
    #         self.answer_text.set("You are correct and you may enter")
    #         self.answer_to_pass = 1
    #     else:
    #         # print("You are incorrect and the door is locked")
    #         self.answer_to_pass = 2
    #         self.answer_text.set("You are incorrect and the door is locked")
    #
    #
    # def draw_question_box(self, question, answer):
    #     # self.button_true["state"] == "normal"
    #     # self.button_false["state"] == "normal"
    #     self.button_true.place(x=300, y=600)
    #     self.button_false.place(x=340, y=600)
    #     self.question_text.set(question)
    #     # question_box = tk.Label(self.windows, text=str(question), wraplength=250)
    #
    #     self.asking_question = True
    #
    #     self.answer = answer



    def draw_answer_box(self):
        answer_box = tk.Label(self.windows, textvariable=self.answer_text, wraplength=300)
        answer_box.place(x=100, y=600)
        self.answer_text.set("")
        self.answer = None
        self.draw_answer()


    def answer_ture(self):
        if self.answer == True:
            self.answer_to_pass = 1
            self.asking_question = False
            self.answer_text.set("You are correct and you may enter")
        if self.answer == False:
            self.answer_to_pass = 2
            self.asking_question = False
            self.answer_text.set("You are incorrect and the door is locked")
        if self.answer == None:
            ValueError("answer not set")

    def answer_false(self):
        if self.answer == False:
            self.answer_to_pass = 1
            self.asking_question = False
            self.answer_text.set("You are correct and you may enter")
        if self.answer == True:
            self.answer_to_pass = 2
            self.asking_question = False
            self.answer_text.set("You are incorrect and the door is locked")
        if self.answer == None:
            ValueError("answer not set")


    def draw_question_box(self, question, answer):
        question_box = tk.Label(self.windows, bitmap="question", compound="left", text=question)
        question_box.place(x=100,y=450)
        self.answer = answer
        self.asking_question = True

    def draw_answer(self):
        button_true = tk.Button(self.windows, text="Ture", command=self.answer_ture)
        button_true.place(x=300,y=600)
        button_false = tk.Button(self.windows, text="False", command=self.answer_false)
        button_false.place(x=340,y=600)


    def reset_question_box(self):
        self.answer = None

    def callback(self):
        print("called~")

    def draw_menu(self, start_game_func):
        print("menu set up")
        menubase = tkinter.Menu(self.windows)
        menubar = tkinter.Menu(menubase, tearoff=False)
        menubar.add_command(label="Start Game",command=start_game_func)
        menubar.add_command(label="Continue Game",command=self.callback)
        menubar.add_command(label="Save Game",command=self.callback)
        menubar.add_command(label="Exit Game",command=self.windows.quit)
        menubase.add_cascade(label="Menu",menu=menubar)
        self.windows.config(menu=menubase)

    def draw_player(self, row, col, color="red"):
        cell_width = 100
        x0, y0 = col * cell_width, row * cell_width
        x1, y1 = x0 + cell_width, y0 + cell_width
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="green", width=10)

    def draw_cell(self, row, col, color="white"):
        cell_width = 100
        x0, y0 = col * cell_width, row * cell_width
        x1, y1 = x0 + cell_width, y0 + cell_width
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey", width=1)

    def draw_maze_tk(self, map):
        for y in range(1,5):
            for x in range(1,5):
                room = map[y][x]
                if room.visited_status():
                    self.draw_cell(room.get_y(), room.get_x(), "#8B0000")
                if room.get_value() == 0:  # empty room
                    self.draw_cell(room.get_y(), room.get_x())
                if room.get_value() == 4:  # blocked room
                    self.draw_cell(room.get_y(), room.get_x(), "black")
                if room.get_value() == 2:  # start of maze
                    self.draw_cell(room.get_y(), room.get_x(), "yellow")
                if room.get_value() == 3:  # end of maze
                    self.draw_cell(room.get_y(), room.get_x(), "blue")
                if room.get_value() == 10:  # hero in room
                    self.draw_cell(room.get_y(), room.get_x(), "red")



    def print_question(self, question):
        print("question:" + question)
