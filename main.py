class Person:
    name = "Person class"
    count = 0

    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name  = lname
        self.age        = age

        Person.count += 1

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


p1 = Person('Ali', 'Valiyev', 23)
p2 = Person('Gani', 'Soliyev', 17)
p3 = Person('Asil', 'Nasimov', 20)

print(Person.count)
