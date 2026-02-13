import random
import json

class UvIndexSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "idx"
        self.measure_uv_index()

    def measure_uv_index(self):
        self.value = random.uniform(0.0, 10.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
