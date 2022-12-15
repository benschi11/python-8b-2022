from dataclasses import dataclass, field
@dataclass
class User:

    Id : int
    Username : str
    Password : str
    Prename : str = ""
    Surname : str = ""

    def decodeUserForFile(self) -> str:
        return str(self.Id) + ";" + self.Username + ";" + self.Password + ";" + self.Prename + ";" + self.Surname;
     
