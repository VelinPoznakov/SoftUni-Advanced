from project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, milliliters: float, price: float, caffeine: float):
        super().__init__(name, milliliters, price)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
