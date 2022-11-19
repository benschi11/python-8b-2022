from dataclasses import dataclass, field
from user import User

@dataclass
class Teacher(User):
    Courses : list = field(default_factory=[])

    def AddCourse(self, course) -> None:
        self.Courses.append(course)

    def RemoveCourse(self, course) -> None:
        self.Courses.remove(course)