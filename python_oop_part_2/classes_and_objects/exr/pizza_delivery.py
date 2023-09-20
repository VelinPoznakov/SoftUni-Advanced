class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity * price_per_quantity

        else:
            self.ingredients[ingredient] += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients.keys() and self.ingredients.get(ingredient) - quantity * price_per_quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients.pop(ingredient)

    def make_order(self):
        self.ordered = True


