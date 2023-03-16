from PyQt6.QtWidgets import QDialog, QPushButton
from ui_login import Ui_m_dlgLogin
from user import User
from userRepository import UserRepository

class LoginForm(Ui_m_dlgLogin,QDialog):

    def __init__(self) -> None:
        super().__init__();
        super().setupUi(self);
        self._userRepository = UserRepository();

        self.m_btnLogin.clicked.connect(self.LoginButton_pressed)


    def LoginButton_pressed(self) -> None:
        username:str = self.m_tbUsername.text();
        user:User = self._userRepository.getUserByName(username);
        print(user);
        password:str = self.m_tbPassword.text();

        if(user == None):
            self.m_lblErrors.setText("User does not exist.")
        elif(user.Password == UserRepository.generateHash(password)):
            self.m_lblErrors.setText("Willkommen " + user.Username)
            self.done(1)
        else:
            self.m_lblErrors.setText("Password wrong")
