# 3. Abstract Factory
# Для создания семейств связанных объектов.

from abc import ABC, abstractmethod
'''
определяем:
- абстрактные обьекты
- конкретные обьекты
- абстрактную фабрику
- конкрытные фабрики (simple factory)

'''

# Абстрактные продукты
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Table(ABC):
    @abstractmethod
    def place_items(self):
        pass


# Конкретные продукты
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."


class ModernTable(Table):
    def place_items(self):
        return "Items placed on a modern table."


class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair."


class VictorianTable(Table):
    def place_items(self):
        return "Items placed on a Victorian table."


# Абстрактная фабрика
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


# Конкретные фабрики
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_table(self):
        return VictorianTable()


# Использование
def furnish_home(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    print(chair.sit_on())
    print(table.place_items())


# Пример вызова
modern_factory = ModernFurnitureFactory()
furnish_home(modern_factory)

victorian_factory = VictorianFurnitureFactory()
furnish_home(victorian_factory)
