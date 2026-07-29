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

# Create logger for this module
logger = logging.getLogger(__name__)


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would exceed the account balance."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Raise ValueError if balance is negative."""

        # An account should never start with invalid negative balance
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        # Store account data
        self.owner = owner
        self.balance = balance


    def deposit(self, amount: float) -> None:
        """Raise ValueError if amount is not positive (zero or negative).
        On success, increase the balance and log an INFO-level message.
        """

        # Deposit must always be a positive amount
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
    

        # Update balance
        self.balance += amount

        # Log successful operation
        logger.info("Deposited %s into account of %s", amount, self.owner)


    def withdraw(self, amount: float) -> None:
        """If amount exceeds the current balance: log a WARNING-level message
        that mentions the account has insufficient funds, then raise
        InsufficientFundsError. The balance must be unchanged when this
        happens. On success, decrease the balance and log an INFO-level
        message.
        """
        # # if amount is not positive, raise ValueError
        # if amount <= 0:
        #     raise ValueError("Withdraw amount must be positive")

        # Check funds before changing balance
        if amount > self.balance:

            # Log warning before raising exception
            logger.warning("Account %s has insufficient funds", self.owner)

            raise InsufficientFundsError( "Insufficient funds")

        # Withdraw money after validation
        self.balance -= amount

        # Log successful withdrawal
        logger.info( "Withdrawn %s from account of %s",amount,self.owner)


    def __repr__(self) -> str:
        """Must include the owner and the balance in the string."""

        return (
            f"BankAccount(owner={self.owner},balance={self.balance})"
        )


    def __eq__(self, other: object) -> bool:
        """Two BankAccounts are equal if owner and balance both match."""

        # Ensure comparison is with another BankAccount
        if not isinstance(other, BankAccount):
            return NotImplemented

        return (
            self.owner == other.owner and self.balance == other.balance
        )



class SavingsAccount(BankAccount):

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
        """Must call parent's __init__ using super()."""

        # Parent handles balance validation
        super().__init__(owner, balance)

        # Store savings-specific data
        self.interest_rate = interest_rate


    def apply_interest(self) -> None:
        """balance += balance * interest_rate."""

        # Increase balance according to interest rate
        self.balance += self.balance * self.interest_rate


    def __repr__(self) -> str:
        """Extend parent's repr."""

        # Reuse parent's representation instead of rewriting
        return (
            f"{super().__repr__()}, "f"interest_rate={self.interest_rate}"
        )



class Bank:

    def __init__(self) -> None:

        # Store all accounts managed by bank
        self.accounts = []


    def add_account(self, account: BankAccount) -> None:

        # Add account to bank collection
        self.accounts.append(account)


    def total_assets(self) -> float:
        """Sum of every held account's balance."""

        # Calculate total balance of all accounts
        return sum( account.balance for account in self.accounts)


    def summary_by_owner(self) -> dict[str, float]:
        """Map each owner name to their total balance."""

        # defaultdict automatically creates missing owner entries
        summary = defaultdict(float)

        for account in self.accounts:
            summary[account.owner] += account.balance

        return dict(summary)



def save_accounts( path: Path, accounts: list[BankAccount]) -> None:
    """Write accounts as JSON."""

    # Create parent folders if they do not exist
    path.parent.mkdir( parents=True, exist_ok=True)
    

    data = []

    for account in accounts:

        # Save basic information for SavingsAccount
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
        # Save basic information for BankAccount
            data.append(
                {
                    "type": "BankAccount",
                    "owner": account.owner,
                    "balance": account.balance,
                }
            )


    # Write list of accounts into JSON file
    with path.open("w") as file:
        json.dump(data, file)



def load_accounts(path: Path) -> list[BankAccount]:
    """Load accounts from JSON."""
    # so it propagates as required by specification
    with path.open("r") as file:
        data = json.load(file)


    accounts = []

    for item in data:

        # Recreate correct class using stored type
        if item["type"] == "SavingsAccount":

            accounts.append(
                SavingsAccount(
                    item["owner"],
                    item["balance"],
                    item["interest_rate"]
                )
            )

        else:

            accounts.append(
                BankAccount(
                    item["owner"],
                    item["balance"]
                )
            )

    return accounts



def count_by_type(accounts: list[BankAccount]) -> Counter:
    """Counter mapping class name to count."""

    # Count objects using their actual class name
    return Counter(type(account).__name__ for account in accounts)



def is_business_hours(dt: datetime) -> bool:
    """Monday-Friday 9 inclusive to 17 exclusive."""

    return (
        dt.weekday() < 5 and 9 <= dt.hour < 17
    )


def apply_interest_to_all(accounts: list[SavingsAccount]) -> None:
    """Apply interest using ThreadPoolExecutor."""

    with ThreadPoolExecutor() as executor:
        futures = []

        for account in accounts:
            futures.append(
                executor.submit(account.apply_interest)
            )

        for future in futures:
            future.result()



def fetch_rates_concurrently( symbols: list[str], fetch_fn: Callable[[str], float] ) -> dict[str, float]:

    """Fetch rates concurrently."""

    results = {}


    def fetch(symbol):

        try:
            # Execute external/slow function
            return symbol, fetch_fn(symbol)

        except Exception:

            # One failure should not stop other requests
            logger.warning("Failed to fetch rate for %s", symbol)
            return symbol, None



    with ThreadPoolExecutor() as executor:

        # Submit all symbols together
        futures = [
            executor.submit(fetch, symbol)
            for symbol in symbols
        ]


        for future in futures:

            symbol, rate = future.result()

            # Ignore failed symbols
            if rate is not None:
                results[symbol] = rate


    return results



async def apply_interest_async(  accounts: list[SavingsAccount]) -> None:

    """Apply interest asynchronously using asyncio.gather."""

    async def process(account):

        # Simulate async confirmation step
        await asyncio.sleep(0.05)

        # Perform actual interest calculation
        account.apply_interest()


    # Create all tasks together
    tasks = [
        process(account)
        for account in accounts
    ]


    # Run tasks concurrently
    await asyncio.gather(*tasks)


## fetch_rates_concurrently:
# I used ThreadPoolExecutor to submit multiple fetch_fn calls at the same time.
## Each symbol gets its own future, so slow network-like calls execute concurrently instead of waiting for the previous one to finish.


## apply_interest_async:
## I created a coroutine for each account and collected all coroutines using asyncio.gather().
## This allows all confirmation sleeps to run concurrently before applying interest to each account.