import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from room import Room
from player import Player
from map import Map
import time

# class TriviaView:
#     def print_map(self, map):
#         map.print_map()
#
#     def print_question(self, question):
#         print("question:" + question)

if __name__== "__main__":
    cell_width = 60
    row = 4
    cols = 4
    height = cell_width * row
    width = cell_width * cols
    move_counter, total_counter = 0, 0


    windows = tk.Tk()
    windows.geometry('600x800')
    windows.maxsize(1500,1500)
    windows.title("Winter Olympics Trivia Game")
    windows.resizable(0,0)
    t0 = time.time()

    #game play instructions method pop-up window
    def instructions():
        messagebox.showinfo("How to play this game:", "Navigate maze from Start to Finish using the Control Panel.\n"
                            "You will need to answer one trivia question correctly to pass through each door.\n"
                            "If the question is answered incorrectly, that door will permanently lock.\n"
                            "If you are able to reach the Finish, you will have won the game!")

    def about():
        messagebox.showinfo("Welcome to Winter Olympics Trivia Game!", "Brought to you by the Four Musketeers")


    #methods to be filled in for file menu options
    def new_game():
        pass

    def save_game():
        pass

    def load_game():
        pass

    # file menu (new game, save game, load game, exit)
    def donothing():
        x = 0


    menubar = Menu(windows)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Game", command=donothing)
    filemenu.add_command(label="Save Game", command=donothing)
    filemenu.add_command(label="Load Game", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=windows.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # help menu(about, game play instructions)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Game Play Instructions", command=instructions)
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    windows.config(menu=menubar)

    #big canvas holds maze
    canvas = tk.Canvas(windows, background="#525288", width=2 * width, height=2 * height)
    canvas.pack(anchor=tk.N)

    map = Map(4, 4, canvas)
    map.generate_map()
    map.generate_player()
    map.draw_maze()

    #frame for room info/question packed under maze
    frame_roominfo = tk.Frame(windows, background="#525288", highlightthickness=1, width=2 * width,
                              height=2 * height, bd=0)
    # frame_roominfo.pack()

    #frame for question/answer packed under maze
    frame_question = tk.Frame(windows, background="#525288", highlightthickness=1, width=2 * width,
                              height=2 * height, bd=0)

    #toggle between two frames--room info and question/answer frames
    #Define a function for switching the frames
    def change_to_roominfo():
        frame_roominfo.pack(fill='both', expand=1, anchor=tk.NE)
        # frame_roominfo.grid(row=1, column=3)
        frame_question.pack_forget()

    def change_to_question():
        frame_question.pack(fill='both', expand=1, anchor=tk.NE)
        # frame_question.grid(row=1, column=3)
        frame_roominfo.pack_forget()

    # Create fonts for making difference in the frame
    font1 = font.Font(family='Georgia', size='22', weight='bold')
    font2 = font.Font(family='Aerial', size='22')

    #Add heading logo in the frames
    label_a = Label(frame_roominfo, text="Room Info: ", foreground="green3", font=font1)
    label_a.pack(pady=20)

    label_b = Label(frame_question, text="Question: ", foreground="blue", font=font2)
    label_b.pack(pady=20)

    #Add button to switch between two frames
    # button1 = Button(windows, text="Show Question", font=font2, command=change_to_question)
    # button1.pack(pady=20)

    button2 = Button(frame_question, text="Show Room Info", font=font2, command=change_to_roominfo)
    button2.pack(pady=20)

    # control panel frame
    frame_controlpanel = tk.Frame(windows, highlightbackground="green", highlightthickness=1, width=width,
                                  height=height, bd=0)
    frame_controlpanel.pack(fill=tk.Y, side=tk.RIGHT)

    north_button = tk.Button(frame_controlpanel, text="North", fg="yellow", command=change_to_question)
    north_button.grid(row=2, column=3)

    west_button = tk.Button(frame_controlpanel, text="West", fg="red", command=change_to_question)
    west_button.grid(row=3, column=2)

    center_button = tk.Button(frame_controlpanel, text="Control Panel", fg="green")
    center_button.grid(row=3, column=3)

    east_button = tk.Button(frame_controlpanel, text="East", fg="blue", command=change_to_question)
    east_button.grid(row=3, column=4)

    south_button = tk.Button(frame_controlpanel, text="South", fg="black", command=change_to_question)
    south_button.grid(row=4, column=3)

    #label start of maze

    canvas.create_text(25, 15, fill="black", font="Times 10 italic bold", text="START")

    #label end of maze
    canvas.create_text(385, 380, fill="black", font="Times 10 italic bold", text="FINISH")

    #frame for winter olympics banner
    frame_banner = tk.Frame(windows, highlightbackground="white", highlightthickness=1, width=width/2, height=80, bd=0)
    frame_banner.pack(fill=tk.Y, side=tk.LEFT)

    banner_image = Image.open("img.png")
    banner_image = banner_image.resize((170, 100), Image.ANTIALIAS)
    tk_image1 = ImageTk.PhotoImage(banner_image)

    label1 = tk.Label(frame_banner, image=tk_image1)
    label1.image = tk_image1
    label1.pack()




    windows.mainloop()
