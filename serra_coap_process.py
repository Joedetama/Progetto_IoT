import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.temperature_resource_sensor import TemperatureSensorResource
from resources.humidity_resource_sensor import HumiditySensorResource
from resources.light_resource_sensor import LightSensorResource
from resources.wind_resource_sensor import WindSensorResource
from resources.uv_resource_sensor import UvindexSensorResource
from resources.pollution_resource_sensor import PollutionSensorResource
from resources.rain_resource_sensor import RainSensorResource
from resources.battery_resource_sensor import BatterySensorResource
from resources.irrigation_resource_actuator import IrrigationResource
from resources.light_resource_actuator import LightResource

logging.basicConfig(level=logging.INFO)

async def main():
    # Creo le risorse
    root = resource.Site()

    root.add_resource(['temperature'], TemperatureSensorResource())
    root.add_resource(['humidity'], HumiditySensorResource())
    root.add_resource(['light'], LightSensorResource())
    root.add_resource(['wind'], WindSensorResource())
    root.add_resource(['uv_index'], UvindexSensorResource())
    root.add_resource(['pollution'], PollutionSensorResource())
    root.add_resource(['rain'], RainSensorResource())
    root.add_resource(['battery'], BatterySensorResource())
    root.add_resource(['irrigation'], IrrigationResource())
    root.add_resource(['light_control'], LightResource())
    
    await aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683))
    
    print("I Sensori sono pronti sulla porta 5683")
    
    # Mantengo il server in esecuzione
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    try:
        # Gestisce il loop degli eventi
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer arrestato dall'utente")