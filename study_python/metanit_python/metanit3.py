# Классы и объекты

import abc

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Количество страниц: {self.pages}.")

book1 = Book("Voina i mir", 'Bulgakov', 500)
book2 = Book("1960", 'Lermontov', 121)

book1.get_info()
book2.get_info()

class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(area)

    def perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        print(perimeter)

rec1 = Rectangle(1, 2)
rec2 = Rectangle()
rec1.area()
rec2.area()
rec1.perimeter()
rec2.perimeter()

class BankAccount:
    def __init__(self, balance, id):
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_info(self):
        print(f"У человека с id {self.id} баланс счета равен {self.balance}")

    def __del__(self):
        print(f"Объект {self.id} удален")

person1 = BankAccount(100, 1)
person2 = BankAccount(200, 2)
person1.deposit(100)
person2.deposit(200)
person1.withdraw(10)
person2.withdraw(121)
person1.get_info()
person2.get_info()

# Инкапсуляция, атрибуты и свойства

class User:
    def __init__(self, password):
        self.__password = password # переменная будет доступна только внутри класса, но это условная приватность, вне класса можем получить доступ если напишем полный путь к
        # переменной вида user1._User__password = ...

    def check_password(self, password_try):
        if password_try == self.__password:
            print("Совпадают")
        else:
            print("неверный пароль")

user1 = User(12)
user1.check_password(112)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            return

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_info(self):
        print(f"Имя: {self.__name}, возраст: {self.__age}")

person1 = Person("Abnoba", 18)
person2 = Person('Asdasd', 12)
person1.set_age(100)
person2.set_age(-100)
person1.get_info()
person2.get_info()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            return

    @property
    def name(self):
        return self.__name

    def get_info(self):
        print(f"{self.__age}, {self.__name}")

person3 = Person("Asdasd", 18)
person4 = Person("Abnobaasd", 112)
person3.age = 120
person3.get_info()

class Product:
    def __init__(self, price, discount = 0):
        self.__price = price
        self.__discount = discount

    @property
    def final_price(self):
        return self.__price - self.__price * self.__discount / 100

product1 = Product(120, 10)
print(product1.final_price)

# Наследование

class Animal:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def breath(self):
        print(f"{self.__name} дышит")

class Dog(Animal):
    def bark(self):
        print(f"Собака {self.name} рычит")

dog1 = Dog("bba")
dog1.breath()
dog1.bark()

class Vehicle:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

class Car(Vehicle):
    def drive(self):
        print(f"Машина {self.brand} едет")

car1 = Car("Ford")
car1.drive()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        print(f"Имя человека: {self.__name}, возраст: {self.__age}")

class Employee(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.__experience = experience

    @property
    def name(self):
        return self.__name

    def work_experience(self):
        print(f"Опыт работы работника: {self.__experience}")

class Manager(Employee):
    def __init__(self, name, age, experience, id):
        super().__init__(experience, name, age)
        self.__id = id

    def print_id(self):
        print(f"ID: {self.__id}")

manager = Manager("Aboba", 12, 18, 1)
manager.print_id()
manager.work_experience()
manager.get_info()

class Camera:
    def __init__(self, brand):
        self.brand = brand

    def take_photo(self):
        print("Сделано фото")

class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print("Позвонили по телефону")

class Smartphone(Phone, Camera):
    def __init__(self, brand):
        super().__init__(brand)

smartphone = Smartphone("Samsung")
smartphone.take_photo()
smartphone.call()

def filter_employees(items):
    for item in items:
        if isinstance(item, Employee):
            print(item)
filter_employees([manager, smartphone])

# Переопределение функционала базового класса

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Птица летит")

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Пингвин не летает")

peng = Penguin("Penguin")
peng.fly()

class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def get_info(self):
        super().get_info()
        print(f"{self.university}")

student = Student("Bob", "MISIS")
student.get_info()

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def calculate_pay(self):
        return self.__salary

class SalesPerson(Employee):
    def __init__(self, salary, sales):
        super().__init__(salary)
        self.sales = sales

    def calculate_pay(self):
        return super().calculate_pay() + self.sales * 0.1

emp = SalesPerson(120, 10)
print(emp.calculate_pay())

class Logger:
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        print("[INFO]")
        super().log(msg)

timestamp = TimestampLogger()
timestamp.log("log1 : sas")

# Атрибуты классов и статические методы

class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

car = Car("Aboba")
print(car.wheels)
print(Car.wheels)

class Counter:
    count = 0
    def __init__(self, name):
        self.name = name
        Counter.count += 1

counter = Counter("aboba")
print(Counter.count)
counter2 = Counter("adsd")
print(Counter.count)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 2222))

class BankDeposit:
    interest_rate = 0.08
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self, years):
        return self.amount * ((1 + BankDeposit.interest_rate) ** years)

bank = BankDeposit(10)
print(bank.calculate_total(20))

# Класс object. Строковое представление объекта

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(Точка({self.x}, {self.y}))"

point = Point(10, 20)
print(point)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person('<{self.name}>, <{self.age}>')"

person = Person("Aboba", 10)
person2 = Person("Bob", 20)
people = [person, person2]
print(people[0])
print(people)

# Перегрузка операторов

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}, {self.y}"

vector1 = Vector(1, 2)
vector2 = Vector(2, 3)
print(vector1 + vector2)

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __eq__(self, other):
        return self.volume == other.volume

    def __lt__(self, other):
        return self.volume < other.volume

box1 = Box(1)
box2 = Box(2)
print(box1 == box2)
print(box1 < box2)

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __bool__(self):
        return self.amount > 0


def test(wallet):
    if wallet: print("Counter = True")
    else: print("Counter = False")

wallet = Wallet(-10)
test(wallet)

class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, Counter):
            self.value += other.value
        else:
            self.value += other
        return self

    def __str__(self):
        return f"{self.value}"

counter1 = Counter(10)
counter2 = Counter(20)
counter3 = 10
counter1 += counter2
counter1 += counter3
print(counter1)

class Team:
    def __init__(self, members):
        self.members = members

    def __getitem__(self, index):
        return self.members[index]

    def __contains__(self, item):
        return item in self.members

team1 = Team([1, 2, 3])
team2 = Team([4, 5, 6])
print(team1[2])
for member in team1:
    print(member)
for member in team2:
    print(member)

# Абстрактные классы и методыъ

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"Площадь фигуры: {self.area()}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * 3.14 * self.radius

square = Square(21)
circle = Circle(3)
print(square.area())
print(circle.area())
circle.describe()