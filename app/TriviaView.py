import tkinter
import tkinter as tk
import tkinter.messagebox


class TriviaView:
    def __init__(self, windows, size, title, s):
        self.windows = windows
        self.size = size
        self.title = title
        self.s = s
        self.windows.geometry(self.size)
        self.windows.title(string=self.title)
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.canvas.pack()
        self.name = None
        self.labelName = tk.Label(self.windows, text="User Name: ")
        self.varName = tk.StringVar()
        self.entryName = None
        self.controller = None
        self.buttonOK = None
        self.buttonNewGame = None
        self.buttonExit = None

    def messagebox_question(self, question, answer):
        print("messagebox start")
        txt = tk.messagebox.askyesno("Question", question)
        if txt == answer:
            print("message box return true")
            return True
        else:
            print("message box return false")
            return False

    def callback(self):
        print("called~")

    def save(self):
        if self.controller:
            self.controller.store_current_game()

    def load_game(self):
        if self.controller:
            self.controller.recover_previous_game()
            self.destroy_buttons()

    def draw_menu(self, start_game_func):
        print("menu set up")
        menubase = tkinter.Menu(self.windows)
        menubar = tkinter.Menu(menubase, tearoff=False)
        menubar.add_command(label="Start Game", command=start_game_func)
        menubar.add_command(label="Continue Game", command=self.load_game)
        menubar.add_command(label="Save Game", command=self.save)
        menubar.add_command(label="Exit Game", command=self.windows.quit)
        menubase.add_cascade(label="Menu", menu=menubar)
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

    def set_controller(self, controller):
        self.controller = controller

    def login(self):
        self.name = self.entryName.get()
        self.controller.set_name(self.name)
        self.controller.start_new_game(self.name)
        self.destroy_buttons()

    def destroy_buttons(self):
        self.entryName.destroy()
        self.labelName.destroy()
        self.buttonOK.destroy()
        self.buttonLoad.destroy()

    def welcome_page(self):
        # welcome_image = tk.PhotoImage(file='welcome.gif')
        # image = self.canvas.create_image(0, 0, anchor='nw', image=welcome_image)
        # image.pack(side='top')
        self.varName.set("")
        self.labelName.place(x=200, y=300)
        self.entryName = tk.Entry(self.windows, textvariable=self.varName)
        self.entryName.place(x=280, y=300)
        self.buttonOK = tk.Button(self.windows, text="START GAME", command=self.login)
        self.buttonOK.place(x=150, y=350)
        self.buttonLoad = tk.Button(self.windows, text="LOAD GAME", command=self.load_game)
        self.buttonLoad.place(x=350, y=350)

    def win_game_page(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.canvas.pack()
        self.buttonNewGame = tk.Button(self.windows, text="Start A New Game!", command=self.restart_game)
        self.buttonNewGame.place(x=235, y=235)
        self.buttonExit = tk.Button(self.windows, text="Exit", command=exit)
        self.buttonExit.place(x=270, y=300)

    def game_over_page(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.canvas.pack()
        self.buttonNewGame = tk.Button(self.windows, text="Start A New Game!", command=self.restart_game)
        self.buttonNewGame.place(x=235, y=235)
        self.buttonExit = tk.Button(self.windows, text="Exit", command=exit)
        self.buttonExit.place(x=270, y=300)

    def restart_game(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        self.canvas.pack()
        self.buttonNewGame.destroy()
        self.buttonExit.destroy()
        self.controller.start_new_game()