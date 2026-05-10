"""

❓ Problem
Support:
Local storage
AWS S3
Database

🧠 Thinking
👉 Same API:

save(file)
load(file)
"""

# Abstraction Design
from abc import ABC, abstractmethod
class Storage(ABC):

    @abstractmethod
    def save(self, file):
        pass

    @abstractmethod
    def load(self, file):
        pass

# Implementations
class LocalStorage(Storage):
    def save(self, file):
        return "Saved locally"

    def load(self, file):
        return "Loaded locally"
    
class S3Storage(Storage):
    def save(self, file):
        return "Saved to S3"

    def load(self, file):
        return "Loaded from S3"

# System Layer  
class FileManager:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save_file(self, file):
        return self.storage.save(file)

    def load_file(self, file):
        return self.storage.load(file)
    
# Usage
manager = FileManager(S3Storage())
print(manager.save_file("file.txt"))  # Output: Saved to S3