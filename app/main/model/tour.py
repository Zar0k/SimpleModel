import json


class Tour:
    # # Initializer / Instance Attributes
    def __init__(self, id, name, duration, description, availability):
        self.id = id
        self.name = name
        self.duration = duration
        self.description = description
        self.availability = availability

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)