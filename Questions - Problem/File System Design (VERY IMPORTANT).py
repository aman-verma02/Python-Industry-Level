'''
Problem
Design:
create_file(name, content)
read_file(name)
delete_file(name)

🧠 Thinking
Use:
dictionary → filename → content
'''


class FileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, name, content):
        self.files[name] = content

    def read_file(self, name):
        if name not in self.files:
            return "File not found"
        return self.files[name]

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]


'''
⚠ Edge Cases
Overwriting files
Reading non-existent file
'''