

# Static Method (@staticmethod)
# Works with neither instance nor class data
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    

print(Math.add(2, 3))  # Output: 5
# Static methods are used when we want to perform a function that is related to the class but does not need access to instance or class data.



class DataLoader:
    def load(self):
        return "data"

class Preprocessor:
    def process(self, data):
        return "cleaned data"

class Model:
    def train(self, data):
        print("Training")


data = DataLoader().load()
data = Preprocessor().process(data)
Model().train(data)