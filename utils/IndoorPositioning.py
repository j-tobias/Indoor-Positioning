from utils.device import Device

class IPS:
    pass

    def __init__ (self):
        self.devices = {}       # {MAC Address: Device Object}
        self.Sensors = {}       # {Sensor ID: 0}

    def get_current_Room (self, mac_address) -> str:
        """
        returns the Room name of the Room the Device is currently in
        """
        device = self.get_Device(mac_address)
        if device == False:
            return device
        return device.current_Room
        
    def update_Device (self, mac_address, Sensor, Rssi):
        device = self.get_Device(mac_address)
        if device == False:
            self.Sensors.update({Sensor: 0})
            device = Device(mac_address, self.Sensors)
            device.update_sensor(Sensor, Rssi)
        device.update_sensor(Sensor, Rssi)
        return True
        
    def get_Device (self, mac_address) -> Device:
        """
        returns the device with the given MAC Address
        """
        device = self.devices.get(mac_address)
        if device == None:
            print("No Device with the given MAC Address")
            return False
        else:
            return device

    def add_Device (self, mac_address) -> bool:
        """
        adds a Device object to the System
        """
        #create the Object
        device = Device(mac_address)

        #try to add it to the dict -> used try in case of key Error
        try:
            self.devices.update({mac_address:device})
            return True
        except:
            return False

    def delete_Device (self, mac_address) -> bool:
        """
        deletes a Device from the Devices dict
        """
        try:
            del self.devices[mac_address]
            return True
        except KeyError:
            print("MAC address not found in the dictionary.")
            return False