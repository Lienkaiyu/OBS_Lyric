import preview
import program

import os.path

if not os.path.exists("Lyrics.txt"):
    f = open("Lyrics.txt", "x")

if __name__ == '__main__':
    app = program.program()
    app.mainloop()