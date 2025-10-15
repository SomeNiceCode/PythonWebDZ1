#1

class Engine:
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving at maximum speed of {self.max_speed}")


class Car(Engine, Vehicle):
    def __init__(self, model, max_speed):
        Vehicle.__init__(self, max_speed)
        self.model = model

    def drive(self):
        print(f"Car {self.model} is driving at {self.max_speed}")


class Boat(Engine, Vehicle):
    def __init__(self, boat_type, max_speed):
        Vehicle.__init__(self, max_speed)
        self.type = boat_type

    def drive(self):
        print(f"Boat of type {self.type} is sailing at {self.max_speed}")


class AmphibiousVehicle(Car, Boat):
    def __init__(self, model, boat_type, max_speed, is_on_land=True):
        Car.__init__(self, model, max_speed)
        Boat.__init__(self, boat_type, max_speed)
        self.is_on_land = is_on_land

    def drive(self):
        if self.is_on_land:
            print(f"Car {self.model} is driving at {self.max_speed}")
        else:
            print(f"Boat of type {self.type} is sailing at {self.max_speed}")

#2

class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    def __str__(self):
        return f'"{self.title}" by {self.author}, {self.pages} pages'

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __iadd__(self, book):
        self.add_book(book)
        return self

    def __isub__(self, book):
        self.remove_book(book)
        return self

    def __contains__(self, book):
        return book in self.books

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return "\n".join(str(book) for book in self.books)
    



#3

class cache_result:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in self.cache:
            print("Returning cached result")
            return self.cache[key]
        result = self.func(*args, **kwargs)
        self.cache[key] = result
        return result

