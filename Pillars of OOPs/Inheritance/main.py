# Reuse and extend existing class behavior


class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):     ## Inherit the properties and methods of Animal
    def speak(self):
        return "Bark"

class Cat(Animal):     ## Inherit the properties and methods of Animal
    def speak(self):
        return "Meow"
    




# REAL-WORLD EXAMPLE (ML SYSTEM)----------------------------------------------------------
class BaseModel:
    def train(self, data):
        print("Training base model")

    def predict(self, x):
        pass

class LogisticModel(BaseModel):
    def train(self, data):
        print("Training Logistic Regression")

class RandomForestModel(BaseModel):
    def train(self, data):
        print("Training Random Forest")

# 🎯 Key Insight
# 👉 Common logic → parent
# 👉 Specific logic → child


models = [LogisticModel(), RandomForestModel()]

for m in models:
    m.train("data")