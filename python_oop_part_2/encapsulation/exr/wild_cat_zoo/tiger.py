from python_oop_part_2.encapsulation.exr.wild_cat_zoo.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 45)

