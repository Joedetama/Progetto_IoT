import aiocoap.resource as resource
import aiocoap
from model.irrigation_actuator import IrrigationActuatorDescriptor

class IrrigationResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.actuator = IrrigationActuatorDescriptor()

    async def render_get(self, _request):

        #Risponde alle richieste GET con lo stato attuale (JSON)
        payload = self.actuator.to_json().encode('utf-8')

        return aiocoap.Message(content_format=50, payload=payload)

    async def render_post(self, request):

        payload = request.payload.decode('utf-8')

        if self.actuator.update_from_json(payload):

            return aiocoap.Message(code=aiocoap.CHANGED, payload=b"OK")
        
        return aiocoap.Message(code=aiocoap.BAD_REQUEST, payload=b"Error")