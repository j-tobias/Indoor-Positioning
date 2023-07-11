from models.predictor import predict_room
import random
import string

class Device:

    def __init__ (self, MAC_Address: str):
        
        self.mac_address = MAC_Address
        self.previous_Room = None
        self.current_Room = None

        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + ' ' + ''.join(random.choice(string.ascii_uppercase) for _ in range(6))


        self.Sensor1 = 0
        self.Sensor2 = 0
        self.Sensor3 = 0
        self.Sensor4 = 0
        self.Sensor5 = 0

    def update_sensor (self, Sensor: str, Rssi: float):
        """
        This Method adds one sample to the DataFrame
        """
        if Sensor == 's001':
            self.Sensor1 = Rssi
        elif Sensor == 's002':
            self.Sensor2 = Rssi
        elif Sensor == 's003':
            self.Sensor3 = Rssi
        elif Sensor == 's004':
            self.Sensor4 = Rssi
        elif Sensor == 's005':
            self.Sensor5 = Rssi
        
    def get_sensors (self):
        return self.Sensor1, self.Sensor2, self.Sensor3, self.Sensor4, self.Sensor5
    
    def predict_room(self) -> str:
        """predicts the current Room based on the current Sensor Data"""

        roomnames = {1: "Wohnzimmer", 2: "Küche", 3: "Arbeitszimmer", 4: "Diele", 5: "Fließenbereich", 6: "GästeWC", 7: "Flur", 8: "Nina", 9: "Hannah", 10: "Bad", 11: "Justus", 12: "Mom", 13: "Dad"}

        if self.previous_Room != self.current_Room:
            self.previous_Room = self.current_Room
        self.current_Room = roomnames.get(predict_room(s001 = self.Sensor1,s002 = self.Sensor2,s003 = self.Sensor3,s004 = self.Sensor4,s005 = self.Sensor5))

        return self.current_Room
    
    def set_name (self, name: str):
        """ gives the device a name """
        self.name = name