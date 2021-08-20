from tkinter import *
import tkinter as tk

import os

files = os.listdir('.')

class preview(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('Lyrics')
        self.parent = parent  # Display and keep parent window
        self.geometry("1366x720+200+500")

        '''
        #self.frame = Frame( window )

        self.song = Listbox(self)
        for name in files:
            if name.endswith(".lyr"):
                self.song.insert('end', name)
        self.song.pack( side = LEFT )

        sel=[]

        def dialog() :
            selected = (self.song.get(listbox.curselection()))
            sel.append(selected)
            print(sel)

        self.btn = Button( self, text = 'View Info', command=dialog )

        self.btn.pack( side = LEFT , padx = 5 )
        '''
        self.listbox = Listbox(self, font=('Helvetica', 20))
        self.listbox.pack(side="top", fill="both", expand=True)

        f = open("Lyrics.lyr", "r", encoding="utf8")
        for x in f:
            self.listbox.insert(END, x)
        f.close()

        # Submit button
        OK_BUTTON = tk.Frame(self)
        OK_BUTTON.pack(fill="x")

        tk.Button(OK_BUTTON, text="確定", font=('Helvetica', 20),
                  command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        # To change parent window Label variable
        self.parent.name = self.listbox.get(self.listbox.curselection())
        # Update parent window UI
        self.parent.label.config(text=self.parent.name)