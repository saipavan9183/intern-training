class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Bow!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [
    Dog("buddy"),
    Cat("Whiskers"),
    Dog("Max"),
    Cat("Luna")
] 

print("---- Polymorphism Demo ----")
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
