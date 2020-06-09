import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap

app = QApplication(sys.argv)

label = QLabel(app)
pixmap = QPixmap('EYE.jpg')
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
label.show()

QTimer.singleShot(8000, app.quit)

sys.exit(app.exec_())