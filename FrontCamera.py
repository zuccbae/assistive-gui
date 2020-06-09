import PIL
from PIL import Image, ImageTk
import cv2
from tkinter import *

cap = cv2.VideoCapture(0)

root = Tk()
video = Label(root)
video.pack()


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    cap1 = ImageTk.PhotoImage(image=img)
    video.cap1 = cap1
    video.configure(image=cap1)
    video.after(10, show_frame)


root.geometry("350x470+1575+30")
show_frame()
root.mainloop()
