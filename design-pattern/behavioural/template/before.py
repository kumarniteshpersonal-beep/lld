class CSVParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open_file(self):
        print(f"Opening file: {self.file_path}")

    def close_file(self):
        print(f"Closing file: {self.file_path}")

    def parse_file(self):
        self.open_file()
        print(f"Parsing CSV file: {self.file_path}")
        self.close_file()

class JSONParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open_file(self):
        print(f"Opening file: {self.file_path}")

    def close_file(self):
        print(f"Closing file: {self.file_path}")

    def parse_file(self):
        self.open_file()
        print(f"Parsing JSON file: {self.file_path}")
        self.close_file()

# client code
csv_parser = CSVParser("data.csv")
csv_parser.parse_file()

json_parser = JSONParser("data.json")
json_parser.parse_file()

# problems:
# 1. The open_file and close_file methods are duplicated in both CSVParser and JSONParser classes, which violates the DRY (Don't Repeat Yourself) principle.