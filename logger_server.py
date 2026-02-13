import aiocoap.resource as resource
import aiocoap
import asyncio
import json

class LoggerResource(resource.Resource):
    async def render_put(self, request):
        payload = request.payload.decode('utf-8')
        print("\n" + "="*50)
        print(" JOEL & MATTIA [LOGGER] - NUOVO PACCHETTO SENML RICEVUTO ")
        print("="*50)
        
        # Mostriamo il JSON SenML ricevuto
        try:
            senml_data = json.loads(payload)
            print(json.dumps(senml_data, indent=4))
        except:
            print(f"Dati grezzi: {payload}")
            
        return aiocoap.Message(code=aiocoap.CHANGED, payload=b"LOGGER_ACK")

async def main():
    root = resource.Site()
    root.add_resource(['logger'], LoggerResource())
    
    # Ascolta sulla porta 5685 per non andare in conflitto con gli altri server
    await aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5685))
    print("Logger Server attivo su coap://127.0.0.1:5685/logger")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())