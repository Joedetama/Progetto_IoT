import random
import json

class LightSensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "lx"
        self.measure_light()

    def measure_light(self):
        self.value = random.uniform(200.0, 800.0)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
