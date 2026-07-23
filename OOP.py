class Student():
    def __init__(self,name):
        self.name=name
        print(name)
s1=Student("Hiba")
s2=Student("Ali")

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __repr__(self):
        return f"BankAccount({self.owner},{self.balance})"
    def __eq__(self, other):
        self.owner==other.owner 
        self.balance== other.balance

account=BankAccount("Hiba",50000)
print(account)

class Student:
    def __init__(self, name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def introduce(self):
        print(f"My name is {self.name} and my Roll No is {self.roll_no}.")

s1=Student("Hiba",23)
s1.introduce()
    
class Student:
    def __init__(self, name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def __repr__(self):
        return f"Student({self.name},{self.roll_no})"

s1=Student("Hiba",23)
print(s1)

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __repr__(self):
        return f"Student(name='{self.name}', roll_no={self.roll_no})"

    def __eq__(self, other):
        return self.name == other.name and self.roll_no == other.roll_no

s1 = Student("Hiba", 23)
s2 = Student("Hiba", 23)
s3 = Student("Ali", 24)

print(s1 == s2)
print(s1 == s3)

class Student:
    pass

s1 = Student()

print(isinstance(s1, Student))

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __repr__(self):
        return f"name={self.name},salary={self.salary}"
    def __eq__(self, other):
        if not isinstance(other,Employee):
            return False
        if self.name==other.name and self.salary==other.salary:
            return True
        else:
            return False

e1 = Employee("Hiba", 50000)
e2 = Employee("Hiba", 50000)
e3 = Employee("Ali", 60000)

print(e1 == e2)      # True
print(e1 == e3)      # False
print(e1 == 50000)   # False
print(e1 == "Hiba")  # False

class Employee:

    def __repr__(self):
        return "Employee(name='Hiba', salary=50000)"

    def __str__(self):
        return "Hiba earns Rs.50000"

e = Employee()

# print(e)
print(repr(e))

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __repr__(self):
        return f"Book(title='{self.title}',author='{self.author}')"
    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python", "Hiba")

print(b)

print(repr(b))

print(str(b))


class Student:
    def __init__(self):
        self.name = "Hiba"
        self._city = "Lahore"
        self.__age = 24

s = Student()

print(s.name)
print(s._city)
print(s._Student__age)
# print(s.__age)

print(vars(s))


class BankAccount:
    def __init__(self):
        self.__balance = 1000

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.__balance = 5000

s = SavingsAccount()

print(vars(s))


#MANUAL CLASS
class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative") # dataclass canot generated it bczits a progammer deision and choice

        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False

        return (
            self.owner == other.owner and
            self.balance == other.balance
        )

#DATACLASS
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"Student(name='{self.name}',age={self.age})"
    def __str__(self):
        return f"{self.name } is {self.age} years old"
s=Student("Hiba",24)
print(s)
print(repr(s))

class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __eq__(self, other):
        if not isinstance(other, Laptop):
            return False
        return (
        self.brand == other.brand and
        self.price == other.price
    )

l1 = Laptop("Dell", 120000)
l2 = Laptop("Dell", 120000)
l3 = Laptop("HP", 120000)

print(l1 == l2)
print(l1 == l3)
print(l1 == 120000)        


class Employee:
    def __init__(self,name,salary):
        if salary<0:
            raise ValueError("Salary cannot be negative")
        self.name=name
        self.salary=salary
    def __repr__(self):
        return f"Employee(name='{self.name}',salary={self.salary})"

e1 = Employee("Hiba", 50000)
print(e1)

e2 = Employee("Ali", -1000)

class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    def drive(self,speed):
        self.speed=speed
        print(f"{self.brand} {self.model} is driving at {self.speed} km/h")
c = Car("Toyota", "Corolla")

c.drive(80)

Car.drive(c, 120)

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass


class BankAccount:
    def __init__(self, owner, balance):
        # Validation
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient balance")

        self.__balance -= amount

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False

        return (
            self.owner == other.owner
            and self.__balance == other.__balance
        )


# Objects
a1 = BankAccount("Hiba", 1000)
a2 = BankAccount("Hiba", 1000)

print(a1 == a2)          # True

a1.deposit(500)

a1.withdraw(200)

print(a1)

print(vars(a1))
a3 = BankAccount("Ali", 500)

a3.withdraw(1000)

class Animal:
    def __init__(self):
        self.__name = "Animal"


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.__name = "Dog"


d = Dog()

print(vars(d))