from python_oop_part_2.encapsulation.exr.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        is_enough_budget = self.__budget >= price
        is_enougt_compacity = len(self.animals) < self.__animal_capacity

        if is_enougt_compacity and is_enough_budget:
            self.animals.append(animal)
            return  f"{self.name} the {animal.__class__.__name__} added to the zoo"



