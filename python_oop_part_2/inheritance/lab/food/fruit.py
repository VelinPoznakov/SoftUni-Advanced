from python_oop_part_2.inheritance.lab.food.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name


print(Fruit("PEsh", "23.04.09"))
