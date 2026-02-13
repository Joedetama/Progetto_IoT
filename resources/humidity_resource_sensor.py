import aiocoap.resource as resource
import aiocoap
from model.humidity_sensor import HumiditySensorDescriptor


class HumiditySensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.humidity_sensor = HumiditySensorDescriptor()

    async def render_get(self, request):
        
        self.humidity_sensor.measure_humidity()

        payload_string = self.humidity_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))