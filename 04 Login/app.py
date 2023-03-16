import sys
from loginform import LoginForm
from PyQt6.QtWidgets import QApplication, QWidget
from mainwindow import MainWindow
from userform import UserForm

app = QApplication(sys.argv);

mainwindow = MainWindow();

login = LoginForm(); # Instanz meiner LoginForm

if login.exec() == 1:
    mainwindow.show();


sys.exit(app.exec());