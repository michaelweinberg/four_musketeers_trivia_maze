import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

class TriviaView:

    def __init__(self):
        self.cell_width = 40
        self.row = 4
        self.cols = 4
        self.height = self.cell_width * self.row
        self.width = self.cell_width * self.cols
        self.root = tk.Tk()
        self.root.title("Four Musketeers' Winter Olympics Trivia Game")
        self.root.geometry("600x600") #size of the app#
        self.root.resizable(0, 0)
        self.canvas = tk.Canvas(self.root, background="#525288", width=2 * self.width, height=2 * self.height)
        self.canvas.pack()

    def draw_cell(self, row, col, color="#F2F2F2"):
        cell_width = self.cell_width
        x0, y0 = col * cell_width, row * cell_width
        x1, y1 = x0 + cell_width, y0 + cell_width
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color, width=0)

    def draw_maze_tk(self, map):

        for row in map:
            for room in row:
                print(room.get_value())
                if room.get_value() == 0:
                    self.draw_cell(room.get_y(), room.get_x())
                if room.get_value() == 4:
                    self.draw_cell(room.get_y(), room.get_x(), "#525288")
                if room.get_value() == 2:
                    self.draw_cell(room.get_y(), room.get_x(), "#eee83f")
                if room.get_value() == 3:
                    self.draw_cell(room.get_y(), room.get_x(), "#cf52eb")
                if room.get_value() == 10:
                    self.draw_cell(room.get_y(), room.get_x(), "#ee3f4d")
        self.root.mainloop()

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

