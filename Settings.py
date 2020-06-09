import os
from tkinter import *
from PIL import Image, ImageTk

global image


class Settings(Frame):
    def __init__(self, master=None, width=0.4, height=0.3, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or widths
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()


if __name__ == '__main__':
    root = Tk()  #

    sp = Settings(root)
    sp.config(bg="#af2a2f")

    m = Label(sp,
              text="Vertigo Assistive Eye: Keyboard & Mouse! - Settings!")

    m.pack(side=TOP, expand=YES)
    m.config(bg="#af2a2f", justify=CENTER, font=("calibri", 15))


    def Return():  # Returns to splash screen
        root.destroy()
        os.system("python SplashScreen.py")


    Button(sp, text="Return", bg='blue', command=Return).pack(side=BOTTOM, fill=X)
    root.mainloop()
