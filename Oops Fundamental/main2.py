# ⚠ Common Mistakes

# ❌ Forgetting self
# ❌ Using global variables instead of class
# ❌ Mixing too many responsibilities in one class


class Model:
    def __init__(self, name):
        self.name = name
        self.is_trained = False

    def train(self, data):
        print(f"Training {self.name} model...")
        self.is_trained = True

    def predict(self, x):
        if not self.is_trained:
            return "Model not trained"
        return f"Prediction for {x}"
    

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        print(f"Loading data from {self.path}")
        return ["data1", "data2"]
    

class Trainer:
    def __init__(self, model):
        self.model = model

    def run(self, data):
        self.model.train(data)





loader = DataLoader("data.csv")
data = loader.load()

model = Model("XGBoost")
trainer = Trainer(model)

trainer.run(data)