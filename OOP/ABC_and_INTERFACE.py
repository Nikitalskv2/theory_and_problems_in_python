'''

Абстрактный класс:
- цель -            частичная реализация и наследование
- методы -          могут быть с частичной реализацией
- атрибуты -        могут содержать атрибуты
- реализация -      модуть abs (метод @abstractmethod)
- наследование -    раз класс может наследовать только один     class Bird(Animal):
- применение -      создание базового функционала

Интерфейс:
- цель -            определение только структуры
- методы -          все абстрактны
- атрибуты -        обычно нет
- реализация -      модуть abs (метод @abstractmethod)
- наследование -    класс может реализовать несколько интерфейсов   class Penguin(Bird, Swimming):
- применение -      задать структуру для реализации

'''


from abc import ABC, abstractmethod


class Animal(ABC):  # abc class
    @abstractmethod
    def walking(self):
        # реализация
        print("walking")


class Flyable(ABC):     # Interface
    @abstractmethod
    def fly(self):
        pass


class Swimming(ABC):    # Interface
    @abstractmethod
    def swim(self):
        pass


class Bird(Animal):  # реализация
    def walking(self):
        print("bird walking")


class Penguin(Bird, Swimming):
    def walking(self):
        print("penguin walking")

    def swim(self):
        print("penguin swim")


penguin = Penguin()
penguin.walking()
penguin.swim()


class Duck(Bird, Flyable, Swimming):
    def walking(self):
        print("duck walking")

    def fly(self):
        print("duck fly")

    def swim(self):
        print("duck swim")


duck = Duck()
duck.walking()
duck.fly()
duck.swim()

