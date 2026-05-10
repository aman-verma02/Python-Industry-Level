# ❓ Problem
# You want:
# consistent interface
# multiple models
# scalable system

from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def train(self, data): pass

    @abstractmethod
    def predict(self, x): pass

class RandomForestModel(BaseModel):
    def train(self, data):
        print("Training RF")

    def predict(self, x):
        return "RF prediction"
    
class NeuralNetModel(BaseModel):
    def train(self, data):
        print("Training NN")

    def predict(self, x):
        return "NN prediction"
    
class Pipeline:
    def run(self, model: BaseModel, data):      # model: BaseModel it is doing type hinting, it indicates that the model parameter should be an instance of a class that inherits from BaseModel. This allows the Pipeline class to work with any model that implements the train and predict methods defined in the BaseModel abstract class.
        model.train(data)
        return model.predict("input")
    
pipeline = Pipeline()
rf_model = RandomForestModel()
nn_model = NeuralNetModel() 
print(pipeline.run(rf_model, "RF training data"))  # Output: RF prediction
print(pipeline.run(nn_model, "NN training data"))  # Output: NN prediction
# Output:
# Training RF
# RF prediction
# Training NN
# NN prediction