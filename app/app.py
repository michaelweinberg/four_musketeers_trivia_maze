
import tkinter as tk
from tkinter import ttk
from Model import Model
from TriviaView import TriviaView
from TriviaController import TriviaController
import pygame
# from util.seed_db import seed


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        len = 64
        view = TriviaView(self, "640x640", "TriviaMaze", len)
        controller = TriviaController(view)
        print("starting app")
        view.set_controller(controller)
        view.welcome_page()
        
        pygame.mixer.init()
        pygame.mixer.music.load("models/Ultimate-Victory.wav")
        pygame.mixer.music.play(-1)


if __name__ == '__main__':

    app = App()
    app.mainloop()
