from user import User
from userRepository import UserRepository
import getpass

userRepository = UserRepository();

userInput = input("Was möchten Sie tun? (n) -> neuer Benutzer, (l) -> login, (q) -> quit");
while(userInput.lower() != "q"):
    if(userInput.lower() == "n"):
        name = input("Bitte Benutzername eingeben: ");
        password = getpass.getpass("Bitte Passwort eingeben: ");
        user = userRepository.addUser(name, password);
        print(user.Password)


    userInput = input("Was möchten Sie tun? (n) -> neuer Benutzer, (l) -> login, (q) -> quit");