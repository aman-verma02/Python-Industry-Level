from abc import ABC, abstractmethod

class BaseModel(ABC):
    
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

model = BaseModel()   # ❌ ERROR: Can't instantiate abstract class BaseModel with abstract methods predict, train

# Forces child classes to implement methods defined in the abstract class. This ensures that any subclass of BaseModel will have the train and predict methods implemented, providing a consistent interface for all models that inherit from BaseModel.


class LinearRegression(BaseModel):
    def train(self, data):
        print("Training Linear Regression model with data:", data)

    def predict(self, x):
        print("Predicting with Linear Regression model for input:", x)


lr_model = LinearRegression()
lr_model.train("training data for linear regression")
lr_model.predict("input data for prediction")   
# Output:
# Training Linear Regression model with data: training data for linear regression
# Predicting with Linear Regression model for input: input data for prediction
