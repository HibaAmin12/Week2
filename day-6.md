# Week 02 · Day1 · Learn
## OOP Foundations — Classes, `self`, and Magic Methods by Hand

### Learning objectives
By the end of today, you should be able to:
- Write `__init__`, `__repr__`, and `__eq__` by hand for a class, and explain exactly what `@dataclass` was generating for you last week.
- Explain what `self` actually is, mechanically — not just "the instance," but how `instance.method()` becomes `Class.method(instance)` underneath.
- Use single- and double-underscore naming to signal encapsulation, and explain why Python treats both as a convention, not an enforced lock.
- Name two places you already used an OOP mechanism last week, before this lesson ever gave it a name.

### Lesson

**1. Cashing in last week's IOU: what `@dataclass` actually generated**
Thursday's lesson told you plainly that `@dataclass` generates `__init__`, `__repr__`, and `__eq__` for you, and promised the vocabulary for that was coming "next week." Here it is: those three are **magic methods** (also called dunder methods, from "double underscore") — special methods Python calls automatically in response to specific operations, not something you call directly yourself. `@dataclass` writes them for you *as long as your class is just a bag of fields*. The moment a class needs real behavior — validation in the constructor, custom equality logic, anything beyond "assign these fields and move on" — you write these by hand instead. That's exactly what today's kata does.

**2. `self`, mechanically, not mystically**
When you write `account.deposit(50)`, Python translates that into `BankAccount.deposit(account, 50)` — the instance you called it through gets silently passed in as the first argument. `self` is not a keyword; it's a naming convention for that first parameter (you could technically call it anything — but never do; this is the one convention every Python codebase you'll ever read actually follows). Worth proving to yourself directly rather than just accepting it: today's kata has you call the same method both ways and confirm they're identical.

**3. The three magic methods you'll write today**
- `__init__` — runs right after the (mostly invisible) real constructor, `__new__`, and is where you validate and assign. Unlike a dataclass's generated version, *your* `__init__` can refuse bad input outright.
- `__repr__` — an unambiguous, debugging-facing representation of the object; what you see printed in a REPL or a debugger. Write one on every class you make, out of habit.
- `__str__` — a human-readable representation, used by `print()` and `str()`. Skip it and Python falls back to `__repr__` automatically.
- `__eq__` — defines what `==` actually compares. Without it, `==` falls back to *identity* comparison (the same thing `is` does) — whether two variables point at the literal same object in memory — which is almost never what you want for two accounts that simply happen to hold the same owner and balance.

**4. Encapsulation is a convention, not a lock**
`_balance` (single leading underscore) signals "internal, don't touch this from outside" — a convention, not an enforcement; Python does nothing to stop you from reaching in anyway. `__balance` (double leading underscore) triggers **name mangling**: Python silently renames it to `_ClassName__balance` internally, specifically to avoid accidental naming collisions in subclasses — not to make it "private." Python has no true private attributes, and treating double-underscore as real security is a common, incorrect assumption worth correcting directly. This is the same "Python reads this convention, it doesn't enforce a rule" idea behind last week's `if __name__ == "__main__":` guard.

**5. You've already done this, twice, without the vocabulary**
Tuesday's `class InsufficientFundsError(Exception):` is inheritance — you subclassed `Exception` to get all of its raise/except machinery for free, and only added a docstring on top. And if your Tuesday context-manager kata was written as a class (rather than with `@contextmanager`), `__enter__`/`__exit__` are themselves magic methods — the exact category of thing this lesson is about. You were doing object-oriented programming all last week; today just gives it a name.

### Resources
- [Real Python — Python Classes: The Power of Object-Oriented Programming](https://realpython.com/python-classes/)
- [Real Python — Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Real Python — Python's Magic Methods: Leverage Their Power in Your Classes](https://realpython.com/python-magic-methods/)
- [Real Python — When Should You Use `.__repr__()` vs `.__str__()` in Python?](https://realpython.com/python-repr-vs-str/)

### Kata set
1. **Hand-write `BankAccount`.** A class with `owner` and `balance`. `__init__` must reject a negative starting balance (a plain `ValueError` is fine here — you'll wire in a real custom exception in Kata 3). Write `__repr__` and `__eq__` by hand — no `@dataclass` this time.
2. **Prove `self` is just a parameter.** Call one of `BankAccount`'s methods two ways: `account.deposit(50)` and `BankAccount.deposit(account, 50)`. Confirm they do the exact same thing.
3. **Reuse Tuesday's exception.** Add a `withdraw(amount)` method that raises last week's `InsufficientFundsError` — not a generic exception — when `amount` exceeds the balance.
4. **Name-mangling demo.** Rename `balance` to `__balance` (double underscore) inside `BankAccount`, subclass it as `SavingsAccount` which also sets its own `self.__balance`, and print `vars(instance)` on a `SavingsAccount` object to see both mangled names coexist without colliding. Explain in one sentence why that's useful, and why it still isn't "privacy."
5. **Compare to a dataclass.** Sketch what `BankAccount` would look like as a `@dataclass`, and name the one specific line of your hand-written version a dataclass could not have generated for you.

### Today's tasks
- [ ] `BankAccount` class written by hand with `__init__`, `__repr__`, `__eq__`
- [ ] Same method called both instance-style and class-style, confirmed identical
- [ ] `withdraw` raises `InsufficientFundsError` from last week, not a generic exception
- [ ] Name-mangling demo done, `vars()` output explained
- [ ] Dataclass-comparison kata done — one specific line named that a dataclass couldn't generate


