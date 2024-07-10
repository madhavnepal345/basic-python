#wap/algorithm which can monitor as traffic,
#if any car buses etc goes aginst traffic rule then must fine some amount from bank account
#no helmet fine charges=200
#no seat belt fine charges=100
#no driving license fine charges=500
# high speed=350
#  detect car/ buses number
#  find details of vehicles with their vehicles number and reduce amount from their account


class Vehicle:
    def __init__(self,number,account):
        self.number=number
        self.account=account
class Trafficmonitor:
    def __init__(self):
        self.vehicles=[]
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def fine_vehicle(self,vehicle,fine):
        vehicle.account-=fine

    def check_helmet(self,vehicle):
        if vehicle.number[0]!= "H":
            self.fine_vehicle(vehicle,200)

    def check_seatbelt(self,vehicle):
        if vehicle.number[0] != "C":
            self.fine_vehicle(vehicle,300)
    

    def check_highspeed(self,vehicle,speed_limit):
        if int (vehicle.number[1:])>speed_limit:
            self.fine_vehicle(vehicle,500)
    
    def monitor_traffic(self):
        for vehicle in self.vehicles:
            self.check_helmet(vehicle)
            self.check_seatbelt(vehicle)
            
            self.check_highspeed(vehicle, 100)
monitor = Trafficmonitor()
monitor.add_vehicle(Vehicle('H123', 1000))
monitor.add_vehicle(Vehicle('C456', 2000))
monitor.add_vehicle(Vehicle('D789', 3000))

monitor.monitor_traffic()


print(monitor.vehicles[0].account) 
print(monitor.vehicles[1].account) 
print(monitor.vehicles[2].account) 