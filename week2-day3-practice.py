def add(a: int, b: int) -> int:
    return a + b

add(10, 20)

# LOGGING
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Program Started")
#WITHOUT LOGGING
def deposit(balance, amount):
    print("Deposit Started")

    balance += amount

    print("Deposit Successful")

    return balance


balance = 1000

balance = deposit(balance, 500)

# WITH LOGGING
import logging

logging.basicConfig(level=logging.INFO)

def deposit(balance, amount):
    logging.info("Deposit Started")
    balance += amount
    logging.info("Deposit Successful")
    return balance

balance = 1000
balance = deposit(balance, 500)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Program Started")
logger.info("User Logged In")
logger.info("Program Ended")

import logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
def deposit(balance, amount):
    logger.info("Deposit Started")
    balance += amount
    logger.info("Deposit Successful")
    return balance
def withdraw(balance, amount):
    logger.info("Withdraw Started")
    if balance >= amount:
        balance -= amount
        logger.info("Withdraw Successful")
    if balance < amount:
        try:
            raise ValueError("Insufficient Balance")
        except ValueError as e:
            logger.error(e)
    return balance
balance = 1000
balance = deposit(balance, 500)
balance = withdraw(balance, 2000)
import logging


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bank_account.log"),
        logging.StreamHandler()
    ],
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# Custom Exception
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    pass


class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        logger.info(f"Account created for {self.owner} with balance {self.balance}")

    def deposit(self, amount: float) -> None:
        logger.info(f"Deposit started: {amount}")

        self.balance += amount

        logger.info(
            f"Deposited {amount}. Current balance: {self.balance}"
        )

    def withdraw(self, amount: float) -> None:
        logger.info(f"Withdrawal requested: {amount}")

        if self.balance >= amount:
            self.balance -= amount
            logger.info(
                f"Withdrawal successful. Current balance: {self.balance}"
            )

        else:
            logger.warning(
                f"Withdrawal failed. Available balance: {self.balance}"
            )

            raise InsufficientFundsError(
                "Insufficient balance."
            )

    def check_balance(self) -> float:
        logger.info(f"Balance checked: {self.balance}")
        return self.balance


# Main Program
account = BankAccount("Hiba", 5000)

account.deposit(1000)

try:
    account.withdraw(8000)

except InsufficientFundsError as e:
    logger.error(e)

print("Current Balance:", account.check_balance())

from pathlib import Path
folder=Path("data").mkdir(exist_ok=True)
folder1=Path("data/reports").mkdir(exist_ok=True)
path=Path("data/reports/report.txt").write_text("Hello Hiba")
output=path.read_text()


from datetime import datetime
now=datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)

from datetime import datetime, timedelta

today = datetime.now()

last_week = today - timedelta(days=7)
next_week = today + timedelta(days=7)
one_day = today+ timedelta(days=1)
one_week = today + timedelta(weeks=2)
print(today.strftime("%d-%m-%Y"))
print(last_week)
print(next_week)
print(one_day)
print(one_week)

from collections import Counter

text = "banana"

print(Counter(text))

