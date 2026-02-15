import json

LEVEL_CONSUMPTION = {
    "Low": 0.5,
    "Medium": 1.0,
    "High": 1.5
}

class LightActuatorDescriptor:
    def __init__(self):
        self.status = "OFF"
        self.intensity = "None"
        self.consumo_luce_counter = 0.0
        self.is_blocked = False

    def to_json(self):
        return json.dumps(self.__dict__)

    def update_from_json(self, data_json):
        if self.is_blocked:
            return True

        try:
            data = json.loads(data_json)
            new_status = data.get("status", self.status)
            new_intensity = data.get("intensity", self.intensity)

            if new_status == "ON":
                # Uso intensity per descrivere l'intesità della luce
                self.consumo_luce_counter += LEVEL_CONSUMPTION.get(new_intensity, 0.0)

            if self.consumo_luce_counter >= 10.0:
                self.is_blocked = True
                self.status = "OFF"
                self.intensity = "None"
            else:
                self.status = new_status
                self.intensity = new_intensity
            
            return True
        except:
            return False