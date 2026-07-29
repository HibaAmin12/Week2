"""Week 2 Assessment — Bank Toolkit.

Implement every method/function below. Keep every signature exactly as given.
Use logging (not print) wherever a docstring says to log something.
"""
from __future__ import annotations

import asyncio
import json
import logging
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Callable
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S" )
logger = logging.getLogger(__name__)


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would exceed the account balance."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Raise ValueError if balance is negative."""
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner=owner
        self.balance=balance
        

    def deposit(self, amount: float) -> None:
        """Raise ValueError if amount is not positive (zero or negative).
        On success, increase the balance and log an INFO-level message.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        logger.info("Deposited %s into account of %s", amount, self.owner)

    def withdraw(self, amount: float) -> None:
        """If amount exceeds the current balance: log a WARNING-level message
        that mentions the account has insufficient funds, then raise
        InsufficientFundsError. The balance must be unchanged when this
        happens. On success, decrease the balance and log an INFO-level
        message.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number")
        if not isinstance(amount, (int, float)):
            raise notImplementedError("Withdraw amount must be a number")
        if amount > self.balance:
            logger.warning("Account %s has insufficient funds", self.owner)
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        logger.info("Withdrawn %s from account of %s", amount, self.owner)

    def __repr__(self) -> str:
        """Must include the owner and the balance in the string."""
        return f"BankAccount(owner={self.owner},balance={self.balance})"


    def __eq__(self, other: object) -> bool:
        """Two BankAccounts are equal if owner and balance both match."""
    
        return self.owner == other.owner and self.balance == other.balance
    


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
        """Must call the parent's __init__ (via super()) rather than
        reimplementing balance validation — a negative starting balance must
        still be rejected the same way it is for a plain BankAccount.
        """
        def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
            super().__init__(owner, balance)
            self.interest_rate = interest_rate
        

    def apply_interest(self) -> None:
        """balance += balance * interest_rate."""
        self.balance += self.balance * self.interest_rate

        raise NotImplementedError

    def __repr__(self) -> str:
        """Must extend (not fully rewrite) the parent's __repr__ — start from
        super().__repr__() and add the interest rate to it.
        """
        return (
                    f"{super().__repr__()}, "f"interest_rate={self.interest_rate}"
                )


class Bank:
    def __init__(self) -> None:
        self.accounts=[]

    def add_account(self, account: BankAccount) -> None:
        # TODO
        self.accounts.append(account)


    def total_assets(self) -> float:
        """Sum of every held account's balance."""
        return sum(account.balance for account in self.accounts)

    def summary_by_owner(self) -> dict[str, float]:
        """Map each owner name to their total balance across every account
        they hold — an owner may have more than one account.
        """
        summary = defaultdict(float)
        for account in self.accounts:
            summary[account.owner] += account.balance
        return dict(summary)    
    


def save_accounts(path: Path, accounts: list[BankAccount]) -> None:
    """Write accounts as JSON to path (create parent directories if needed).
    Each entry must carry enough information to reconstruct the correct
    class later — include a "type" field ("BankAccount" or "SavingsAccount")
    plus owner/balance/interest_rate as applicable.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for account in accounts:
        if isinstance(account, SavingsAccount):
            data.append(
                {
                    "type": "SavingsAccount",
                    "owner": account.owner,
                    "balance": account.balance,
                    "interest_rate": account.interest_rate,
                }
            )
        else:
            data.append(
                {
                    "type": "BankAccount",
                    "owner": account.owner,
                    "balance": account.balance,
                }
            )
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_accounts(path: Path) -> list[BankAccount]:
    """Read accounts back from JSON at path, reconstructing each as the
    correct class based on its "type" field. If the file doesn't exist, let
    FileNotFoundError propagate — do not swallow it.
    """
    with open(path, "r") as f:
        data = json.load(f)
        accounts=[]
        for item in data:
            if item["type"] == "SavingsAccount":
                accounts.append(SavingsAccount(item["owner"], item["balance"], item["interest_rate"]))
            else:
                accounts.append(BankAccount(item["owner"], item["balance"]))
        return accounts


def count_by_type(accounts: list[BankAccount]) -> Counter:
    """Counter mapping class name to how many accounts of that type are in
    the list.
    """
    counter=Counter(type(account).__name__ for account in accounts)
    return counter


def is_business_hours(dt: datetime) -> bool:
    """True if dt falls on a weekday (Monday-Friday) between 9:00 (inclusive)
    and 17:00 (exclusive) — hour 9 through hour 16 count, hour 17 does not.
    """
    if dt.weekday() < 5:    
        if 9 <= dt.hour < 17:
            return True
    return False    


def apply_interest_to_all(accounts: list[SavingsAccount]) -> None:
    """Apply interest to every account in the list, using a
    ThreadPoolExecutor to do it — the same tool this week's threading kata
    used, applied here for real.
    """
    # TODO
    raise NotImplementedError


def fetch_rates_concurrently(symbols: list[str], fetch_fn: Callable[[str], float]) -> dict[str, float]:
    """For each symbol, call fetch_fn(symbol) to get its rate. Use a
    ThreadPoolExecutor so the calls run concurrently rather than one at a
    time — fetch_fn stands in for a slow network call (this keeps the
    assessment from needing a real network request). If fetch_fn raises for
    a given symbol, log a warning and exclude that symbol from the result —
    one failure must not crash the whole batch.
    """
    # TODO
    raise NotImplementedError


async def apply_interest_async(accounts: list[SavingsAccount]) -> None:
    """For every account: await asyncio.sleep(0.05) to simulate a brief async
    confirmation step, then call apply_interest() on it. Run every account's
    confirmation concurrently using asyncio.gather — not a sequential loop.
    """
    # TODO
    raise NotImplementedError