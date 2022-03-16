import tkinter
import tkinter as tk
import tkinter.messagebox
import math
from tkinter.filedialog import askopenfilename

import PIL
from PIL import ImageTk
from PIL.Image import Image


class TriviaView:
    boxopenim = None
    boxblockim = None
    boxcloseim = None
    imgclose = None
    imgblocked = None
    imgopen = None
    imglist = None
    imghero = None
    heroim = None
    startim = None
    imgstart = None
    endim = None
    imgend = None
    imgwin = None
    winim = None
    loseim = None
    imglose = None
    welcomeim = None
    imgwelcome = None

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
        self.imglist = []

    def messagebox_question(self, question, answer):
        print("messagebox start")
        txt = tk.messagebox.askyesno("Question", question)
        if txt == answer:
            print("message box return true")
            return True
        else:
            print("message box return false")
            return False

    def save(self):
        if self.controller:
            self.controller.store_current_game()

    def load_game(self):
        if self.controller:
            file = askopenfilename(title="Please choose your file", filetypes=[('txt', '*.txt')])
            # self.name = self.entryName.get()
            # self.controller.set_name(self.name)
            self.controller.recover_previous_game(file)
            self.destroy_buttons()

    def instructions(self):
        tkinter.messagebox.showinfo("How to play this game:", "Navigate maze from Start to Finish using arrow keys.\n"
                            "You will need to answer one trivia question correctly to pass through each door.\n"
                            "If the question is answered incorrectly, that door will permanently lock.\n"
                            "If you are able to reach the End, you will have won the game!")
        
    def about(self):
        tkinter.messagebox.showinfo("Welcome to Winter Olympics Trivia Game!", "Brought to you by the Four Musketeers")
        
    def draw_menu(self, start_game_func):
        print("menu set up")
        menubase = tkinter.Menu(self.windows)
        filemenu = tkinter.Menu(menubase, tearoff=False)
        filemenu.add_command(label="Start Game", command=start_game_func)
        filemenu.add_command(label="Continue Game", command=self.load_game)
        filemenu.add_command(label="Save Game", command=self.save)
        filemenu.add_command(label="Exit Game", command=self.windows.quit)
        menubase.add_cascade(label="File",menu=filemenu)
        # help menu object
        helpmenu = tkinter.Menu(menubase, tearoff=False)
        helpmenu.add_command(label="Game Play Instructions", command=self.instructions)
        helpmenu.add_command(label="About", command=self.about)
        menubase.add_cascade(label="Help", menu=helpmenu)
        self.windows.config(menu=menubase)

    def draw_maze_tk(self, map):
        global boxcloseim, imgclose, imglist, boxblockedim, imgblocked, boxopenim, imgopen, imghero, heroim, startim, imgstart, endim, imgend
        for y in range(1, 5):
            for x in range(1, 5):
                room = map[y][x]
                if room.visited_status():
                    boxopenim = PIL.Image.open(r"boxopen1.png")
                    imgopen = ImageTk.PhotoImage(boxopenim)
                    self.imglist.append(imgopen)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imgopen)
                if room.get_value() == 0:  # empty room
                    print("emptyroom")
                    boxcloseim = PIL.Image.open(r"boxclose1.png")
                    imgclose = ImageTk.PhotoImage(boxcloseim)
                    self.imglist.append(imgclose)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imgclose)
                if room.get_value() == 4:  # blocked room
                    boxblockedim = PIL.Image.open(r"boxlocked1.png")
                    imgblocked = ImageTk.PhotoImage(boxblockedim)
                    self.imglist.append(imgblocked)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imgblocked)
                if room.get_value() == 2:  # start of maze
                    startim = PIL.Image.open(r"start.png")
                    imgstart = ImageTk.PhotoImage(startim)
                    self.imglist.append(imgstart)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imgstart)
                if room.get_value() == 3:  # end of maze
                    endim = PIL.Image.open(r"end1.png")
                    imgend = ImageTk.PhotoImage(endim)
                    self.imglist.append(imgend)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imgend)
                if room.get_value() == 10:  # hero in room
                    heroim = PIL.Image.open(r"player.png")
                    imghero = ImageTk.PhotoImage(heroim)
                    self.imglist.append(imghero)
                    self.canvas.create_image(x * 100, y * 100, anchor="nw", image=imghero)

    def set_controller(self, controller):
        self.controller = controller

    # def login(self):
    #     self.name = self.entryName.get()
    #     self.controller.set_name(self.name)
    #     self.controller.start_new_game(self.name)
    #     self.destroy_buttons()

    def destroy_buttons(self):
        self.entryName.destroy()
        self.labelName.destroy()
        self.buttonOK.destroy()
        # self.buttonLoad.destroy()

    def welcome_page(self):
        global welcomeim, imgwelcome
        welcomeim = PIL.Image.open(r"welcome.png")
        imgwelcome = ImageTk.PhotoImage(welcomeim)
        self.canvas.create_image(320, 150, anchor="center", image=imgwelcome)
        self.canvas.pack()
        self.draw_star()
        self.varName.set("")
        self.labelName.place(x=200, y=300)
        self.entryName = tk.Entry(self.windows, textvariable=self.varName)
        self.entryName.place(x=280, y=300)
        self.buttonOK = tk.Button(self.windows, text="START GAME", command=self.controller.login)
        self.buttonOK.place(x=260, y=350)
        # self.buttonLoad = tk.Button(self.windows, text="LOAD GAME", command=self.load_game)
        # self.buttonLoad.place(x=350, y=350)

    def win_game_page(self):
        global imgwin, winim
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        winim = PIL.Image.open(r"win1.png")
        imgwin = ImageTk.PhotoImage(winim)
        self.canvas.create_image(310, 250, anchor="center", image=imgwin)
        self.canvas.pack()
        self.buttonNewGame = tk.Button(self.windows, text="Start A New Game!", command=self.controller.restart_game)
        self.buttonNewGame.place(x=235, y=235)
        self.buttonExit = tk.Button(self.windows, text="Exit", command=exit)
        self.buttonExit.place(x=270, y=300)

    def game_over_page(self):
        global loseim, imglose
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.windows, background=None, width=640, height=640)
        loseim = PIL.Image.open(r"lose1.png")
        imglose = ImageTk.PhotoImage(loseim)
        self.canvas.create_image(310, 250, anchor="center", image=imglose)
        self.canvas.pack()
        self.buttonNewGame = tk.Button(self.windows, text="Start A New Game!", command=self.controller.restart_game)
        self.buttonNewGame.place(x=235, y=235)
        self.buttonExit = tk.Button(self.windows, text="Exit", command=exit)
        self.buttonExit.place(x=270, y=300)

    def draw_star(self):
        center_x = 150
        center_y = 50
        r = 20
        points = [
            center_x - int(r * math.sin(2 * math.pi / 5)),
            center_y - int(r * math.cos(2 * math.pi / 5)),
            center_x + int(r * math.sin(2 * math.pi / 5)),
            center_y - int(r * math.cos(2 * math.pi / 5)),
            center_x - int(r * math.sin(math.pi / 5)),
            center_y + int(r * math.cos(math.pi / 5)),
            center_x,
            center_y - r,
            center_x + int(r * math.sin(math.pi / 5)),
            center_y + int(r * math.cos(math.pi / 5)),
        ]
        self.canvas.create_polygon(points, outline='green', fill='yellow')
