
import tkinter as tk
from tkinter import ttk

import PIL
from PIL.Image import Image
from TriviaView import TriviaView
from TriviaController import TriviaController
# from util.seed_db import seed

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # windows = tk.Tk()
        len = 64
        view = TriviaView(self, "640x640", "TriviaMaze", len)
        controller = TriviaController(view)

        print("starting app")
        # seed()

        view.set_controller(controller)
        view.welcome_page()

if __name__ == '__main__':

    # seed()
    app = App()
    app.mainloop()
