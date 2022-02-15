
import tkinter as tk
from tkinter import ttk
from Model import Model
from View import View
from TriviaController import TriviaController


class App(tk.Tk):

    def __init__(self):
        super().__init__()




        model = Model("Mike")
        controller = TriviaController()
        view = View(self, controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
