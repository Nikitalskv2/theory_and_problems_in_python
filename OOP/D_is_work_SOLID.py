import asyncio
from abc import ABC, abstractmethod


# Абстракция:
class PriceDataSource(ABC):     # Абстракный класс тк есть реализация логикиN
    @abstractmethod
    async def get_prices(self) -> dict:
        """
        б-логика
        Получить данные о ценах
        """
        pass


# Реализация для API:
class APIPriceDataSource(PriceDataSource):
    async def get_prices(self) -> dict:
        # Логика запроса к API
        return {"item1": 100, "item2": 200}


# Реализация для парсинга:
class WebScrapingPriceDataSource(PriceDataSource):
    async def get_prices(self) -> dict:
        # Логика парсинга сайта
        return {"item1": 110, "item2": 210}


# Использование:
async def process_prices(data_source: PriceDataSource):
    prices = await data_source.get_prices()
    print(prices)
    # Работа с ценами


data_source_API = APIPriceDataSource()
data_source_Web = WebScrapingPriceDataSource()


asyncio.run(process_prices(data_source_API))
asyncio.run(process_prices(data_source_Web))
# Здесь process_prices зависит от интерфейса PriceDataSource, а не от конкретной реализации.