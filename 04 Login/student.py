from dataclasses import dataclass, field
from user import User

@dataclass
class Student(User):

    SchoolClass : str = ""
    Courses : list = field(default_factory=[])

    