'''
Преимущества шаблона Registry:

- Централизованное управление: Все объекты или фабрики хранятся в одном месте.
- Гибкость: Можно легко добавлять, удалять или заменять объекты.
- Расширяемость: Подходит для реализации плагинов или модульных систем.

Недостатки:
- Глобальное состояние: Реестр может стать глобальной переменной, что усложняет тестирование и сопровождение.
- Потенциальные конфликты: Необходимо следить за уникальностью ключей.

Когда использовать:

- Когда нужно управлять множеством объектов или фабрик в одном месте.
- Для реализации плагинов или модульных систем.
- В dependency injection для хранения зависимостей.
'''


class Registry:
    def __init__(self):
        # Словарь для хранения зарегистрированных объектов или фабрик
        self._registry = {}

    def register(self, key, value):
        """Регистрация объекта или фабрики по ключу."""
        if key in self._registry:
            raise ValueError(f"Key '{key}' is already registered.")
        self._registry[key] = value

    def get(self, key):
        """Получение объекта по ключу."""
        if key not in self._registry:
            raise KeyError(f"Key '{key}' is not registered.")
        return self._registry[key]

    def unregister(self, key):
        """Удаление объекта из реестра."""
        if key in self._registry:
            del self._registry[key]

    def clear(self):
        """Очистка реестра."""
        self._registry.clear()

    def __contains__(self, key):
        """Проверка наличия ключа в реестре."""
        return key in self._registry

    def __repr__(self):
        """Представление реестра для отладки."""
        return f"Registry({self._registry})"


# Создаем реестр
registry = Registry()


class Dog:
    def __init__(self, name):
        self.name = name


dog_Waf = Dog("Waf")

# Регистрируем объекты
registry.register('greeting', "Hello, World!")
registry.register('pi', 3.14159)
registry.register('dog', dog_Waf)

# Получаем объекты
print(registry.get('greeting'))  # Hello, World!
print(registry.get('pi'))        # 3.14159
print(registry.get('dog'))

print(registry)

# Проверяем наличие ключа
print('pi' in registry)  # True

# Удаляем объект
registry.unregister('pi')
print('pi' in registry)  # False

# Очищаем реестр
registry.clear()
print(registry)  # Registry({})