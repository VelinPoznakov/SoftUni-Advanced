from python_oop_part_2.encapsulation.exr.food.beverage.cold_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, milliliters: float, name: str, price: float, caffeine: float):
        super().__init__(milliliters, name, price)
        self.__caffeine = caffeine


    @property
    def caffeine(self):
        return self.__caffeine


