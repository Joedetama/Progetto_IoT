import aiocoap.resource as resource
import aiocoap
from model.rain_sensor import RainSensorDescriptor


class RainSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.rain_sensor = RainSensorDescriptor()

    async def render_get(self, request):

        self.rain_sensor.measure_rain()

        payload_string = self.rain_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))