import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QWidget, QDialog
from PyQt6.QtCore import *

from loginform import *
from mainwindow import MainWindow
from user import User
from userRepository import UserRepository
# import getpass

userRepository = UserRepository();

# userInput = input("Was möchten Sie tun? (n) -> neuer Benutzer, (l) -> login, (q) -> quit");
# while(userInput.lower() != "q"):
#     if(userInput.lower() == "n"):
#         name = input("Bitte Benutzername eingeben: ");
#         password = getpass.getpass("Bitte Passwort eingeben: ");
#         user = userRepository.addUser(name, password);
#         print(user.Password)


#     userInput = input("Was möchten Sie tun? (n) -> neuer Benutzer, (l) -> login, (q) -> quit");

app = QApplication(sys.argv)

loginDlg = LoginForm(userRepository);
if loginDlg.exec():
    print("Login Successfull");
    mainwindow = MainWindow()
    mainwindow.show()
else:
    sys.exit()

sys.exit(app.exec());
