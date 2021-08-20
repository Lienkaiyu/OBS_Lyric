from tkinter import *
import tkinter.messagebox as box
import os

files = os.listdir('.')

window = Tk()
window.title( '<title>' )

frame = Frame( window )

listbox = Listbox(frame)
for name in files:
    if name.endswith(".lyr"):
        listbox.insert('end', name)

def dialog() :
    #box.showinfo( 'Selection' , 'Your Choice: ' + \
    #listbox.get( listbox.curselection() ) )
    song=listbox.curselection()
    window.destroy()
btn = Button( frame, text = 'View Info', command=dialog )

btn.pack( side = RIGHT , padx = 5 )
listbox.pack( side = LEFT )
frame.pack( padx = 30, pady = 30 )

window.mainloop()