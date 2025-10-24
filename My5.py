1. Создайте дескриптор PositiveValue, который:
Разрешает устанавливать только положительные числа. Используйте этот дескриптор в классе BankAccount для проверки баланса счета.
Добавьте возможность создать объект BankAccount с заданным именем владельца и начальными средствами.
Если попытаться установить отрицательное значение или ноль, выбрасывает ValueError.

Добавьте еще один дескриптор Name для проверки имени владельца:
- Имя должно быть строкой.
- Имя должно содержать только буквы и начинаться с заглавной.

class PositiveValue:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if value <= 0:
            raise ValueError("Значение должно быть положительным")
        setattr(instance, self.private_name, value)


class Name:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        if not value.isalpha():
            raise ValueError("Имя должно содержать только буквы")
        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")
        setattr(instance, self.private_name, value)


class BankAccount:
    owner = Name()
    balance = PositiveValue()

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


2. Создайте дескриптор LogDescriptor, который:
Логирует каждый доступ к атрибуту, включая чтение и запись.

class LogDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name, None)
        print(f"[LOG] Чтение {self.private_name} = {value}")
        return value

    def __set__(self, instance, value):
        print(f"[LOG] Запись {self.private_name} = {value}")
        setattr(instance, self.private_name, value)


class Example:
    x = LogDescriptor()

    def __init__(self, x):
        self.x = x

3. Напишите метакласс, который не позволяет создавать классы с атрибутами, начинающимися с подчеркивания. 
Если класс содержит такие атрибуты, метакласс должен выбрасывать исключение.
Реализуйте метакласс, который проверяет атрибуты класса на соответствие этому ограничению.
Напишите несколько классов с атрибутами, начинающимися с подчеркивания, и убедитесь, что будет выброшено исключение.

class NoUnderscoreAttrs(type):
    def __new__(cls, name, bases, attrs):
        for key in attrs:
            if key.startswith("_"):
                raise AttributeError(f"Атрибут {key} запрещён")
        return super().__new__(cls, name, bases, attrs)


4. Создайте метакласс, который автоматически добавляет в каждый класс метод hello(), который выводит строку "Hello from <имя класса>".
Реализуйте метакласс, который добавляет метод hello() в каждый класс.
Напишите несколько классов, использующих этот метакласс, и вызовите метод hello() для каждого класса.

class HelloMeta(type):
    def __new__(cls, name, bases, attrs):
        def hello(self):
            print(f"Hello from {name}")
        attrs["hello"] = hello
        return super().__new__(cls, name, bases, attrs)


class A(metaclass=HelloMeta): pass
class B(metaclass=HelloMeta): pass

5. Напишите метакласс, который не позволяет классам наследовать другие классы, если в имени родительского класса есть подстрока "Forbidden".
Реализуйте метакласс, который проверяет имя родительского класса и запрещает наследование от классов с подстрокой "Forbidden" в имени.
Напишите несколько классов с этим метаклассом, и попробуйте создать класс, наследующий от запрещенного класса.

class NoForbiddenInheritance(type):
    def __new__(cls, name, bases, attrs):
        for base in bases:
            if "Forbidden" in base.__name__:
                raise TypeError(f"Нельзя наследовать от {base.__name__}")
        return super().__new__(cls, name, bases, attrs)


class ForbiddenBase: pass

6. Создайте метакласс, который проверяет, что каждый атрибут класса является строкой. Если атрибут не является строкой, выбрасывайте исключение.
Реализуйте метакласс, который проверяет тип атрибутов класса.
Напишите класс с атрибутами разных типов (например, строками и числами) и убедитесь, что метакласс выбрасывает исключение, если тип атрибута некорректен.

class OnlyStrings(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if not key.startswith("__") and not isinstance(value, str):
                raise TypeError(f"Атрибут {key} должен быть строкой")
        return super().__new__(cls, name, bases, attrs)

7. Создайте протокол Shape, который требует реализации метода area() для вычисления площади фигуры. Реализуйте несколько классов, таких как Circle, Rectangle и Triangle, которые будут реализовывать данный протокол. 
Напишите функцию, которая принимает объекты, реализующие протокол Shape, и выводит их площадь.
Протокол Shape должен содержать метод area().
Классы Circle, Rectangle и Triangle должны реализовывать метод area(), соответствующий их геометрической форме.
Функция print_area() должна принимать объект, реализующий протокол Shape, и выводить площадь.


class Shape(Protocol):
    def area(self) -> float: ...


class Circle:
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return math.pi * self.r ** 2


class Rectangle:
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h


class Triangle:
    def __init__(self, a: float, h: float):
        self.a, self.h = a, h
    def area(self) -> float:
        return 0.5 * self.a * self.h


def print_area(shape: Shape):
    print(f"Площадь: {shape.area()}")

8. Создайте протокол Serializable, который требует реализации метода serialize(). Реализуйте два класса: Person и Book, которые будут реализовывать этот метод для преобразования объектов в строковый формат JSON.
Протокол Serializable должен содержать метод serialize().
Классы Person и Book должны реализовывать метод serialize(), возвращающий строку в формате JSON.
Напишите функцию serialize_object(), которая будет принимать объект и вызывать его метод serialize().

class Serializable(Protocol):
    def serialize(self) -> str: ...


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def serialize(self) -> str:
        return json.dumps({"name": self.name, "age": self.age})


class Book:
    def __init__(self, title, author):
        self.title, self.author = title, author
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "author": self.author})


def serialize_object(obj: Serializable):
    print(obj.serialize())