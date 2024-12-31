# 2. Factory Method
# Создание объекта делегируется подклассам.

from abc import ABC, abstractmethod
'''
определяем:
- абстрактный обьект
- классы конкретных обьектов
- фабрика 
- конкретные фабрики 
'''

# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Конкретные реализации
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Фабричный метод
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Конкретные фабрики
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


factory = DogFactory()
animal = factory.create_animal()
print(animal.speak())  # Woof!
