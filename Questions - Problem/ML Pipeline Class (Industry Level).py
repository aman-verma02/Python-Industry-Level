'''
❓ Problem
Design:
load
preprocess
train
predict

🧠 Thinking
Pipeline orchestration
'''

class MLPipeline:
    def __init__(self, model):
        self.model = model
        self.data = None

    def load_data(self):
        self.data = "raw data"
        print("Data loaded")

    def preprocess(self):
        self.data = "processed data"
        print("Data processed")

    def train(self):
        print("Model trained")

    def predict(self, x):
        return f"Prediction for {x}"
    


    
pipeline = MLPipeline("RandomForest")

pipeline.load_data()
pipeline.preprocess()
pipeline.train()

print(pipeline.predict("input"))