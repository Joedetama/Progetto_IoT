import random
import json

class BatterySensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "%"
        self.measure_battery()

    def measure_battery(self):
        self.value = random.uniform(0.0, 100.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
