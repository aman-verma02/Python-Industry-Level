


"""
❓ Problem
Design:
Add car
Remove car
Capacity limit
Track occupied spots


🧠 Thinking
Use:
list → store cars
limit → capacity

"""



class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []

    def park(self, car):
        if len(self.cars) >= self.capacity:
            return "Parking Full"
        
        self.cars.append(car)
        return f"{car} parked"

    def remove(self, car):
        if car not in self.cars:
            return "Car not found"
        
        self.cars.remove(car)
        return f"{car} removed"

    def available_spots(self):
        return self.capacity - len(self.cars)
    


lot = ParkingLot(2)

print(lot.park("Car1"))
print(lot.park("Car2"))
print(lot.park("Car3"))  # full

print(lot.remove("Car1"))
print(lot.available_spots())


'''
⚠ Edge Cases
Removing non-existing car
Parking when full

'''