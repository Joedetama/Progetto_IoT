import aiocoap.resource as resource
import aiocoap
from model.wind_sensor import WindSensorDescriptor


class WindSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.wind_sensor = WindSensorDescriptor()

    async def render_get(self, request):

        self.wind_sensor.measure_wind()

        payload_string = self.wind_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))