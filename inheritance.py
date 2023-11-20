class Animal:
    def __init__(self, name: str):
        self.name = name

    def description(self):
        return  f"{self.name} is animal."


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def description(self):
        return  f"{self.name} is dog and {self.age} years old."

class Cat(Animal):
    def __init__(self, name: str, age: int):
        Animal.__init__(self, name)
        self.age = age

    def description(self):
        return  f"{self.name} is cat and {self.age} years old."

a = Animal("cow")
d = Dog("simba", 3)
c = Cat("mosh", 5)

print(a.description())
print(d.description())
print(c.description())