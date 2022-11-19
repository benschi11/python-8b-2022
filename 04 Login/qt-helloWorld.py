import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

app = QApplication(sys.argv)
widget = QWidget()

textLabel = QLabel(widget)
textLabel.setText("Hello World!")
textLabel.move(110,85)

widget.setGeometry(50,50,320,200)
widget.setWindowTitle("PyQt5 Example")
widget.show()
sys.exit(app.exec())