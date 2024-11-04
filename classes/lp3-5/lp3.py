class Animal:

    name: str

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks!")


class Dog(Animal):

    breed: str

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Spot")
dog.speak()