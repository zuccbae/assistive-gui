import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import *


class TabWidget(QDialog):
    def __init__(self):
        super(). __init__()

        self.setWindowTitle("Chrome")
        self.setWindowIcon(QIcon())
        self.resize(455, 950)
        self.move(0, 0)

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
App.exec()



