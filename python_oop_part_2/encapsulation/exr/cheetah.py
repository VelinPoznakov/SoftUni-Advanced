from python_oop_part_2.encapsulation.exr.animal import Animal


class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 50)