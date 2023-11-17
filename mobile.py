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

    def delete(self, count: int) -> float:
        self.quantity -= count
        return self.quantity


class CartItem:
    def __init__(self, mobile: Mobile, quanitity: int):
        self.mobile = mobile
        self.quanitity = quanitity

    def total(self):
        return self.mobile.price * self.quanitity

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: CartItem):
        item.mobile.delete(item.quanitity)
        self.items.append(item)

    def check(self):
        data = "Your Cart\n\n"
        total = 0
        number = 1
        for item in self.items:
            total += item.total()
            data += f"{number}. {item.mobile.name} X {item.quanitity} = {item.total()}\n"
            number += 1

        data += f"\nTotal: {total}"

        return data



m1 = Mobile(name='Samsung S21', color='rad', price=350, ram=4, quantity=34)
m2 = Mobile(name='Iphone 12 pro', color='black', price=740, ram=6, quantity=25)
m3 = Mobile(name='Redme 7', color='black', price=250, ram=4, quantity=53)

item1 = CartItem(m1, 3)
item2 = CartItem(m3, 2)

cart = Cart()
cart.add_item(item1)
cart.add_item(item2)

print(cart.check())
