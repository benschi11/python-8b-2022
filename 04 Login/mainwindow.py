import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from loginform import LoginForm
from userRepository import UserRepository

class MainWindow(QMainWindow):

    def getUserRepository(self):
        self.__userRepository = UserRepository();


    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Store")

        # loginDlg = LoginForm(self.getUserRepository());
        # if loginDlg.exec():
        #     print("Login Successfull");
        # else:
        #     sys.exit()
