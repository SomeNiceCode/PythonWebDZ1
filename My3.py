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

#6

class Book:
    def __init__(self, title, author, pages, book_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_id = book_id

    def display_info(self):
        print(f"название: {self.title}")
        print(f"автор: {self.author}")
        print(f"страниц: {self.pages}")
        print(f"идентификатор: {self.book_id}")
        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"книга '{book.title}' добавлена в библиотеку.")

    def remove_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"книга удалена.")
                return
        print(f"книга не найдена.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"найдено книгу:")
                book.display_info()
                return book
        print(f"книгу не найдено.")
        return None
    
#7

class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_description(self):
        return f"{self.name} ({self.category}) — {self.price:.2f}грывень"

class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"блюдо '{dish.name}' добавлено в заказ.")

    def remove_dish(self, dish_name):
        for dish in self.dishes:
            if dish.name.lower() == dish_name.lower():
                self.dishes.remove(dish)
                print(f"блюдо '{dish.name}' удалено из заказа.")
                return
        print(f"блюдо '{dish_name}' не найдено в заказе.")

    def get_total(self):
        return sum(dish.price for dish in self.dishes)

class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish_to_menu(self, dish):
        self.menu.append(dish)
        print(f"блюдо '{dish.name}' добавлено в меню.")

    def show_menu(self):
        print("меню")
        for dish in self.menu:
            print(f" - {dish.get_description()}")

def main():
    restaurant = Restaurant()
    order = Order()

    # Предустановленные блюда
    restaurant.add_dish_to_menu(Dish("Борщ", 85, "Суп"))
    restaurant.add_dish_to_menu(Dish("Цезарь", 120, "Салат"))
    restaurant.add_dish_to_menu(Dish("Шашлык", 150, "Горячее"))

    while True:
        print("меню:")
        print("1. Показать меню ресторана")
        print("2. Добавить блюдо в заказ")
        print("3. Удалить блюдо из заказа")
        print("4. Показать сумму заказа")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            name = input("введите название блюда для добавления: ")
            found = next((dish for dish in restaurant.menu if dish.name.lower() == name.lower()), None)
            if found:
                order.add_dish(found)
            else:
                print("блюдо не найдено в меню.")

        elif choice == "3":
            name = input("Введите название блюда для удаления: ")
            order.remove_dish(name)

        elif choice == "4":
            total = order.get_total()
            print(f"сумма заказа: {total:.2f}грн")

        elif choice == "5":
            print("спасибо за визит!")
            break

        else:
            print("неверный выбор. Попробуйте снова.")
            
#8

