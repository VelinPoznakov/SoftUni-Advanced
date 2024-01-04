from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0


class Bird(ABC, Animal):
    def __init__(self, wing_size: float, name: str, weight: float):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(ABC, Animal):
    def __init__(self, living_region: str, name: str, weight: float):
        super().__init__(name, weight)
        self.living_region = living_region

