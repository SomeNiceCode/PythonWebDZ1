#CLASSWORK

#1
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    # геттеры и сеттеры
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным числом.")

    # вывод инфы о книге
    def display_info(self):
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Страниц: {self.__pages}")

    # больше ли 300 стр
    def is_long_book(self):
        return self.__pages > 300
    
#2    
class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def decrement(self):
        self.__count -= 1

    def reset(self):
        self.__count = 0

    def get_value(self):
        return self.__count

#3    
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Деление на ноль!"
        
print(Calculator.add(10, 5))        
print(Calculator.subtract(10, 5))   
print(Calculator.multiply(10, 5))   
print(Calculator.divide(10, 0))     

#4
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # геты\сеты
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Ширина должна быть положительным числом.")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Высота должна быть положительным числом.")

    # площадь
    def area(self):
        return self.__width * self.__height

    # периметр
    def perimeter(self):
        return 2 * (self.__width + self.__height)

    # является ли прямоугольник квадратом
    def is_square(self):
        return self.__width == self.__height
    
#5
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Нема денях!")

    def display_balance(self):
        print(f"Баланс {self.__owner}: {self.__balance:.2f}₴")
