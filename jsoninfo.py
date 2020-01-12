#json parser

import json
from datetime import datetime

def bytime():
    with open('Murder-on-the-2nd-Floor-Raw-Data.json','r') as f:
        data = json.load(f)

    return data

def byperson():
    info = {"Veronica" : [],
            "Jason" : [],
            "Thomas" : [],
            "Rob" : [],
            "Kristina" : [],
            "Marc-Andre" : [],
            "Dave" : [],
            "Salina" : [],
            "Harrison" : [],
            "Eugene" : [],
            "Alok" : [],
            "James" : [],
            "n/a" : []
            }


    with open('Murder-on-the-2nd-Floor-Raw-Data.json','r') as f:
        data = json.load(f)

        for obj in data:
            value = data[obj]
            
            time = int(obj)
            
            name = value["guest-id"]
            device = value["device"]
            deviceid = value["device-id"]
            event = value["event"]

            sensor = []

            sensor.append(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))

            sensor.append(name)
            sensor.append(device)
            sensor.append(deviceid)
            sensor.append(event)

            info[name].append(sensor)

    return info
            
