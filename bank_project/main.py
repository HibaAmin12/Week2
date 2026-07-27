import logging
from pathlib import Path

from models import (
    BankAccount,
    SavingsAccount,
    Bank,
    InsufficientFundsError,
)

from utils import (
    save_transactions,
    load_transactions,
    transactions_today,
    count_categories,
    group_amounts,
)

# ---------------- Logging Configuration ----------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("bank.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# ---------------- Main Program ----------------

def main():

    bank = Bank()

    account1 = BankAccount("Hiba", 5000)

    account2 = SavingsAccount("Ali", 10000, 10)

    bank.add_account(account1)

    bank.add_account(account2)

    account1.deposit(1000)

    account2.deposit(500)

    account2.add_interest()

    try:

        account1.withdraw(7000)

    except InsufficientFundsError as e:

        logger.error(e)

    logger.info(f"Current Balance = {account1.check_balance()}")

    logger.info(f"Total Bank Balance = {bank.total_balance()}")

    # ---------------- JSON ----------------

    path = Path("transactions.json")

    save_transactions(path, account1.transactions)

    transactions = load_transactions(path)

    logger.info(f"Transactions Loaded = {transactions}")

    # ---------------- Today's Transactions ----------------

    today = transactions_today(transactions)

    logger.info(f"Today's Transactions = {today}")

    # ---------------- Counter ----------------

    category_count = count_categories(transactions)

    logger.info(f"Category Count = {category_count}")

    # ---------------- defaultdict ----------------

    grouped = group_amounts(transactions)

    logger.info(f"Grouped Amounts = {dict(grouped)}")

    # ---------------- Type Hint Demo ----------------

    try:

        account1.deposit("fifty")

    except Exception as e:

        logger.error(
            f"Type hints are not enforced by Python: {e}"
        )


if __name__ == "__main__":

    main()