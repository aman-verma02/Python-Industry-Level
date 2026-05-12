# Core Idea
# Exceptions are part of your system design, not just error handling


class InvalidAmountError(Exception):
    pass


def withdraw(amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    


## Real ML Example     ----------------------------

class ModelNotTrainedError(Exception):
    pass


class MLModel:
    def __init__(self):
        self.trained = False

    def train(self):
        self.trained = True

    def predict(self, x):
        if not self.trained:
            raise ModelNotTrainedError("Model not trained")
        return "prediction"