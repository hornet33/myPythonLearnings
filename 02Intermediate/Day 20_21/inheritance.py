# eg. below - a monkey class inherits from the animal super class
class Animal:
    def __init__(self):
        self.animal_type = "animal"

    def move(self):
        print(f"{self.animal_type} moving")


class Monkey(Animal):
    def __init__(self):  # Monkey constructor
        super().__init__()  # Invoking the constructor of parent class Animal
        self.animal_type = "monkey"  # Monkey inherits the field "animal_type" and can set it to its own value

    def move(self):
        super().move()  # Invoking super class method
        print(f"{self.animal_type} swinging")


monkey = Monkey()
print(monkey.animal_type)
print(monkey.move())
