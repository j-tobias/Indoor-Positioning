from utils.device import Device
import json

class IPS:
    pass

    def __init__ (self):
        """
        the IndoorPositioningSytem
        This class simplifies the prediction of the location for BLE devices which broadcast the iBeacon Protocol
        """
        self.devices = {}       # {MAC Address: Device Object}
        # read the Sensors from the config
        with open("Config.json", mode="r") as f:
            config = json.load(f)

        self.Sensors = config.get("Sensors")       # {Sensor ID: 0}

    def get_current_Room (self, mac_address) -> str:
        """
        returns the Room name of the Room the Device is currently in
        """
        #get the device
        device = self.get_Device(mac_address)

        return device.predict_room()
        
    def update_Device (self, mac_address, Sensor, Rssi):
        """
        Updates the RSSI value of a Device for the given Sensor | creates a new Device if MAC Address hasn't been registered yet
        - mac_address: MAC Address of the respective Device -> AA:BB:CC:DD:EE:FF
        - Sensor: SensorID of the respective Sensor -> s001
        - RSSI: rssi value -> 12.4564
        """
        #get the Device
        device = self.get_Device(mac_address)
        #update the RSSI value for the Sensor
        device.update_sensor(Sensor, Rssi)

    def get_Device (self, mac_address) -> Device:
        """
        returns the device with the given MAC Address if None found it creates an Object and returns it
        """
        # get the Device
        device = self.devices.get(mac_address)
        # check if a device was found
        if device == None:
            # create a new Device and add it
            device = self.add_Device(mac_address)

            print("No Device with the given MAC Address")

        return device

    def add_Device (self, mac_address) -> bool:
        """
        adds a Device object to the System
        """
        #create the Object
        device = Device(mac_address, self.Sensors)
        #add it to the dict
        self.devices.update({mac_address:device})

        return device

    def delete_Device (self, mac_address) -> bool:
        """
        deletes a Device from the Devices dict
        """
        try:
            # delete the device and free the memory space
            del self.devices[mac_address]
            return True
        
        except KeyError:
            # incase the Device was not found
            print("MAC address not found in the dictionary.")
            return False