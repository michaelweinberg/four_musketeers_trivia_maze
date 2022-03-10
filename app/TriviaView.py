import tkinter
import tkinter as tk
import tkinter.messagebox


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
        self.name = None
        self.labelName = tk.Label(self.windows, text="User Name: ")
        self.varName = tk.StringVar()
        self.entryName = None

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

    def set_controller(self, controller):
        pass

    # def login(self):
    #     self.name = self.entryName.get()
    #
    # def welcome_page(self):
    #     self.varName.set("")
    #     self.labelName.place(x=240, y=300)
    #     self.entryName = tk.Entry(self.windows, textvariable=self.varName)
    #     self.entryName.place(x= 400, y=300)
    #     buttonOK = tk.Button(self.windows, text="START", command=self.login)
    #     buttonOK.place(x=300, y=400)
