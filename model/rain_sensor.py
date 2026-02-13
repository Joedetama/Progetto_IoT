import random
import json

class RainSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "mm"
        self.measure_rain()

    def measure_rain(self):
        self.value = random.uniform(0.0, 5.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
