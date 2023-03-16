from PyQt6.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow
from userform import UserForm

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)

        self.actionUser_hinzufuegen.triggered.connect(self.openAddUser)

    def openAddUser(self):
        addUserForm = UserForm();
        addUserForm.exec();