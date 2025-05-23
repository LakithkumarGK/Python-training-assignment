import json
class Storage:
    def __init__(self, filename):
        self.filename = filename
    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)