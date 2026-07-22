# Template design pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. It allows subclasses to redefine certain steps of an algorithm without changing the algorithm's structure.
from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open_file(self): # common step for all parsers
        print(f"Opening file: {self.file_path}")
    
    def close_file(self): # common step for all parsers
        print(f"Closing file: {self.file_path}")

    @abstractmethod
    def parse(self): # we want that subclass will write this part of algorithm
        pass

    def parse_file(self):
        self.open_file()
        self.parse()
        self.close_file()

class CSVParser(Parser):
    def parse(self):
        print(f"Parsing CSV file: {self.file_path}")

class JSONParser(Parser):
    def parse(self):
        print(f"Parsing JSON file: {self.file_path}")

# client code
csv_parser = CSVParser("data.csv")
csv_parser.parse_file()

json_parser = JSONParser("data.json")
json_parser.parse_file()