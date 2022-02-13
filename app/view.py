import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()

root.title("CovidAdventure")

frame = ttk.Frame(root)
frame.pack()
ttk.Button(frame, text = 'Click Me').pack()
ttk.LabelFrame(root, height = 400, width = 800, text = 'My Frame').pack()

root.mainloop()

