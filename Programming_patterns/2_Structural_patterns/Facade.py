'''
Основная идея:

- Фасад (Facade) — это класс, который предоставляет простой интерфейс для работы с подсистемой.
- Подсистема (Subsystem) — это набор классов, которые реализуют сложную функциональность.
- Клиент (Client) — это код, который использует фасад для взаимодействия с подсистемой.

Как это работает:

- SubsystemA и SubsystemB — это классы, которые реализуют сложную функциональность.
- Facade — это класс, который предоставляет простой интерфейс для работы с подсистемой.
- Client — это код, который использует фасад для взаимодействия с подсистемой.

Преимущества шаблона Facade:

- Упрощение интерфейса: Позволяет клиенту работать с подсистемой через простой интерфейс.
- Сокрытие сложности: Скрывает сложность подсистемы от клиента.
- Гибкость: Можно изменять подсистему, не изменяя клиентский код.

Недостатки:

- Ограничения: Фасад может стать "божественным объектом", если он берет на себя слишком много ответственности.
- Сложность: Может увеличить сложность кода, если фасад становится слишком большим.

Когда использовать:

- Когда нужно предоставить простой интерфейс для работы со сложной подсистемой.
- Когда нужно скрыть сложность подсистемы от клиента.
- Например, в библиотеках, фреймворках или крупных приложениях.

Пример из реальной жизни:

Библиотеки: Фасад может предоставить простой интерфейс для работы с сложной библиотекой.
Фреймворки: Фасад может скрыть сложность фреймворка, предоставляя клиенту удобный интерфейс.
Микросервисы: Фасад может объединить несколько микросервисов в один простой интерфейс.
'''


# Подсистема
class SubsystemA:
    def operation_a(self) -> str:
        return "SubsystemA: Ready!"

    def operation_b(self) -> str:
        return "SubsystemA: Go!"


class SubsystemB:
    def operation_a(self) -> str:
        return "SubsystemB: Fire!"

    def operation_b(self) -> str:
        return "SubsystemB: Ready!"


# Фасад
class Facade:
    def __init__(self, subsystem_a: SubsystemA, subsystem_b: SubsystemB):
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_a.operation_a())
        results.append(self._subsystem_b.operation_a())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_a.operation_b())
        results.append(self._subsystem_b.operation_b())
        return "\n".join(results)


# Клиентский код
def client_code(facade: Facade) -> None:
    print(facade.operation())


# Создаем подсистемы
subsystem_a = SubsystemA()
subsystem_b = SubsystemB()

# Создаем фасад
facade = Facade(subsystem_a, subsystem_b)

# Клиентский код использует фасад
client_code(facade)

'''
Facade initializes subsystems:
SubsystemA: Ready!
SubsystemB: Fire!
Facade orders subsystems to perform the action:
SubsystemA: Go!
SubsystemB: Ready!
'''


# Пример: Фасад для работы с файловой системой
'''
class FileReader:
    def read(self, filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()


class FileWriter:
    def write(self, filename: str, content: str) -> None:
        with open(filename, 'w') as file:
            file.write(content)


class FileFacade:
    def __init__(self):
        self._reader = FileReader()
        self._writer = FileWriter()

    def read_file(self, filename: str) -> str:
        return self._reader.read(filename)

    def write_file(self, filename: str, content: str) -> None:
        self._writer.write(filename, content)


# Клиентский код
facade = FileFacade()

# Чтение файла
content = facade.read_file('example.txt')
print(content)

# Запись файла
facade.write_file('example.txt', 'Hello, World!')
'''