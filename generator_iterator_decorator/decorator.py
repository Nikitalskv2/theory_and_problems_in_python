from functools import wraps
'''
Декоратор — это функция, которая принимает другую функцию (или класс) в качестве аргумента,
модифицирует её поведение, и возвращает новую или ту же функцию.
Это удобный способ добавлять функциональность к существующему коду без его изменения.
'''


### 1. Простой декоратор
def simple_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()  # Вызов исходной функции
        print("После вызова функции.")
    return wrapper


@simple_decorator
def say_hello():
    print("Привет, мир!")


say_hello()


### 2. Декоратор с переменной
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)  # Вызываем оригинальную функцию
        return wrapper
    return decorator


@repeat_decorator(3)
def say_hello():
    print("Привет, мир!")


say_hello()


### 3.Пример_ Декоратор для проверки прав
def require_permission(permission):
    def decorator(func):
        @wraps(func)  # Сохраняет метаданные оригинальной функции
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")  # Допустим, пользователь передаётся через kwargs
            if not user or permission not in user.get("permissions", []):
                raise PermissionError(f"У пользователя недостаточно прав для {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_permission("view_dashboard")
def get_dashboard_data(*args, **kwargs):
    return {"data": "Данные для дашборда"}


user = {"permissions": ["view_dashboard"]}
try:
    print(get_dashboard_data(user=user))
except PermissionError as e:
    print(e)

