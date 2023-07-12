from models.predictor import predict_room
import random
import string
import json

class Device:

    def __init__ (self, MAC_Address: str, Sensors: dict = {}):
        #store the MAC Address which acts as a UID
        self.mac_address = MAC_Address
        #initiate the current Room attribute
        self.current_Room = None
        #create a Random Name for the Device which can be changed later for personalization
        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + ' ' + ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        #the IPS can hand over a list of Sensors which are currently active //neccessary since the classifier needs a fixed size
        self.Sensors = Sensors      # {Sensor ID: 0}
        #load the Configuration of the Roomnames
        with open("Config.json", mode="r") as f:
            config = json.load(f)
        self.roomnames = config.get("Roomnames")

    def update_sensor (self, Sensor: str, Rssi: float):
        """
        This Method updates the RSSI value int the sensors dict
        """
        # check if a new Sensor will be added and print message if True
        if self.Sensors.get(Sensor) == None:
            print("New Sensor added")

        # update the Rssi for the Sensor and add new pair if not registerd yet
        self.Sensors.update({Sensor: Rssi})

    def get_sensors (self):
        return [self.Sensors[key] for key in self.Sensors.keys()]
    
    def predict_room(self) -> str:
        """predicts the current Room based on the current Sensor Data"""

        #call the Classifier and hand over the current state of the Sensors
        RoomID = predict_room(self.Sensors)
        #change the ID to the Roomname and store it as current Room
        self.current_Room = self.roomnames.get(str(RoomID))
        #return the current Roomname
        return self.current_Room
    
    def set_name (self, name: str):
        """ gives the device a name """
        self.name = name