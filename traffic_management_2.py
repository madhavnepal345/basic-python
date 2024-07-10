import random

class TrafficControl:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
        self.vehicle_details = self.get_vehicle_details(vehicle_number)
        self.speed = self.get_speed_vehicle()
        self.fine_amount = 0

    def get_vehicle_details(self, vehicle_number):
        return {"owner_name": "Ram", "account_num": "00823667413", "mobile_number": "9808908"}

    def get_speed_vehicle(self):
        return random.randint(1, 200)

    def detect_helmet(self):
        return random.choice([True, False])

    def detect_seatbelt(self):
        return random.choice([True, False])

    def detect_single(self):
        return random.choice([True, False])

    def is_ok(self):
        if self.speed > 60:
            self.fine_amount = 350
            return False
        elif self.detect_helmet():
            self.fine_amount = 200
            return False
        elif  self.detect_seatbelt():
            self.fine_amount = 150
            return False
        elif self.detect_single():
            self.fine_amount = 100
            return False
        else:
            return True

    def fine(self):
        print(f"Fining {self.vehicle_details['owner_name']} Rs{self.fine_amount} for violating traffic rules.")
        print(f"Deducting Rs{self.fine_amount} from account {self.vehicle_details['account_num']}")

while True:
    vehicle_number = input("Enter vehicle number: ")
    vehicle_obj = TrafficControl(vehicle_number)
    if not vehicle_obj.is_ok():
        vehicle_obj.fine()