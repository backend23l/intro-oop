class Tortburchak(object):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self) -> int:
        return self.a * self.b


class Kvadrat(Tortburchak):
    def __init__(self, a: int):
        super().__init__(a, a)

    def __str__(self) -> str:
        return f"{self.a}X{self.b}"


k = Kvadrat(6)

print(str(k))
print(k)