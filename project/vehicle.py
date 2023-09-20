class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int, fuel_consumption):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.fuel - (self.fuel_consumption * kilometers) >= 0:
            self.fuel -= (self.fuel_consumption * kilometers)
