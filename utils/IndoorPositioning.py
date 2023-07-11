

class IPS:
    pass

    def __init__ (self):
        self.devices = {}
        pass

    def get_current_Room (self, mac_address) -> str:
        pass

    def update_Device (self, mac_address, Sensor, Rssi):
        pass

    def get_Device (self, mac_address):
        pass

    def add_Device (self, mac_address):
        pass

    def delete_Device (self, mac_address) -> bool:
        pass