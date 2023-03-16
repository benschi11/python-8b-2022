from PyQt6.QtWidgets import QDialog, QPushButton

from ui_user import Ui_UserDialog
from userRepository import UserRepository

class UserForm(Ui_UserDialog, QDialog):

    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)

        self.m_btnSave.clicked.connect(self.saveButtonClicked)
    
    def saveButtonClicked(self):
        userRepo = UserRepository();
        userRepo.addUser(self.m_tbUsername.text(), self.m_tbPassword.text())
    

    