import aiocoap.resource as resource
import aiocoap
from model.battery_sensor import BatterySensorDescriptor


class BatterySensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.battery_sensor = BatterySensorDescriptor()

    async def render_get(self, request):
        
        self.battery_sensor.measure_battery()
        
        payload_string = self.battery_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))