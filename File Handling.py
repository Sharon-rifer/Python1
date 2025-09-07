from abc import ABC, abstractmethod
# Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self, filepath):
        pass
    @abstractmethod
    def write(self, filepath, data):
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    def write(self, filepath, data):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(data)
            print(f"Text written to {filepath}")

#Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, "rb") as file:
            return file.read()

        def write(self, filepath, data):
        with open(filepath, "wb") as file:
            file.write(data)
            print(f"Binary written to {filepath}")