import tkinter as tk
from tkinter import *
import os.path

if not os.path.exists("Lyrics.txt"):
    f = open("Lyrics.txt", "x")

# Second Screen
class PopupDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('Lyrics')
        self.parent = parent  # Display and keep parent window
        self.geometry("1280x720+200+500")

        self.listbox = Listbox(self, font=('Helvetica', 20))
        self.listbox.pack(side="top", fill="both", expand=True)

        f = open("Lyrics.txt", "r", encoding="utf8")
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


# Main Screen
class MyApp(tk.Tk):

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
                              fg='white', font=('Helvetica', 60))

        self.label.pack(side=tk.BOTTOM)
        pw = PopupDialog(self)
        self.wait_window(pw)  # This is important！！！
        return


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()