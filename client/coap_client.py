import logging
import asyncio
import aiocoap
from aiocoap import *
import json
import time

# Logging per monitorare l'attività

logging.basicConfig(level=logging.INFO)

def genera_senml(valori, c_irr, c_light):

    # Genera il payload SenML per il Logger Server

    timestamp = int(time.time())
    senml = [
        {"bn": "serra_joel/", "bt": timestamp},
        {"n": "temperature", "u": "Cel", "v": float(valori['temperature'])},
        {"n": "humidity", "u": "%L", "v": float(valori['humidity'])},
        {"n": "light", "u": "lux", "v": float(valori['light'])},
        {"n": "wind", "u": "km/h", "v": float(valori['wind'])},
        {"n": "uv_index", "u": "idx", "v": float(valori['uv_index'])},
        {"n": "pollution", "u": "ug/m3", "v": float(valori['pollution'])},
        {"n": "rain", "u": "mm", "v": float(valori['rain'])},
        {"n": "battery", "u": "%", "v": float(valori['battery'])},
        {"n": "water_counter", "u": "L", "v": float(c_irr)},
        {"n": "light_counter", "u": "h", "v": float(c_light)}
    ]
    return json.dumps(senml)

async def main():
    protocol = await Context.create_client_context()
    uri_base = 'coap://127.0.0.1:5683/'
    resources = ['temperature', 'humidity', 'light', 'wind', 'uv_index', 'pollution', 'rain', 'battery']

    print("SENSORI PRONTI")
    print("Invio dati a Logger Server sulla porta 5685")

    while True:
        try:
            # LETTURA SENSORI
            valori = {}
            for res in resources:
                msg = Message(code=GET, uri=uri_base + res)
                response = await protocol.request(msg).response
                raw = response.payload.decode("utf-8")
                try:
                    js = json.loads(raw)
                    val = str(js['value']) if 'value' in js else raw
                except:
                    val = raw
                val_clean = "".join(c for c in val if c.isdigit() or c == '.')
                valori[res] = val_clean if val_clean != "" else "0"

            # LOGICA ATTUATORI
            h = float(valori['humidity'])
            l = float(valori['light'])
            
            # irr = irrigazione, lvl = livello di potenza

            if(h < 10):
                irr = "ON"
                lvl = "High"
            elif(h < 20):
                irr = "ON"
                lvl = "Medium"
            elif(h < 30):
                irr = "ON"
                lvl = "Low"
            else:
                irr = "OFF"
                lvl = "None"                

            # light_req = luci, light_int = livello intensità

            if(l < 300):
                light_req = "ON"
                light_int = "High"
            elif(l < 500):
                light_req = "ON"
                light_int = "Medium"
            elif(l < 700):
                light_req = "ON"
                light_int = "Low"
            else:
                light_req = "OFF"
                light_int = "None"

            # INVIO COMANDI AI SENSORI/ATTUATORI (POST)
            await protocol.request(Message(code=POST, payload=json.dumps({"status": irr, "level": lvl}).encode('utf-8'), uri=uri_base + 'irrigation')).response
            await protocol.request(Message(code=POST, payload=json.dumps({"status": light_req, "intensity": light_int}).encode('utf-8'), uri=uri_base + 'light_control')).response

            # RECUPERO STATO REALE E COUNTER (GET)
            res_i = await protocol.request(Message(code=GET, uri=uri_base + 'irrigation')).response
            res_l = await protocol.request(Message(code=GET, uri=uri_base + 'light_control')).response
            
            data_irr = json.loads(res_i.payload.decode('utf-8'))
            data_light = json.loads(res_l.payload.decode('utf-8'))

            c_irr = data_irr.get('consumo_acqua_counter', 0.0)
            c_light = data_light.get('consumo_luce_counter', 0.0)
            
            # INVIO AL SERVER LOGGER (5685 - SENML)
            payload_senml = genera_senml(valori, c_irr, c_light).encode('utf-8')
            await protocol.request(Message(code=PUT, payload=payload_senml, uri='coap://127.0.0.1:5685/logger')).response
            
            logging.info(f"Dati aggiornati ({time.strftime('%H:%M:%S')})")

        except Exception as e:
            logging.error(f"Errore nel ciclo: {e}")

        await asyncio.sleep(10)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGateway chiuso.")