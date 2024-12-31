'''
Основная идея:

- Объект предметной области (Domain Object) — это объект, который содержит бизнес-логику и данные.
- Data Mapper — это слой, который отвечает за сохранение и загрузку объектов в базу данных.
- База данных — это хранилище данных, с которым взаимодействует Data Mapper.

Как это работает:

- User — это объект предметной области, который содержит данные и бизнес-логику.
- UserMapper — это интерфейс, который определяет методы для работы с базой данных.
- UserMapperImpl — это конкретная реализация Data Mapper, которая взаимодействует с базой данных (в данном случае — с простым словарем).

Преимущества шаблона Data Mapper:

- Разделение ответственности: Логика работы с базой данных отделена от бизнес-логики.
- Гибкость: Можно легко изменить способ хранения данных, не изменяя объекты предметной области.
- Тестируемость: Легко тестировать объекты предметной области и Data Mapper независимо друг от друга.

Недостатки:

- Сложность: Может увеличить сложность кода из-за введения дополнительного слоя.
- Производительность: В некоторых случаях может привести к дополнительным накладным расходам.

Когда использовать:

- Когда нужно разделить логику работы с базой данных и бизнес-логику.
- Когда вы хотите, чтобы объекты предметной области не знали о способе их хранения.
- Например, в крупных приложениях, где важно разделение ответственности.

Пример из реальной жизни:

- ORM (Object-Relational Mapping): Библиотеки, такие как SQLAlchemy в Python или Hibernate в Java, используют паттерн Data Mapper для работы с базой данных.
- Микросервисы: В микросервисной архитектуре Data Mapper может использоваться для работы с данными в каждом сервисе.

'''


from abc import ABC, abstractmethod


# Объект предметной области
class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"


# Интерфейс Data Mapper
class UserMapper(ABC):
    @abstractmethod
    def get(self, id: int) -> User:
        pass

    @abstractmethod
    def set(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass


# Конкретный Data Mapper
class UserMapperImpl(UserMapper):
    def __init__(self):
        # В реальной жизни это будет подключение к базе данных
        self.users = {}

    def get(self, id: int) -> User:
        if id in self.users:
            return self.users[id]
        raise ValueError(f"User with id {id} not found")

    def set(self, user: User) -> None:
        self.users[user.id] = user

    def delete(self, user: User) -> None:
        if user.id in self.users:
            del self.users[user.id]
        else:
            raise ValueError(f"User with id {user.id} not found")


# Создаем Data Mapper
user_mapper = UserMapperImpl()

# Создаем пользователя
user = User(id=1, name="John Doe", email="john@example.com")

# Сохраняем пользователя
user_mapper.set(user)

# Находим пользователя по id
found_user = user_mapper.get(1)
print(found_user)  # User(id=1, name=John Doe, email=john@example.com)

# Удаляем пользователя
user_mapper.delete(user)

# Пытаемся найти удаленного пользователя
try:
    user_mapper.get(1)
except ValueError as e:
    print(e)  # User with id 1 not found

'''
# Пример: Использование SQLAlchemy в качестве Data Mapper
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

# Определяем модель User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

# Создаем таблицу
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Создаем пользователя
user = User(name="John Doe", email="john@example.com")

# Сохраняем пользователя
session.add(user)
session.commit()

# Находим пользователя по id
found_user = session.query(User).filter_by(id=1).first()
print(found_user)  # User(id=1, name=John Doe, email=john@example.com)

# Удаляем пользователя
session.delete(found_user)
session.commit()

# Пытаемся найти удаленного пользователя
deleted_user = session.query(User).filter_by(id=1).first()
print(deleted_user)  # None
'''