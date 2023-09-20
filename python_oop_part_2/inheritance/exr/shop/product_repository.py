from python_oop_part_2.inheritance.exr.shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product_name)

    def __repr__(self):
        res = '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
        return res
