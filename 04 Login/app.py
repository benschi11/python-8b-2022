import sys
from loginform import LoginForm
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv);

login = LoginForm(); # Instanz meiner LoginForm

login.show();


sys.exit(app.exec());