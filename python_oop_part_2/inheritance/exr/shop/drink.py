from python_oop_part_2.inheritance.exr.shop.product import Product


class Drink(Product):
    def __init__(self,name):
        super().__init__(name, 10)
