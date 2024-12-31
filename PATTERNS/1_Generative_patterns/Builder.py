'''
Основные концепции паттерна Builder:
Builder — интерфейс, определяющий шаги построения объекта.
Concrete Builder — конкретная реализация интерфейса, которая создает и собирает части объекта.
Director — управляет процессом построения, определяя порядок вызова шагов.
Product — готовый объект, который нужно создать.

Когда использовать:
- Когда объект сложен и имеет много частей, которые нужно конфигурировать.
- Когда нужно гарантировать, что процесс создания объекта стандартизирован.
- Когда создание объекта требует разного представления.

'''


# 1. Пример из реальной разработки: создание конфигурации для сложной системы
# Мы создаем конфигурацию для веб-приложения, которая включает несколько этапов: настройку базы данных, API и кеша.

# Product: объект, который мы собираем
class WebAppConfig:
    def __init__(self):
        self.config = {}

    def __str__(self):
        return str(self.config)


# Builder: интерфейс для создания частей объекта
class ConfigBuilder:
    def __init__(self):
        self.config = WebAppConfig()

    def set_database(self, db_url):
        self.config.config["database"] = db_url

    def set_cache(self, cache_url):
        self.config.config["cache"] = cache_url

    def set_api(self, api_url):
        self.config.config["api"] = api_url

    def get_result(self):
        return self.config


# Director: управляет процессом сборки
class WebAppConfigDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_full_config(self):
        self.builder.set_database("postgres://localhost")
        self.builder.set_cache("redis://localhost")
        self.builder.set_api("http://api.example.com")


# Использование
builder = ConfigBuilder()
director = WebAppConfigDirector(builder)

# Пошаговое построение
director.build_full_config()
config = builder.get_result()

print(config)
# Вывод: {'database': 'postgres://localhost', 'cache': 'redis://localhost', 'api': 'http://api.example.com'}







