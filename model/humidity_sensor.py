import random
import json

SOGLIA_UMIDITA = 40.0

class HumiditySensorDescriptor:

    def __init__(self):
        self.value = 0.0
        self.unit = "%"
        self.measure_humidity()
        self.irrigation1 = "OFF" # 1 stato
        self.irrigation2()

    def measure_humidity(self):
        self.value = random.uniform(00.0, 80.0)

    # Attiva l'irrigazione
    def irrigation2(self):
        if self.value < SOGLIA_UMIDITA :
            self.irrigation1 = "ON" # 2 stato

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
