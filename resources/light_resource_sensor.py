import aiocoap.resource as resource
import aiocoap
from model.light_sensor import LightSensorDescriptor


class LightSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.light_sensor = LightSensorDescriptor()

    async def render_get(self, request):

        self.light_sensor.measure_light()

        payload_string = self.light_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))