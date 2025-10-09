#1
def type_check(*expected_types, **expected_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Позиционный аргумент {arg} должен быть типа {expected}, но получен {type(arg)}")

            for key, expected in expected_kwargs.items():
                if key in kwargs and not isinstance(kwargs[key], expected):
                    raise TypeError(f"Аргумент '{key}' должен быть типа {expected}, но получен {type(kwargs[key])}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

def process_data(a, b, c, z=0.0):
    print(f"a: {a}, b: {b}, c: {c}, z: {z}")

process_data = type_check(int, str, z=float)(process_data)
process_data(10, "тест", [1, 2, 3], z=3.14)
process_data(42, "данные", None, z=0.0)
#process_data("10", "тест", [], z=3.14) # а тут уже ошибку выдаст


#2

def cache_results(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Возвращаю из кэша")
            return cache[key]
        print("Вычисляю заново")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

def multiply(a, b=1):
    print(f"Выполняю: {a} * {b}")
    return a * b

print(multiply(3, b=4))  
print(multiply(3, b=4))  
print(multiply(3))   

#3

def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, dict):
            raise TypeError("Ожидался словарь с данными пользователя")

        if not user.get("is_authenticated"):
            raise PermissionError("Пользователь не авторизован")

        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_dashboard(user):
    return f"Добро пожаловать, {user['name']}!"

user1 = {"name": "Артём", "is_authenticated": True}
user2 = {"name": "Гость", "is_authenticated": False}

print(view_dashboard(user1))  # Добро пожаловать, Артём!
#print(view_dashboard(user2))  # PermissionError: Пользователь не авторизован

#4 нет задачки

#5
import time

def retry_on_exception(retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Ошибка: {e}. Повтор через {delay} сек...")
                    time.sleep(delay)
            print("Финита ля комедия")
        return wrapper
    return decorator

#6

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
 
 #7     
def divisible_by_3_or_5(limit):
    for number in range(1, limit + 1):
        if number % 3 == 0 or number % 5 == 0:
            yield number
#8
def factorial_generator():
    n = 1
    result = 1
    while True:
        result *= n
        yield result
        n += 1
#9
def every_nth_element(data, n):
    for i in range(0, len(data), n):
        yield data[i]
#10
def limit_calls(func, max_calls):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        if count >= max_calls:
            raise RuntimeError(f"Функция может быть вызвана не более {max_calls} раз")
        count += 1
        return func(*args, **kwargs)

    return wrapper
#11
def make_membership_checker(numbers):
    def checker(value):
        return value in numbers
    return checker
#12
def make_formatter(template):
    def formatter(**kwargs):
        return template.format(**kwargs)
    return formatter
#13
def difference_tracker():
    previous = None

    def tracker(current):
        nonlocal previous
        if previous is None:
            result = None  # Первый вызов — нет предыдущего значения
        else:
            result = current - previous
        previous = current
        return result

    return tracker
#14
def count_calls_by_argument(func):
    counts = {}

    def wrapper(arg):
        counts[arg] = counts.get(arg, 0) + 1
        print(f"Аргумент '{arg}' был вызван {counts[arg]} раз(а)")
        return func(arg)

    return wrapper

