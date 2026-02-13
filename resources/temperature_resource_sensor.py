import aiocoap.resource as resource
import aiocoap
from model.temperature_sensor import TemperatureSensorDescriptor


class TemperatureSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.temperature_sensor = TemperatureSensorDescriptor()

    async def render_get(self, request):

        self.temperature_sensor.measure_temperature()

        payload_string = self.temperature_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))