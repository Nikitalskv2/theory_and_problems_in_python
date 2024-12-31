'''
Основная идея:

- Абстракция (Abstraction) — это высокоуровневый интерфейс, который определяет поведение.
- Реализация (Implementation) — это низкоуровневый интерфейс, который реализует детали.
- Мост (Bridge) — это связь между абстракцией и реализацией, которая позволяет им изменяться независимо.

Как это работает:

- Implementation — это низкоуровневый интерфейс, который реализует детали.
- Implementation — это низкоуровневый интерфейс, который реализует детали.
- Abstraction — это высокоуровневый интерфейс, который использует реализацию.
- ExtendedAbstraction — это расширенная абстракция, которая может добавлять дополнительные функции.

Преимущества шаблона Bridge:

- Разделение абстракции и реализации: Позволяет изменять их независимо друг от друга.
- Гибкость: Можно добавлять новые абстракции и реализации без изменения существующего кода.
- Упрощение кода: Избегает создания сложных иерархий классов.

Недостатки:

- Сложность: Может увеличить сложность кода из-за введения дополнительных классов.
- Ограничения: Не всегда удобно использовать, если абстракция и реализация тесно связаны.

Когда использовать:

- Когда у вас есть иерархия классов, которая может разрастаться в двух независимых направлениях.
- Когда вы хотите разделить абстракцию и реализацию, чтобы они могли изменяться независимо.
- Например, в графических интерфейсах (где абстракция — это элементы интерфейса, а реализация — это платформа, на которой они отображаются).

Пример из реальной жизни:

- Графические интерфейсы: Абстракция — это элементы интерфейса (кнопки, окна), а реализация — это платформа (Windows, macOS, Linux).
- Драйверы устройств: Абстракция — это высокоуровневый интерфейс для работы с устройством, а реализация — это конкретный драйвер.

'''

from abc import ABC, abstractmethod


# Реализация (Implementation)
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


# Конкретные реализации
class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


# Абстракция (Abstraction)
class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


# Расширенная абстракция
class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


# Клиентский код
def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())


# Создаем реализации
implementation_a = ConcreteImplementationA()
implementation_b = ConcreteImplementationB()

# Создаем абстракции и связываем их с реализациями
abstraction = Abstraction(implementation_a)
client_code(abstraction)

extended_abstraction = ExtendedAbstraction(implementation_b)
client_code(extended_abstraction)
