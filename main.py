from fastapi import FastAPI
from utils.device import Device
from utils.IndoorPositioning import IPS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Here, we define the origins that are allowed to make CORS requests to the API.
# In this example, any origin is allowed by using the wildcard '*'.
origins = ["*"]

# Then, we add the middleware to the app.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ENDPOINTS FOR SENSORS

@app.post("/recieve_scan/")
async def recieve_scan(data: dict):
    """
    Add a new scan to the respective Device
    """

    # print the recieved Data for Debugging
    print(str(data))

    # extract the MAC Address
    mac_address = list(data.get(list(data.keys())[0]).keys())[0]

    # print the MAC Address
    print(f'MAC Address: {mac_address}')

    # extract the Sensor ID
    Sensor = list(data.keys())[0]

    # extract the Rssi value
    Rssi = data.get(Sensor).get(list(data.get(Sensor).keys())[0])

    # update the Device (where the Device corresponds to a User which is tracked)
    ips.update_Device(mac_address, Sensor, Rssi)

    return {'response': 200}

@app.get("/predict_room/{mac_address}")
async def predict_room_ (mac_address: str):
    """
    Predict the current Room of a Device

    - mac_address := MAC Address of the Device the location should be predicted of
    """

    # print the recieved Command for Debugging
    print('Requested Room Prediction ...')

    # get the prediction of the current Room
    room = ips.get_current_Room(mac_address)    

    print(f'the predicdted Room is {room}')

    return {'Current Room': room}




# ENDPOINT FOR EVERYTHING ABOUT DEVICES

@app.get("/Devices/get_Devices_list/")
async def get_Devices_list ():
    """
    returns a List of all currently registered Devices
    """

    # print the recieved Command for Debugging
    print('Requested Devices List ...')
    # get Devices from RoomControl
    Devices = ips.devices
    # create a json dict storing all the devices
    Devices_data = {"Devices": [device.__dict__ for device in Devices]}
    print(20*'-')
    print(Devices_data)
    print(20*'-')
    return Devices_data


@app.get("/Devices/get_Device_by_mac_address/{mac_address}")
async def get_Device (mac_address: str):
    """ 
    this returns the one specific Device with the given MAC_Address
    """

    # print the recieved Command for Debugging
    print(f'Requested Device Data for {mac_address} ...')
    # get Device from RoomControl
    device = ips.get_Device(mac_address)

    if device == None:
        return {'error': 'Device not found'}
    else:
        return {'Device': device.__dict__}


@app.post("/Devices/add_device/")
async def add_device (device_data: dict):
    """
    Adds a new Device to the IPS - remember: newly found MAC Addresses are automatically added as Device
    a valid post looks like this
    device_data = {
                    "MAC_Address": "AA:BB:CC:DD:EE:FF",
                    "name": "Device Name",
                    }
    """
    # print the recieved Command for Debugging
    print('Requested Device Adding ...')
    try:
        # add device to RoomControl
        ips.add_Device(device_data.get('MAC_Address'))
        ips.get_Device(device_data.get('MAC_Address')).set_name(device_data.get('name'))
        # return success
        return "200"
    except:
        return "400"


@app.post("/Devices/update_device_name/")
async def update_device_name (device_data: dict):
    """updates the name of a device
    a valid request looks like
    {
        "MAC_Address": "AA:BB:CC:DD:EE:FF",
        "new_name": "new device name"
    }
    """
    # print the recieved Command for Debugging
    print('Requested Device Name change')
    try:
        #get the device
        device = ips.get_Device(device_data.get("MAC_Address"))
        #update the name to the given value
        device.set_name(device_data.get("new_name"))
        # return success
        return "200"
    except:
        return "400"


@app.get("/Devices/delete_device/{mac_address}")
async def delete_device (mac_address: str):
    """Deletes a Device from the Devices list
    a valid request looks like
    {"MAC_Address":"AA:BB:CC:DD:EE:FF"}
    """
    # print the recieved Command for Debugging
    print('Requested Device Delete')
    try:
        #delete device
        _ = ips.delete_Device(mac_address)
        if _:
            return "200"
        return "300"
    except:
        "400"


@app.get("/Devices/get_sensor_data/{mac_address}")
async def get_sensor_data (mac_address: str):
    """Gets the Sensor Data from a Sensor"""
    # print the requested Command
    print('Requested Sensor Data')
    return {ips.get_Device(mac_address).get_sensors()}



if __name__ == "__main__":
    import uvicorn

    ip = "10.220.9.82" #has to be configured
    port_n = 5000
    

    ips = IPS()
    

    uvicorn.run(app, host=ip, port=port_n)