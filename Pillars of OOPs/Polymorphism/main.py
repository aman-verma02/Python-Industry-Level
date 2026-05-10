# SAME code → different behavior  
# Polymorphism is the ability of an object to take on many forms.
# It allows us to use a single interface to represent different types of objects.




class BaseModel:
    def train(self, data):
        pass

    def predict(self, x):
        pass

class LogisticModel(BaseModel):
    def train(self, data):
        print("Training Logistic")

    def predict(self, x):
        return "LR prediction"
    
class RandomForestModel(BaseModel):
    def train(self, data):
        print("Training RF")

    def predict(self, x):
        return "RF prediction"
    

    
models = [LogisticModel(), RandomForestModel()]

for m in models:
    m.train("data")
    print(m.predict("input"))