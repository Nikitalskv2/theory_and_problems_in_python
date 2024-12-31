'''
Основная идея:

- Flyweight — это объект, который содержит общие данные, которые могут быть разделены между множеством объектов.
- Контекст (Context) — это объект, который содержит уникальные данные и ссылку на Flyweight.
- Flyweight Factory — это фабрика, которая управляет созданием и повторным использованием Flyweight объектов.

Преимущества шаблона Flyweight:

- Экономия памяти: Уменьшает использование памяти за счет разделения общих данных.
- Производительность: Уменьшает количество создаваемых объектов, что может повысить производительность.
- Гибкость: Позволяет легко добавлять новые Flyweight объекты.

Недостатки:

- Сложность: Может увеличить сложность кода из-за введения дополнительных классов.
- Ограничения: Не всегда подходит для всех типов объектов, особенно если объекты имеют много уникальных данных.

Когда использовать:

- Когда у вас есть множество объектов, которые содержат одинаковые данные.
- Когда вы хотите уменьшить использование памяти за счет разделения общих данных.
- Например, в графических редакторах (где множество объектов могут иметь одинаковые текстуры), в текстовых редакторах (где множество символов могут иметь одинаковые шрифты) и т.д.

Пример из реальной жизни:

- Графические редакторы: Flyweight может использоваться для разделения общих текстур, шрифтов и других ресурсов.
- Текстовые редакторы: Flyweight может использоваться для разделения общих символов и шрифтов.
- Игры: Flyweight может использоваться для разделения общих ресурсов, таких как текстуры, звуки и модели.
'''

from typing import Dict


# Flyweight
class Flyweight:
    def __init__(self, shared_state: str):
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        print(f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state.")


# Flyweight Factory
class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict[str, str]):
        for state in initial_flyweights:
            self._flyweights[state] = Flyweight(state)

    def get_flyweight(self, shared_state: str) -> Flyweight:
        if shared_state not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[shared_state] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[shared_state]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for key in self._flyweights:
            print(key)


# Контекст
class Context:
    def __init__(self, flyweight: Flyweight, unique_state: str):
        self._flyweight = flyweight
        self._unique_state = unique_state

    def operation(self) -> None:
        self._flyweight.operation(self._unique_state)


# Инициализация фабрики с начальными Flyweight объектами
initial_flyweights = {
    "A": "Shared state A",
    "B": "Shared state B",
}
factory = FlyweightFactory(initial_flyweights)

# Получение Flyweight объектов
flyweight_a = factory.get_flyweight("A")
flyweight_b = factory.get_flyweight("B")
flyweight_c = factory.get_flyweight("C")

# Создание контекстов
context1 = Context(flyweight_a, "Unique state 1")
context2 = Context(flyweight_b, "Unique state 2")
context3 = Context(flyweight_c, "Unique state 3")

# Выполнение операций
context1.operation()
context2.operation()
context3.operation()

# Вывод списка Flyweight объектов
factory.list_flyweights()

'''
FlyweightFactory: Reusing existing flyweight.
FlyweightFactory: Reusing existing flyweight.
FlyweightFactory: Can't find a flyweight, creating new one.
Flyweight: Displaying shared (Shared state A) and unique (Unique state 1) state.
Flyweight: Displaying shared (Shared state B) and unique (Unique state 2) state.
Flyweight: Displaying shared (C) and unique (Unique state 3) state.
FlyweightFactory: I have 3 flyweights:
A
B
C
'''


# Пример: Flyweight для текстового редактора
'''
class CharacterFlyweight:
    def __init__(self, char: str, font: str):
        self._char = char
        self._font = font

    def render(self, position: int) -> None:
        print(f"Character '{self._char}' with font '{self._font}' at position {position}.")


class CharacterFactory:
    _characters: Dict[str, CharacterFlyweight] = {}

    def get_character(self, char: str, font: str) -> CharacterFlyweight:
        key = f"{char}_{font}"
        if key not in self._characters:
            self._characters[key] = CharacterFlyweight(char, font)
        return self._characters[key]


# Клиентский код
factory = CharacterFactory()

# Создание символов
char1 = factory.get_character('A', 'Times New Roman')
char2 = factory.get_character('B', 'Arial')
char3 = factory.get_character('A', 'Times New Roman')

# Рендеринг символов
char1.render(1)
char2.render(2)
char3.render(3)


# Character 'A' with font 'Times New Roman' at position 1.
# Character 'B' with font 'Arial' at position 2.
# Character 'A' with font 'Times New Roman' at position 3.
'''