from tkinter import *
import tkinter as tk
import preview

class program(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Current lyrics')
        self.geometry("1280x200+0+0")
        # initialization
        self.name = ''
        # Prog Main UI
        self.setupUI()

    def setupUI(self):
        self.config(bg='#00ff00')
        self.label = tk.Label(text=self.name,  bg='#00ff00',
                              fg='white', font=('Helvetica', 45))

        self.label.pack(side=tk.BOTTOM)
        pw = preview.preview(self)
        self.wait_window(pw)  # This is important！！！
        return