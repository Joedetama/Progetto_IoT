import json

LEVEL_CONSUMPTION = {
    "Low": 0.5,
    "Medium": 1.0,
    "High": 1.5
}

class IrrigationActuatorDescriptor:
    def __init__(self):
        self.status = "OFF"
        self.level = "None"
        self.consumo_acqua_counter = 0.0
        self.is_blocked = False

    def to_json(self):
        return json.dumps(self.__dict__)

    def update_from_json(self, data_json):
        if self.is_blocked:
            return True # Riceve il comando ma non agisce perché bloccato

        try:
            data = json.loads(data_json)
            new_status = data.get("status", self.status)
            new_level = data.get("level", self.level)

            # Se l'acqua viene accesa (o era già accesa), incremento il counter
            if new_status == "ON":
                self.consumo_acqua_counter += LEVEL_CONSUMPTION.get(new_level, 0.0)

            # Controllo limite sicurezza
            if self.consumo_acqua_counter >= 10.0:
                self.is_blocked = True
                self.status = "OFF"
                self.level = "None"
            else:
                self.status = new_status
                self.level = new_level
            
            return True
        except:
            return False