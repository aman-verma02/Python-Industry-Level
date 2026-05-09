
# Instance Method
# Works with object data
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name
    

## Class Method (@classmethod)
# Works with class data
class Student:
    school = "ABC"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name