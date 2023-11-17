class Mobile:
    total_price = 0
    instances = []

    def __init__(self, name: str, color: str, price: float, ram: int, quantity: int):
        self.name  = name
        self.color = color
        self.price = price
        self.ram   = ram
        self.quantity = quantity

        Mobile.total_price += self.total()
        Mobile.instances.append(self)

    def info(self) -> str:
        return f"{self.name} costs {self.price}"

    def total(self) -> float:
        return self.price * self.quantity


m1 = Mobile('Samsung s21', 'black', 700.00, 6, 34)
m2 = Mobile('Ihone 12 pro', 'gray', 600.00, 4, 21)

print(Mobile.total_price)
print(Mobile.instances)
