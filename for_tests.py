class Vehicle:
    def __init__(self, model: str, doors: int, fuel: float):
        self.model = model
        self.doors = doors
        self.fuel = fuel

    def __repr__(self) -> str:
        return self.model 


class Car(Vehicle):
    def __init__(self, model, doors, fuel):
        super().__init__(model, doors, fuel)


car = Car('BMW', 4, 25.3)
print(car.model)
