#!/usr/bin/env python3
from main.client import call_service
from config.services import ServiceNames, ServicePorts
from utility.req_resp import GenericRequest

TCP_IP = '192.168.194.95'  # IP address of the A50 sensor
class DVLData:
    def __init__(self, x, y, z, yaw, pitch, roll):
        self.x = x
        self.y = y  
        self.z = z
        self.yaw = yaw 
        self.pitch = pitch
        self.roll = roll
        
    def get_dvl_data(self):
        return call_service(port=ServicePorts[ServiceNames.DVL], 
                    request=GenericRequest(
                        function="generate_fake_data", 
                        args={},
        ))
        

    def parseJson(self, json_dict):
        try:    
            x = json_dict["x"]
            y = json_dict["y"]
            z = json_dict["z"]
            yaw = json_dict["yaw"]
            pitch = json_dict["pitch"]
            roll = json_dict["roll"]

            return [yaw, pitch, roll, x, y, z]
        except Exception as e:
            print("Failed to parse JSON:", e)
            return []  # Return an empty list if parsing fails

    def publishData(self):
        # Publish the extracted A50 sensor data
        print("Publishing State Data:")
        print("Yaw:", self.yaw, "Pitch:", self.pitch, "Roll:", self.roll)
        print("X:", self.x, "Y:", self.y, "Z:", self.z)

    def run_loop(self):
        try:
            dvl_data = self.get_dvl_data()
            while dvl_data is not None:
                a50_data = self.parseJson(dvl_data)
                if a50_data:
                    self.x = a50_data[3]
                    self.y = a50_data[4]
                    self.z = a50_data[5]
                    self.yaw = a50_data[0]
                    self.pitch = a50_data[1]
                    self.roll = a50_data[2]
                    self.publishData()
        except Exception as e:
            print("Error in getting A50 data:", e)

    if __name__ == "__main__":
        run_loop()