class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class SavingsAccount(BankAccount):
    pass


acc = SavingsAccount("Hiba", 5000)

print(acc.owner)
print(acc.balance)

acc.deposit(1000)

print(acc.balance)


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"
        
class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
        print(f"Child cLass")
student = Student("Hiba", 24, 101)

print(student.name)
print(student.age)
print(student.roll_no)
print(student.introduce())

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def details(self):
        return f"Brand:{self.brand}, Model:{self.model}"
class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type=fuel_type
car = Car("Toyota", "Corolla", "Petrol")

print(car.brand)
print(car.model)
print(car.fuel_type)
print(car.details())

#METHOD OVERRIDING
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Animal makes a sound"
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return " Dog Barks"

animal = Animal("Unknown")
dog = Dog("Tommy")

print(animal.speak())
print(dog.speak())

#Method Extension
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def info(self):
        return f"Name:{self.name},Salary:{self.salary},"
class Manager(Employee):
    def __init__(self, name, salary,dep):
        super().__init__(name, salary)
        self.dep=dep
    def info(self):
        return super().info()+ f"Department:{self.dep}"
manager = Manager("Hiba", 100000, "AI")

print(manager.info())


class Shape:

    def area(self):
        return "Area not defined"


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    print(shape.area())

class Bird:
    def __init__(self):
        pass
    def fly(self):
        return "Birds Fly"
class Sparrow(Bird):
    def __init__(self):
        super().__init__()
    def fly(self):
        return "Sparrows Fly high"
class Penguin(Bird):
    def __init__(self):
        super().__init__()
    def fly(self):
        return "Penguin cannot fly"

birds = [
    Sparrow(),
    Penguin()
]
for bird in birds:
    print(bird.fly())

class Payment:

    def pay(self, amount):
        return f"Processing payment of {amount}"


class CreditCard(Payment):

    def pay(self, amount):
        return f"Paid {amount} using Credit Card"


class JazzCash(Payment):

    def pay(self, amount):
        return f"Paid {amount} using JazzCash"


class BankTransfer(Payment):

    def pay(self, amount):
        return f"Paid {amount} using Bank Transfer"


payments = [
    CreditCard(),
    JazzCash(),
    BankTransfer()
]

for payment in payments:
    print(payment.pay(5000))
#COMPOSITION
class Battery:
    def charge(self):
        return " Battery Charging......."

class Mobile:
    def __init__(self):
        self.battery = Battery()
mobile = Mobile()

print(mobile.battery.charge())

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

    def __eq__(self, value):
        if not isinstance(value, BankAccount):
            return False
        return (
            self.owner == value.owner and
            self.balance == value.balance
        )

    def summary(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __repr__(self):
        return super().__repr__() + f", Interest Rate: {self.interest_rate}"

    def summary(self):
        return super().summary() + f", Interest Rate: {self.interest_rate}"


# Polymorphism Function
def print_all(accounts):
    for account in accounts:
        print(account.summary())


# Composition
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_assets(self):
        total = 0

        for account in self.accounts:
            total += account.balance

        return total


# Testing
acc1 = BankAccount("Hiba", 5000)
acc2 = BankAccount("Hiba", 5000)
acc3 = SavingsAccount("Ali", 10000, "5%")

print(acc1)
print(acc3)

print(acc1 == acc2)

print(acc1.summary())
print(acc3.summary())

accounts = [
    acc1,
    acc3,
    BankAccount("Sara", 7000)
]

print("\nAll Accounts:")
print_all(accounts)


# Composition Testing
bank = Bank()

bank.add_account(acc1)
bank.add_account(acc3)

print("\nTotal Assets:")
print(bank.total_assets())