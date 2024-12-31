# 1. Simple Factory
# Один метод управляет созданием экземпляров разных классов.

class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


dog_1 = AnimalFactory.create_animal("dog")
dog_2 = AnimalFactory.create_animal("dog")
print(dog_1.speak(), dog_1.__class__)  # Woof!
print(dog_2.speak(), dog_2.__class__)  # Woof!
print(dog_1 is dog_2)   # False разные
