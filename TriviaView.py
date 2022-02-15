import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

class TriviaView:

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
            print(show_spot)
        print(" ")

    def print_question(self, question):
        print("question:" + question)

# if __name__== "__main__":
#     cell_width = 40
#     row = 4
#     cols = 4
#     height = cell_width * row
#     width = cell_width * cols
#     move_counter, total_counter = 0, 0
#
#     windows = tk.Tk()
#     windows.title("Four Musketeers' Winter Olympics Trivia Game")
#     windows.resizable(4, 4)
#     t0 = time.time()
#
#     #big canvas holds maze
#     canvas = tk.Canvas(windows, background="#525288", width=4 * width, height=4 * height)
#     canvas.pack(anchor=tk.NW)
#
#     map = Map(4, 4, canvas)
#     map.generate_map()
#     map.generate_player()
#     map.draw_maze()
#
#     #frame for winter olympics banner
#     frame_banner = tk.Frame(windows, highlightbackground="white", highlightthickness=1, width=width/2, height=80, bd=0)
#     frame_banner.pack(fill=tk.Y, side=tk.LEFT)
#
#     banner_image = Image.open("img.png")
#     banner_image = banner_image.resize((200, 100), Image.ANTIALIAS)
#     tk_image1 = ImageTk.PhotoImage(banner_image)
#     # tk_image1._PhotoImage__photo.subsample(2)
#     label1 = tk.Label(frame_banner, image=tk_image1)
#     label1.image = tk_image1
#     label1.pack()
#
#     windows.mainloop()