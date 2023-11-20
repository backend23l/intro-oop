class Tortburchak:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self) -> int:
        return self.a * self.b


class Kvadrat(Tortburchak):
    def __init__(self, a: int):
        super().__init__(a, a)


k = Kvadrat(6)
print(k.area())
