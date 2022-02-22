import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from room import Room
from player import Player
from map import Map
import random
import time

class TriviaView:

    def __init__(self):
        self.cell_width = 60
        self.row = 4
        self.cols = 4
        self.height = self.cell_width * self.row
        self.width = self.cell_width * self.cols
        # move_counter, total_counter = 0, 0
        self.root = tk.Tk()
        self.root.geometry('600x800')
        self.root.maxsize(1500,1500)
        self.root.title("Four Musketeers' Winter Olympics Trivia Game")
        self.root.resizable(0,0)
        # t0 = time.time()
        # big canvas holds maze
        self.canvas = tk.Canvas(self.root, background="#525288", width=2 * self.width, height=2 * self.height)
        self.canvas.pack(anchor=tk.N)

        # label start of maze
        self.canvas.create_text(25, 15, fill="black", font="Times 10 italic bold", text="START")

        # label end of maze
        self.canvas.create_text(385, 380, fill="black", font="Times 10 italic bold", text="FINISH")

        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New Game", command=self.donothing)
        self.filemenu.add_command(label="Save Game", command=self.donothing)
        self.filemenu.add_command(label="Load Game", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # help menu(about, game play instructions)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Game Play Instructions", command=self.instructions)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)

        # frame for room info/question packed under maze
        self.frame_roominfo = tk.Frame(self.root, background="#525288", highlightthickness=1, width=2 * self.width,
                                  height=2 * self.height, bd=0)

        # frame for question/answer packed under maze
        self.frame_question = tk.Frame(self.root, background="#525288", highlightthickness=1, width=2 * self.width,
                                  height=2 * self.height, bd=0)

        # Create fonts for making difference in the frame
        self.font1 = font.Font(family='Georgia', size='22', weight='bold')
        self.font2 = font.Font(family='Aerial', size='22')

        # Add heading logo in the frames
        self.label_a = Label(self.frame_roominfo, text="Room Info: ", foreground="green3", font=self.font1)
        self.label_a.pack(pady=20)

        self.label_b = Label(self.frame_question, text="Question: ", foreground="blue", font=self.font2)
        self.label_b.pack(pady=20)

        # Add button to switch between two frames
        # button1 = Button(windows, text="Show Question", font=font2, command=change_to_question)
        # button1.pack(pady=20)

        self.button2 = Button(self.frame_question, text="Show Room Info", font=self.font2, command=self.change_to_roominfo)
        self.button2.pack(pady=20)

        # control panel frame
        self.frame_controlpanel = tk.Frame(self.root, highlightbackground="green", highlightthickness=1, width=self.width,
                                      height=self.height, bd=0)
        self.frame_controlpanel.pack(fill=tk.Y, side=tk.RIGHT)

        self.north_button = tk.Button(self.frame_controlpanel, text="North", fg="yellow", command=self.change_to_question)
        self.north_button.grid(row=2, column=3)

        self.west_button = tk.Button(self.frame_controlpanel, text="West", fg="red", command=self.change_to_question)
        self.west_button.grid(row=3, column=2)

        self.center_button = tk.Button(self.frame_controlpanel, text="Control Panel", fg="green")
        self.center_button.grid(row=3, column=3)

        self.east_button = tk.Button(self.frame_controlpanel, text="East", fg="blue", command=self.change_to_question)
        self.east_button.grid(row=3, column=4)

        self.south_button = tk.Button(self.frame_controlpanel, text="South", fg="black", command=self.change_to_question)
        self.south_button.grid(row=4, column=3)

        # frame for winter olympics banner
        self.frame_banner = tk.Frame(self.root, highlightbackground="white", highlightthickness=1, width=self.width / 2, height=80,
                                bd=0)
        self.frame_banner.pack(fill=tk.Y, side=tk.LEFT)

        self.banner_image = Image.open("img.png")
        self.banner_image = self.banner_image.resize((170, 100), Image.ANTIALIAS)
        tk_image1 = ImageTk.PhotoImage(self.banner_image)

        self.label1 = tk.Label(self.frame_banner, image=tk_image1)
        self.label1.image = tk_image1
        self.label1.pack()

        # self.map = Map(4, 4, self.canvas)
        # self.map.generate_map()
        # self.map.generate_player()
        # self.map.draw_maze()

        self.root.mainloop()

    # toggle between two frames--room info and question/answer frames
    # Define a function for switching the frames
    def change_to_roominfo(self):
        self.frame_roominfo.pack(fill='both', expand=1, anchor=tk.NE)
        # frame_roominfo.grid(row=1, column=3)
        self.frame_question.pack_forget()

    def change_to_question(self):
        self.frame_question.pack(fill='both', expand=1, anchor=tk.NE)
        # frame_question.grid(row=1, column=3)
        self.frame_roominfo.pack_forget()

    def draw_cell(self, width=4, height=4, color="#ee3f4d", color_border="#000000"):
        cell_width = 120
        x0, y0 = width * cell_width, height * cell_width
        x1, y1 = x0 + cell_width, y0 + cell_width
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color_border, width=2)



    def draw_maze_tk(self, map):

        for row in map:
            for room in row:
                print(room.get_value())
                if room.get_value() == 0:  # empty room
                    self.draw_cell(room.get_y(), room.get_x())
                if room.get_value() == 4:  # blocked room
                    self.draw_cell(room.get_y(), room.get_x(), "#525288")
                if room.get_value() == 2:  # start of maze
                    self.draw_cell(room.get_y(), room.get_x(), "#eee83f")
                if room.get_value() == 3:  # end of maze
                    self.draw_cell(room.get_y(), room.get_x(), "#cf52eb")
                if room.get_value() == 10:  # hero in room
                    self.draw_cell(room.get_y(), room.get_x(), "#ee3f4d")
        # self.root.mainloop()

    def print_map(self, map):
        """show the map in the console"""
        for row in map:
            show_spot = ""
            for room in row:
                if room.get_value() == 0:
                    show_spot += " ."
                elif room.get_value() == 4:
                    show_spot += " □"
                elif room.get_value() == 2:
                    show_spot += " S"
                elif room.get_value() == 3:
                    show_spot += " D"
                elif room.get_value() == 10:
                    show_spot += " ▲"
                elif room.get_value() == 5:
                    show_spot += "  "
            print(show_spot)
        print(" ")

    #game play instructions method pop-up window
    def instructions(self):
        messagebox.showinfo("How to play this game:", "Navigate maze from Start to Finish using the Control Panel.\n"
                            "You will need to answer one trivia question correctly to pass through each door.\n"
                            "If the question is answered incorrectly, that door will permanently lock.\n"
                            "If you are able to reach the Finish, you will have won the game!")

    def about(self):
        messagebox.showinfo("Welcome to Winter Olympics Trivia Game!", "Brought to you by the Four Musketeers")


    #methods to be filled in for file menu options
    def new_game(self):
        pass

    def save_game(self):
        pass

    def load_game(self):
        pass

    # file menu (new game, save game, load game, exit)
    def donothing(self):
        x = 0

    def print_question(self, question):
        print("question:" + question)

# trivia_view = TriviaView()
# trivia_view.draw_cell()
# trivia_view.draw_maze_tk(map)
# trivia_view.print_map()


