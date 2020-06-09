import os
from tkinter import *
from PIL import Image, ImageTk
global image

class SplashScreen(Frame):
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

    photo = Image.open("VertigoIndustries.png") #   Parsing name of photo.
    photo = photo.resize((150, 150), Image.ANTIALIAS) #     Resizing photo.
    photo = ImageTk.PhotoImage(photo)   #   Photo Added.


    label = Label(root, image=photo)
    label.pack(side=TOP, expand=YES)

    sp = SplashScreen(root)
    sp.config(bg="#af2a2f")

    m = Label(sp,
              text="Now booting, Vertigo Assistive Eye: Keyboard & Mouse!"
                   "\n\n Select your options below: ")


    m.pack(side=TOP, expand=YES)
    m.config(bg="#af2a2f", justify=CENTER, font=("calibri", 18))

    def Start():
        root.destroy()
        os.system("python GUIWindow.py")

    def Instructions():
        root.destroy()
        os.system("python Instructions.py")

    def Settings():
        root.destroy()
        os.system("python Settings.py")

    def Destroy():
        root.destroy()

    Button(sp, text="Exit", bg='blue', command=Destroy).pack(side=BOTTOM, fill=X)
    Button(sp, text="Settings", bg='blue', command=Settings).pack(side=BOTTOM, fill=X)
    Button(sp, text="Instructions", bg='blue', command=Instructions).pack(side=BOTTOM, fill=X)
    Button(sp, text="Start", bg='blue', command=Start).pack(side=BOTTOM, fill=X)
    root.mainloop()
