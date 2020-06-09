import os
from tkinter import *
from PIL import Image, ImageTk
global image

class Instructions(Frame):
    def __init__(self, master=None, width=0.4, height=0.3, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()


if __name__ == '__main__':
    root = Tk() #

    sp = Instructions(root)
    sp.config(bg="#af2a2f")

    m = Label(sp,
              text="Vertigo Assistive Eye: Keyboard & Mouse! - Instructions!"
              "\n\n This is the Vertigo Assistive Eye!"
              "\n\n This is a GUI for disabled students. "
              "\n\n Use the keyboard by looking at any specific key and blink to select it."
              "\n\n The key when selected will turn green that shows you that you have done it! "
              "\n\n Stay in frame by using the active front camera. Keep your face within the frame at all times."
              "\n\n For one left click, blink once, "
              "\n\n For a double click, blink twice."
              "\n\n I hope you enjoy using this application.")


    m.pack(side=TOP, expand=YES)
    m.config(bg="#af2a2f", justify=CENTER, font=("calibri", 15))

    def Return(): # Returns to splash screen
        root.destroy()
        os.system("python SplashScreen.py")

    Button(sp, text="Return", bg='blue', command=Return).pack(side=BOTTOM, fill=X)
    root.mainloop()
