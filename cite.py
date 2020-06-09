import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

mainWindow = QMainWindow()
widget = QWidget()

web = QWebView()
web.load(QUrl("https://www.citethisforme.com/"))

verticalLayout = QVBoxLayout()
verticalLayout.addWidget(web)

widget.setLayout(verticalLayout)
mainWindow.setCentralWidget(widget)
mainWindow.show()

sys.exit(app.exec_())