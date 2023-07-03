class vehicle:
    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand

    def vehicle(self):
        raise NotImplementedError("Child class must implement this method ")


class Toyota(vehicle):
    def vehicle(self):
        return "Totota!"


class Nissan(vehicle):
    def vehicle(self):
        return "Nissan!"


vehicle = vehicle("vitz", "Red", "Toyota")
print(vehicle.name)
print(vehicle.color)
print(vehicle.brand)
