'''
Когда использовать Singleton:
- Управление ресурсами (например, пул соединений с базой данных).
- Глобальная точка доступа к объекту (например, конфигурация приложения или логгер).
- Гарантия единственного экземпляра (например, кеш, работа с внешними API).
'''


# 1. Через классический подход с атрибутом класса:
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Проверка
a = Singleton()
b = Singleton()
print(a is b)  # True, оба объекта — один и тот же экземпляр


# 2. Через декоратор:
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class SingletonClass:
    pass


# Проверка
a = SingletonClass()
b = SingletonClass()
print(a is b)  # True


# 3. Через метакласс:
# Этот способ более сложный и чаще используется в продвинутых сценариях.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


a = Singleton()
b = Singleton()
print(a is b)  # True

