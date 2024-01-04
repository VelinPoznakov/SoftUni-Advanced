from project import Food


class Dessert(Food):
    def __init__(self, name: str, grams: float, price: float, calories: float):
        super().__init__(name, grams, price)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

