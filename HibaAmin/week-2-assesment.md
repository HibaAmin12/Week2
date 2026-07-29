# Week 02 · Assessment — Build the Bank Toolkit

**Format:** implement a fixed spec against a starter file. A few sample tests are included so you can check your own work — but grading uses a larger, hidden test suite you will not see. Passing the sample tests is necessary, not sufficient.

## Setup

Create a package folder named `bank_toolkit/` containing an empty `__init__.py` and the starter file below saved as `bank_toolkit/bank_toolkit.py`. Save the sample test file next to the package as `test_bank_toolkit_sample.py`.

**`bank_toolkit/bank_toolkit.py`** — implement every function/method marked `# TODO`. **Do not change any function or class signature** — the hidden tests call these exact names with these exact arguments.

```python
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

logger = logging.getLogger(__name__)


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would exceed the account balance."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Raise ValueError if balance is negative."""
        # TODO
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        """Raise ValueError if amount is not positive (zero or negative).
        On success, increase the balance and log an INFO-level message.
        """
        # TODO
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        """If amount exceeds the current balance: log a WARNING-level message
        that mentions the account has insufficient funds, then raise
        InsufficientFundsError. The balance must be unchanged when this
        happens. On success, decrease the balance and log an INFO-level
        message.
        """
        # TODO
        raise NotImplementedError

    def __repr__(self) -> str:
        """Must include the owner and the balance in the string."""
        # TODO
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Two BankAccounts are equal if owner and balance both match."""
        # TODO
        raise NotImplementedError


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
        """Must call the parent's __init__ (via super()) rather than
        reimplementing balance validation — a negative starting balance must
        still be rejected the same way it is for a plain BankAccount.
        """
        # TODO
        raise NotImplementedError

    def apply_interest(self) -> None:
        """balance += balance * interest_rate."""
        # TODO
        raise NotImplementedError

    def __repr__(self) -> str:
        """Must extend (not fully rewrite) the parent's __repr__ — start from
        super().__repr__() and add the interest rate to it.
        """
        # TODO
        raise NotImplementedError


class Bank:
    def __init__(self) -> None:
        # TODO
        raise NotImplementedError

    def add_account(self, account: BankAccount) -> None:
        # TODO
        raise NotImplementedError

    def total_assets(self) -> float:
        """Sum of every held account's balance."""
        # TODO
        raise NotImplementedError

    def summary_by_owner(self) -> dict[str, float]:
        """Map each owner name to their total balance across every account
        they hold — an owner may have more than one account.
        """
        # TODO
        raise NotImplementedError


def save_accounts(path: Path, accounts: list[BankAccount]) -> None:
    """Write accounts as JSON to path (create parent directories if needed).
    Each entry must carry enough information to reconstruct the correct
    class later — include a "type" field ("BankAccount" or "SavingsAccount")
    plus owner/balance/interest_rate as applicable.
    """
    # TODO
    raise NotImplementedError


def load_accounts(path: Path) -> list[BankAccount]:
    """Read accounts back from JSON at path, reconstructing each as the
    correct class based on its "type" field. If the file doesn't exist, let
    FileNotFoundError propagate — do not swallow it.
    """
    # TODO
    raise NotImplementedError


def count_by_type(accounts: list[BankAccount]) -> Counter:
    """Counter mapping class name to how many accounts of that type are in
    the list.
    """
    # TODO
    raise NotImplementedError


def is_business_hours(dt: datetime) -> bool:
    """True if dt falls on a weekday (Monday-Friday) between 9:00 (inclusive)
    and 17:00 (exclusive) — hour 9 through hour 16 count, hour 17 does not.
    """
    # TODO
    raise NotImplementedError


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
```

**`test_bank_toolkit_sample.py`** — a few sample checks so you know the expected shape. These are not the full grading suite.

```python
from datetime import datetime

import pytest

from bank_toolkit.bank_toolkit import (
    Bank,
    BankAccount,
    InsufficientFundsError,
    SavingsAccount,
    is_business_hours,
)


def test_deposit_happy():
    a = BankAccount("Alice", 100.0)
    a.deposit(50.0)
    assert a.balance == 150.0


def test_withdraw_insufficient_funds_raises():
    a = BankAccount("Alice", 50.0)
    with pytest.raises(InsufficientFundsError):
        a.withdraw(100.0)


def test_savingsaccount_apply_interest():
    s = SavingsAccount("Alice", 100.0, interest_rate=0.1)
    s.apply_interest()
    assert s.balance == pytest.approx(110.0)


def test_bank_total_assets():
    bank = Bank()
    bank.add_account(BankAccount("Alice", 100.0))
    bank.add_account(BankAccount("Bob", 50.0))
    assert bank.total_assets() == 150.0


def test_is_business_hours_weekday_daytime():
    assert is_business_hours(datetime(2026, 7, 22, 10, 0)) is True
```

## The task

Your goal: a fully implemented `bank_toolkit.py` that passes the sample tests above **and** a hidden test suite covering the rest of the spec — including edge cases and error cases the sample tests don't show you.

**1. Implement everything.** Fill in every `# TODO`. Run `pytest test_bank_toolkit_sample.py` until all sample tests pass.

**2. Read every docstring as a contract, not a suggestion.** Several behaviors — the exact business-hours boundary, what happens when `fetch_rates_concurrently` gets a failing symbol, what `load_accounts` should do when the file is missing — are specified in the docstrings above and will be checked by hidden tests you can't see. If a docstring says something specific, implement exactly that, not your own reasonable-sounding alternative.

**3. Prove the concurrency parts are actually concurrent.** `apply_interest_to_all`, `fetch_rates_concurrently`, and `apply_interest_async` all ask for a specific concurrency tool by name. Using a plain sequential loop instead will often still produce the *correct final values* — the hidden tests time these functions, so a sequential version that happens to compute the right answer will still fail on speed.

**4. Package it properly.** `bank_toolkit/` should be a real package (non-empty `__init__.py` is fine if you want to re-export names, but it must at minimum make `from bank_toolkit.bank_toolkit import ...` work).

**5. Write down your reasoning for the two concurrency functions.** For `fetch_rates_concurrently` and `apply_interest_async`: 1-2 sentences each on how you made them actually run concurrently, not just correctly.

## Submission

Bring: the completed `bank_toolkit/` package, and your written notes on the two concurrency functions.
