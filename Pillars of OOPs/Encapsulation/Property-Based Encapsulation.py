class Student:
    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Invalid marks")
        self.__marks = value


s = Student()

s.marks = 90    # setter
print(s.marks)  # getter

# s.marks = -10   # ❌ invalid state
# print(s.marks)  # ❌ invalid state
# In this example, we have a Student class with a private variable __marks. We use the @property decorator to create a getter method for marks, and the @marks.setter decorator to create a setter method for marks. The setter method includes validation to ensure that the marks cannot be set to a negative value, thus maintaining the integrity of the data.