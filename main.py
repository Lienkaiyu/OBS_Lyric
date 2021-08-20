import tkinter as tk
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

PROG_BG = config['Program']['BG']
PROG_FG = config['Program']['FG']
PROG_GEO_W = config['Program']['Width']
PROG_GEO_H = config['Program']['Height']
PROG_GEO_X = config['Program']['X']
PROG_GEO_Y = config['Program']['Y']
PROG_FONT_SIZE = config['Program']['Font_Size']
PROG_FONT_FAMILY = config['Program']['Font_Family']

BKSG_LB_W = config['Backstage']['Box_Width']
BKSG_GEO_W = config['Backstage']['Width']
BKSG_GEO_H = config['Backstage']['Height']
BKSG_GEO_X = config['Backstage']['X']
BKSG_GEO_Y = config['Backstage']['Y']
BKSG_FONT_SIZE = config['Backstage']['Font_Size']
BKSG_FONT_FAMILY = config['Backstage']['Font_Family']

class Program(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Current lyrics")
        self.config(bg=PROG_BG)
        self.geometry("{}x{}+{}+{}".format(PROG_GEO_W, PROG_GEO_H, PROG_GEO_X, PROG_GEO_Y)) #widthxheight±x±y
        self.label = tk.Label(self, bg=PROG_BG,
                              fg=PROG_FG, font=(PROG_FONT_FAMILY, PROG_FONT_SIZE))
        self.label.pack()


def new_window():
    global window
    window = Program(master)  # only the latest new TopLevel window is tracked


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

def load_lyric():
    listbox_lyrics.delete(0,tk.END)
    f = open(listbox_song.get(listbox_song.curselection()), "r", encoding="utf8")

    for x in f:
        listbox_lyrics.insert('end', x)
    f.close()

files = os.listdir('.')

window = None  # The global variable to keep track of your 'latest' TopLevel window
master = tk.Tk()
master.geometry("{}x{}+{}+{}".format(BKSG_GEO_W, BKSG_GEO_H, BKSG_GEO_X, BKSG_GEO_Y)) #widthxheight±x±y

label = tk.Label(master, text="Control Center")
label.pack(side="top", pady=10)

btn_new_window = tk.Button(master, text="Click to open character generator", command=new_window)
btn_new_window.pack(pady=10)
btn_load_lyric = tk.Button(master, text="load", command=load_lyric)
btn_load_lyric.pack(pady=10)

#Song selection
if int(BKSG_FONT_SIZE) > 10:
    BKSGS_FONT_SIZE =int(BKSG_FONT_SIZE) - 8
listbox_song = tk.Listbox(master, width = BKSG_LB_W, font=(BKSG_FONT_FAMILY, BKSGS_FONT_SIZE))
for name in files:
    if name.endswith(('.txt', '.lyr')):
        listbox_song.insert('end', name)
listbox_song.pack(side="left", fill="both")

#Lyrics selection
listbox_lyrics = tk.Listbox(master, font=(BKSG_FONT_FAMILY, BKSG_FONT_SIZE))
listbox_lyrics.pack(side="top", fill="both", expand=True)

listbox_lyrics.select_set(0)
listbox_lyrics.bind("<<ListboxSelect>>", callback)

master.mainloop()
