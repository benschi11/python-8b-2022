from user import User
import hashlib

class UserRepository:

    def __init__(self) -> None:
        self.__nextId = 1;
        self.__users:list[User] = [];
        self.loadUsers();
    
    def loadUsers(self) -> None:
        f = open("user","r")
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.replace("\n","")

            if line != "":
                line_elements = line.split(";")
                user:User = User(int(line_elements[0]),line_elements[1], line_elements[2])
                self.__users.append(user)
        
        if len(self.__users) > 0:
            self.__nextId = self.__users[-1].Id + 1


    def getAllUsers(self) -> list[User]:
        return self.__users;

    def addUser(self, name:str, password:str) -> User:
        newUser = User(self.__nextId, name, UserRepository.generateHash(password));

        # Schreibe User in Datei
        f = open("user","a");
        f.write("\n"+newUser.decodeUserForFile())
        f.close()

        self.__nextId += 1;
        self.__users.append(newUser);
        return newUser;

    def generateHash(password:str) -> str:
        plaintext = password.encode();
        passwordHash = hashlib.sha256(plaintext);
        return passwordHash.hexdigest();

