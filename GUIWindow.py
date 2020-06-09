import os
from tkinter import *
import tkinter as tk
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import *


class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.grid()

        self.initUI()

    def initUI(self, master=None):
        self.master.title("Vertigo Assistive Eye: Keyboard & Mouse")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(12):
            self.master.columnconfigure(c, weight=1)

            Button(master, text="Back".format(c)).grid(row=6, column=0, sticky=E+W)
            Button(master, text="Save".format(c)).grid(row=6, column=5, sticky=E+W)
            Button(master, text="Print".format(c)).grid(row=6, column=6, sticky=E+W)
            Button(master, text="Instructions".format(c)).grid(row=6, column=7, sticky=E+W)
            Button(master, text="Settings".format(c)).grid(row=6, column=11, sticky=E+W)

        Frame1 = Frame(master, bg="pink")
        Frame3 = Frame(master, bg="light blue")
        Frame2 = Frame(master, bg="light coral")
        Frame4 = Frame(master, bg="bisque")

        LABEL1 = Label(Frame1, text="CHROME APP").pack()
        LABEL3 =Label(Frame3, text="KEYBOARD").pack()
        LABEL2 =Label(Frame2, text="FRONT CAMERA").pack()

        Frame1.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=W + E + N + S)
        Frame3.grid(row=0, column=3, rowspan=6, columnspan=11, sticky=W + E + N + S)
        Frame2.grid(row=0, column=10, rowspan=3, columnspan=2, sticky=W + E + N + S)
        Frame4.grid(row = 3, column = 10, rowspan = 3, columnspan = 2, sticky = W+E+N+S)


class TabWidget(QDialog):
    def __init__(self):
        super(). __init__()

        self.setWindowTitle("Chrome")
        self.setWindowIcon(QIcon())
        self.resize(455, 955)
        self.move(7,27)

        tabWidget = QTabWidget()

        tabWidget.addTab(Scholar(), "Scholar")
        tabWidget.addTab(Email(), "Email")
        tabWidget.addTab(YouTube(), "YouTube")
        tabWidget.addTab(BBL(), "Student Central")
        tabWidget.addTab(Cite(), "Harvard")
        tabWidget.addTab(Bing(), "Search")

        vBox = QVBoxLayout()
        vBox.addWidget(tabWidget)

        self.setLayout(vBox)


class Scholar(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://scholar.google.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Bing(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.bing.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Cite(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.citethisforme.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class Email(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://mail.google.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class YouTube(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("http://www.youtube.com"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


class BBL(QWidget):
    def __init__(self):
        super().__init__()

        web = QWebView()
        web.load(QUrl("https://studentcentral.brighton.ac.uk/"))

        layout = QVBoxLayout()
        layout.addWidget(web)
        self.setLayout(layout)


App = QApplication(sys.argv)
tabWidget = TabWidget()
tabWidget.show()


def main():
    root = tk.Tk()
    root.geometry("1910x1008+0+0")
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()

