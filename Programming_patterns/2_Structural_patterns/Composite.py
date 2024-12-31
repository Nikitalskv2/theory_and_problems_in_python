'''
Основная идея:

- Компонент (Component) — это интерфейс или абстрактный класс, который определяет общие операции для всех объектов в структуре.
- Лист (Leaf) — это конечный объект, который не содержит других объектов.
- Компоновщик (Composite) — это объект, который содержит другие компоненты (как листы, так и другие компоновщики) и реализует операции для работы с ними.

Преимущества шаблона Composite:

- Упрощение кода: Вы можете работать с древовидной структурой как с единым объектом.
- Гибкость: Легко добавлять новые типы компонентов.
- Расширяемость: Вы можете добавлять новые операции в компоненты, не изменяя существующий код.

Недостатки:

- Сложность: Паттерн может усложнить код, если иерархия объектов слишком глубокая или сложная.
- Ограничения: Не всегда удобно использовать, если компоненты имеют сильно различающиеся интерфейсы.

Когда использовать:

- Когда вам нужно работать с иерархией объектов, где одни объекты содержат другие.
- Когда вы хотите обрабатывать как отдельные объекты, так и их группы одинаково.
- Например, в графических интерфейсах (где элементы могут содержать другие элементы), в файловых системах (где папки содержат файлы и другие папки) и т.д.

'''


from abc import ABC, abstractmethod
from typing import List


# Абстрактный класс Component
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Лист (Leaf)
class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def operation(self) -> str:
        return f"Leaf({self.name})"


# Компоновщик (Composite)
class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self.children: List[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def operation(self) -> str:
        results = [f"Composite({self.name})"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)


# Создаем листья
leaf1 = Leaf("Leaf 1")
leaf2 = Leaf("Leaf 2")
leaf3 = Leaf("Leaf 3")

# Создаем компоновщики
composite1 = Composite("Composite 1")
composite2 = Composite("Composite 2")

# Добавляем листья в компоновщик 1
composite1.add(leaf1)
composite1.add(leaf2)

# Добавляем лист и компоновщик 1 в компоновщик 2
composite2.add(leaf3)
composite2.add(composite1)

# Выполняем операцию для всей структуры
print(composite2.operation())