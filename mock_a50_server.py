from random import choice, uniform

class DVLMockServer:
    def generate_fake_data():
        fake_data = {}
        
        
        # Generate random values for orientation or skip
        if choice([True, False]):    # Generate random values for position
            fake_data["x"] = uniform(0, 100)
            fake_data["y"] = uniform(0, 100)
            fake_data["z"] = uniform(0, 100)
            fake_data["yaw"] = uniform(-180, 180)
            fake_data["pitch"] = uniform(-180, 180)
            fake_data["roll"] = uniform(-180, 180)

            
        else:
            # Alternatively, include "sx", "sy", "sz" without orientation info
            fake_data["sx"] = uniform(0, 100)
            fake_data["sy"] = uniform(0, 100)
            fake_data["sz"] = uniform(0, 100)
        
        return fake_data
