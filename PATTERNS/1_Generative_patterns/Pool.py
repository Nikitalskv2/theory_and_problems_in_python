'''
Пул соединений с базой данных: - (возможно уже есть встроенное решение)
При работе с базой данных мы можем использовать пул соединений,
чтобы ограничить количество активных соединений и переиспользовать существующие вместо создания новых.

Как это работает:
- Очередь соединений: Объекты соединений помещаются в очередь (queue.Queue).
- Получение соединения: Метод acquire извлекает свободное соединение из пула и "активирует" его.
- Возврат соединения: Метод release возвращает объект в пул, делая его доступным для повторного использования.
- Ограничение ресурсов: Пул ограничивает количество одновременно используемых соединений, предотвращая перегрузку системы.

Где это полезно:
- Управление соединениями с базами данных (например, в Django или SQLAlchemy).
- Пул потоков или задач в асинхронных приложениях.
- Ограничение доступа к другим дорогим ресурсам (сокеты, файловые дескрипторы).
'''
import queue


class Connection:
    """Простой класс соединения"""
    def __init__(self, id):
        self.id = id
        self.in_use = False

    def connect(self):
        self.in_use = True
        print(f"Connection {self.id} in use")

    def disconnect(self):
        self.in_use = False
        print(f"Connection {self.id} released")


class ConnectionPool:
    """Реализация пула соединений"""
    def __init__(self, size):
        self.pool = queue.Queue(maxsize=size)
        for i in range(size):
            self.pool.put(Connection(i))

    def acquire(self):
        """Получить соединение из пула"""
        conn = self.pool.get()
        conn.connect()
        return conn

    def release(self, conn):
        """Вернуть соединение в пул"""
        conn.disconnect()
        self.pool.put(conn)


# Использование
if __name__ == "__main__":
    # Создаем пул с 3 соединениями
    connection_pool = ConnectionPool(size=3)

    # Берем соединения из пула
    conn1 = connection_pool.acquire()
    conn2 = connection_pool.acquire()

    # Возвращаем соединение обратно в пул
    connection_pool.release(conn1)

    # Берем еще одно соединение
    conn3 = connection_pool.acquire()

    # Попытка взять соединение, когда пул занят, будет ожидать, пока освободится
    conn4 = connection_pool.acquire()  # Ждет, пока conn2 или conn3 вернутся

    connection_pool.release(conn2)
    connection_pool.release(conn3)
    connection_pool.release(conn4)
