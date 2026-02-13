import random
import json

class PollutionSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "ug/m3"
        self.measure_pollution()

    def measure_pollution(self):
        self.value = random.uniform(10.0, 50.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
