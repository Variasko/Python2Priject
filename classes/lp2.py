class Dog:

    name: str
    age: int
    breed: str

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog = Dog("Rex", 3, "Labrador")

print(dog.name)
print(dog.age)
print(dog.breed)

dog.age += 1

print(dog.age)

dog.owner = "Bob"

print(dog.owner)