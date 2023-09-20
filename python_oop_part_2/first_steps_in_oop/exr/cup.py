class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, amount_quantity):
        if self.size >= self.quantity + amount_quantity:
            self.quantity += amount_quantity  #запомни МНОГО ВАЖНО!!!!

    def status(self):
        return abs(self.size - self.quantity)


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
