from models import BankAccount


def test_deposit():

    account = BankAccount("Ali", 1000)

    account.deposit(500)

    assert account.balance == 1500


def test_withdraw():

    account = BankAccount("Ali", 1000)

    account.withdraw(500)

    assert account.balance == 500