from models.predictor import predict_room
import random
import string
import json

class Device:

    def __init__ (self, MAC_Address: str):
        
        self.mac_address = MAC_Address

        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + ' ' + ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

        self.Sensors = {}

        with open("Config.json", mode="r") as f:
            config = json.load(f)
        self.roomnames = config.get("Roomnames")

    def update_sensor (self, Sensor: str, Rssi: float):
        """
        This Method adds one sample to the DataFrame
        """
        Sensor = self.Sensors.get(Sensor)

        if Sensor == None:
            self.Sensors.update({Sensor: Rssi})
            print("New Sensor added")
        else:
            self.Sensors[Sensor] = Rssi

    def get_sensors (self):
        return [self.Sensors[key] for key in self.Sensors.keys()]
    
    def predict_room(self) -> str:
        """predicts the current Room based on the current Sensor Data"""

        RoomID = predict_room(self.Sensors)
        self.current_Room = self.roomnames.get(str(RoomID))

        return self.current_Room
    
    def set_name (self, name: str):
        """ gives the device a name """
        self.name = name