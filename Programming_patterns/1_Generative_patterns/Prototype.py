'''
Реальный пример: Копирование конфигураций
Представим ситуацию, где у нас есть объект конфигурации приложения.
Вместо создания новых объектов конфигурации с нуля,
мы можем скопировать уже существующий объект и внести в него изменения.


Как это работает:
- Prototype: У нас есть базовый класс Prototype, который предоставляет метод clone, использующий copy.deepcopy.
- Клонирование: Создаем базовый объект base_config. С помощью метода clone получаем его копию и модифицируем её, не затрагивая оригинал.
- Результат: Мы быстро создаем новые экземпляры, основанные на существующем объекте, без необходимости повторной инициализации.


Где это полезно:
- Быстрое создание тестовых объектов с небольшими изменениями.
- Сохранение состояния и его копирование (например, в игре или редакторе).
- Ускорение создания объектов, если их создание с нуля занимает много ресурсов.
'''

import copy


# Базовый класс, который поддерживает клонирование
class Prototype:
    def clone(self):
        return copy.deepcopy(self)


# Реализация конкретного объекта
class AppConfig(Prototype):
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings

    def __str__(self):
        return f"AppConfig(name={self.name}, settings={self.settings})"


# Использование
if __name__ == "__main__":
    # Создаем базовую конфигурацию
    base_config = AppConfig("BaseConfig", {"debug": True, "version": "1.0"})

    # Клонируем базовую конфигурацию
    user_config = base_config.clone()
    user_config.name = "UserConfig"
    user_config.settings["debug"] = False
    user_config.settings["version"] = "2.0"

    print(base_config)  # AppConfig(name=BaseConfig, settings={'debug': True, 'version': '1.0'})
    print(user_config)  # AppConfig(name=UserConfig, settings={'debug': False, 'version': '2.0'})