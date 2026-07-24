# Bank management system
# class InsufficientFundsError(Exception):
#     pass
#     """Raised when withdrawal exceeds balance."""


# class BankAccount:

#     bank_name = "CMIT Bank"

#     def __init__(self, owner, balance):
#         if balance < 0:
#                     raise ValueError("Balance cannot be negative")
        

#         self.owner = owner
#         self.__balance = balance


#     def deposit(self, amount):

#         self.__balance += amount

#     def withdraw(self, amount):

#         if amount > self.__balance:
#             raise InsufficientFundsError("Insufficient balance")

#         self.__balance -= amount

#     def transfer(self, other, amount):

#         self.withdraw(amount)

#         other.deposit(amount)

#     def get_balance(self):

#         return self.__balance

#     def __repr__(self):

#         return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

#     def __str__(self):

#         return self.owner

#     def __eq__(self, other):

#         if not isinstance(other, BankAccount):
#             return False

#         return (
#             self.owner == other.owner and
#             self.__balance == other.__balance
#         )


# class SavingsAccount(BankAccount):

#     def __init__(self, owner, balance):

#         super().__init__(owner, balance)

#         self.__balance = 500

#     def add_interest(self, rate):
#         interest = self._BankAccount__balance * rate / 100
#         self._BankAccount__balance += interest
#         return interest


# class CurrentAccount(BankAccount):

#     def monthly_fee(self):

#         self._BankAccount__balance -= 100


# class Customer:

#     def __init__(self, name):

#         self.name = name

#         self.accounts = []

#     def add_account(self, account):
#         self.accounts.append(account)

#     def show_accounts(self):

#         for account in self.accounts:

#             print(account)


# a1 = BankAccount("Hiba", 1000)

# a2 = BankAccount("Hiba", 1000)

# a3 = BankAccount("Ali", 500)

# print(a1 == a2)

# print(a1 is a2)

# a1.deposit(500)

# print(a1)

# BankAccount.deposit(a1, 100)

# print(a1)

# a1.withdraw(200)

# print(a1)

# a1.transfer(a3, 300)

# print(a1)

# print(a3)

# print(a1.get_balance())

# print(vars(a1))

# s = SavingsAccount("Sara", 2000)

# print(vars(s))

# s.add_interest(5)

# print(vars(s))

# c = CurrentAccount("Usman", 5000)

# c.monthly_fee()

# print(vars(c))

# customer = Customer("Hiba")

# customer.add_account(a1)

# customer.add_account(a3)

# customer.show_accounts()

# print(isinstance(customer, BankAccount))

# print(isinstance(a1, BankAccount))

# print(isinstance(s, BankAccount))

# print(isinstance(1000, BankAccount))

# print(BankAccount.bank_name)

# print(repr(a1))

# print(str(a1))

#Product Management
# class Product:

#     def __init__(self, name, price):

#         if price < 0:
#             raise ValueError("Price cannot be negative")

#         self.name = name
#         self.price = price

#     def discount(self, percent):

#         if percent < 0 or percent > 100:
#             raise ValueError("Invalid discount percentage")

#         self.price -= self.price * percent / 100

#     def __repr__(self):

#         return f"Product(name='{self.name}', price={self.price})"

#     def __eq__(self, other):

#         if not isinstance(other, Product):
#             return False

#         return (
#             self.name == other.name and
#             self.price == other.price
#         )


# p1 = Product("Laptop", 100000)
# p2 = Product("Laptop", 100000)

# print(p1 == p2)

# p1.discount(10)

# print(p1)

# Product.discount(p1, 5)

# print(p1)

# print(vars(p1))

# print(p1 == 100000)



