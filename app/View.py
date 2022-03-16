import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        # self.title("Winter Olympics Trivia Game")


        parent.title("Olympics Trivia Game")

        self.grid(row=0, column=0, padx=10, pady=10)

        self.label = ttk.Label(self, text='Enter your name:')
        self.label.grid(row=1, column=0)

        # email entry
        self.name = tk.StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.name, width=30)
        self.name_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Click', command=self.click)
        self.save_button.grid(row=1, column=3, padx=10)

        self.controller = controller

    def click(self):
        self.controller.click_handler(self.name)
