from dataclasses import dataclass

@dataclass
class User:
    Id : str
    Name : str
    Password : str

    # def __init__(self, id:int, name:str, password:str ) -> None:
    #     self.__id:int = id;
    #     self.__name:str = name;
    #     self.__password:str = password;
    
    # @property
    # def Id(self) -> int:
    #     return self.__id;

    # @Id.setter
    # def Id(self, value) -> None:
    #     self.__id = value;

    # @property
    # def Name(self) -> str:
    #     return self.__name;
    
    # @Name.setter
    # def Name(self, value) -> None:
    #     self.__name = value;
    
    # @property
    # def Password(self) -> str:
    #     return self.__password;
    
    # @Password.setter
    # def Password(self, value) -> None:
    #     self.__password = value;

    def decodeUserForFile(self) -> str:
        return str(self.Id) + ";" + self.Name + ";" + self.Password;
    


    

        