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
    



model = Model("RandomForest")

print(model.predict("input"))   # before training
model.train("data")
print(model.predict("input"))   # after training



# Object maintains state
# Before training → is_trained = False
# After training → is_trained = True