import tkinter as tk
from tkinter import *
import os

class NewWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Current lyrics")
        self.config(bg='#00ff00')
        self.geometry("1280x200+0+0")
        self.label = tk.Label(self, bg='#00ff00',
                              fg='white', font=('Helvetica', 60))
        self.label.pack()


def new_window():
    global window
    window = NewWindow(master)  # only the latest new TopLevel window is tracked


def callback(event):
    global window
    if window:
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            window.label.configure(text=data)
        else:
            window.label.configure(text="")

files = os.listdir('.')


window = None  # The global variable to keep track of your 'latest' TopLevel window
master = tk.Tk()

master.geometry("1280x720+200+500")

label = tk.Label(master, text="This is the main window")
label.pack(side="top", pady=10)

btn = tk.Button(master, text="Click to open a new window", command=new_window)
btn.pack(pady=10)


#Lyrics selection
listbox_lyrics = tk.Listbox(master)
listbox_lyrics.pack(side="top", fill="both", expand=True)
f = open("Lyrics.txt", "r", encoding="utf8")

for x in f:
    listbox_lyrics.insert(END, x)
f.close()
#listbox.insert("end", "one", "two", "three", "four", "five")
listbox_lyrics.select_set(0)
listbox_lyrics.bind("<<ListboxSelect>>", callback)

master.mainloop()