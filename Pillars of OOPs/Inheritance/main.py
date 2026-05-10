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




## Questions to Ask in Interview -------------------------------
"""
🧠 Q1: What is inheritance?
“It allows a class to reuse and extend another class's functionality.”

🧠 Q2: What is method overriding?
“Redefining a parent method in child class.”

🧠 Q3: What is MRO?
“Order in which Python resolves methods in inheritance.”

🧠 Q4: Why use super()?
“To call parent methods safely following MRO.”

🧠 Q5: When NOT to use inheritance?
“When relationship is not ‘is-a’, or when it increases complexity.”
"""




"""
BaseModel → defines rules
Child models → implement behavior
Pipeline → uses models
"""