from lp4 import Animal

class Cat(Animal):

    breed: str
    age: int

    def __init__(self, name, breed, age):

        super().__init__(name)

        self.breed = breed
        self.age = age