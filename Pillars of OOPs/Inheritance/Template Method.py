# 👉 Parent controls flow, child customizes behavior
class DataPipeline:
    def run(self):
        self.load()
        self.process()
        self.save()

    def load(self):
        print("Load data")

    def process(self):
        pass

    def save(self):
        print("Save data")


class CustomPipeline(DataPipeline):
    def process(self):
        print("Custom processing")