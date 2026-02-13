import aiocoap.resource as resource
import aiocoap
from model.pollution_sensor import PollutionSensorDescriptor


class PollutionSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.pollution_sensor = PollutionSensorDescriptor()

    async def render_get(self, request):
        
        self.pollution_sensor.measure_pollution()

        payload_string = self.pollution_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))