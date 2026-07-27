import json
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict


def save_transactions(path: Path, transactions: list) -> None:
    """
    Save transactions to a JSON file.
    """

    with path.open("w") as file:
        json.dump(transactions, file, indent=4)


def load_transactions(path: Path) -> list:
    """
    Load transactions from a JSON file.
    """

    if not path.exists():
        return []

    with path.open("r") as file:
        return json.load(file)


def transactions_today(transactions: list) -> list:
    """
    Return only today's transactions.
    """

    today = datetime.now().date()

    result = []

    for transaction in transactions:

        transaction_date = datetime.fromisoformat(
            transaction["time"]
        ).date()

        if transaction_date == today:
            result.append(transaction)

    return result


def count_categories(transactions: list) -> Counter:
    """
    Count number of transactions in each category.
    """

    categories = [
        transaction["transaction_type"]
        for transaction in transactions
    ]

    return Counter(categories)


def group_amounts(transactions: list) -> defaultdict:
    """
    Group transaction amounts by category.
    """

    grouped = defaultdict(list)

    for transaction in transactions:

        grouped[
            transaction["transaction_type"]
        ].append(transaction["amount"])

    return grouped