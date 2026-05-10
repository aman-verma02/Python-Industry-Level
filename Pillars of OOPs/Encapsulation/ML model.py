class MLModel:
    def __init__(self):
        self.__is_trained = False

    def train(self):
        print("Training...")
        self.__is_trained = True

    def predict(self, x):
        if not self.__is_trained:
            raise Exception("Model not trained")
        return "prediction"