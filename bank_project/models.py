import logging
from dataclasses import dataclass, asdict
from datetime import datetime

logger = logging.getLogger(__name__)


class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds account balance."""
    pass


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    time: str


class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        self.transactions: list[dict] = []

        logger.info(f"Account created for {self.owner}")

    def deposit(self, amount: float) -> None:

        self.balance += amount

        transaction = Transaction(
            transaction_type="Deposit",
            amount=amount,
            time=datetime.now().isoformat()
        )

        self.transactions.append(asdict(transaction))

        logger.info(
            f"${amount} deposited successfully. Balance = {self.balance}"
        )

    def withdraw(self, amount: float) -> None:

        if amount > self.balance:

            logger.warning(
                f"Withdrawal of ${amount} failed."
            )

            raise InsufficientFundsError(
                "Insufficient balance."
            )

        self.balance -= amount

        transaction = Transaction(
            transaction_type="Withdraw",
            amount=amount,
            time=datetime.now().isoformat()
        )

        self.transactions.append(asdict(transaction))

        logger.info(
            f"${amount} withdrawn successfully."
        )

    def check_balance(self) -> float:

        return self.balance


class SavingsAccount(BankAccount):

    def __init__(
        self,
        owner: str,
        balance: float,
        interest_rate: float
    ):

        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def add_interest(self) -> None:

        interest = self.balance * self.interest_rate / 100

        self.deposit(interest)

        logger.info(
            f"Interest Added = {interest}"
        )


class Bank:

    def __init__(self):

        self.accounts: list[BankAccount] = []

    def add_account(
        self,
        account: BankAccount
    ) -> None:

        self.accounts.append(account)

    def total_balance(self) -> float:

        return sum(
            account.balance
            for account in self.accounts
        )