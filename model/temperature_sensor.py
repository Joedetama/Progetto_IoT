import random
import json

class TemperatureSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "C"
        self.measure_temperature()

    def measure_temperature(self):
        self.value = random.uniform(18.0, 30.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
