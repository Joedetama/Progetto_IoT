import aiocoap.resource as resource
import aiocoap
from model.uv_index_sensor import UvIndexSensorDescriptor


class UvindexSensorResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.uv_index_sensor = UvIndexSensorDescriptor()

    async def render_get(self, request):

        self.uv_index_sensor.measure_uv_index()

        payload_string = self.uv_index_sensor.to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))