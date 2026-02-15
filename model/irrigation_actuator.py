import json

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
                incremento = 0.5 if new_level == "Low" else 1.0 if new_level == "Medium" else 1.5
                self.consumo_acqua_counter += incremento

            # Controllo limite sicurezza
            if self.consumo_acqua_counter >= 10.0:
                self.is_blocked = True
                self.status = "OFF"
                self.level = "None"
                #print(f" IRRIGAZIONE BLOCCATA ({self.consumo_acqua_counter})")
            else:
                self.status = new_status
                self.level = new_level
            
            return True
        except:
            return False