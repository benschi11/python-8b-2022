from ui_login import Ui_Login
from PyQt6.QtWidgets import QDialog

from userRepository import UserRepository


class LoginForm(QDialog,Ui_Login):

    def __init__(self, userRepository:UserRepository) -> None:
        super().__init__()
        
        super().setupUi(self)

        self.__userRepository = userRepository;

        self.m_btnLogin.clicked.connect(self.btn_login_clicked)


    
    def btn_login_clicked(self):
        
        self.accept()


