from python_oop_part_2.encapsulation.exr.food.food.food import Food


class Dessert(Food):
    def __init__(self, grams: float, name: str, price: float, calories: float):
        super().__init__(grams, name, price)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

