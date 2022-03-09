
import tkinter as tk
from tkinter import ttk
from Model import Model
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

        # map = controller.get_map()
        controller.start_new_game()
        # controller.store_current_game()
        print("starting app")
        # seed()

        view.set_controller(controller)

if __name__ == '__main__':

    # seed()
    app = App()
    app.mainloop()

