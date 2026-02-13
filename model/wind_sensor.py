import random
import json

class WindSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "km/h"
        self.measure_wind()

    def measure_wind(self):
        self.value = random.uniform(0.0, 20.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
