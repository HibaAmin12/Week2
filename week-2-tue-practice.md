# Week 02 · Tue · Practice
## Inheritance, `super()`, Polymorphism & Composition

### Learning objectives
By the end of today, you should be able to:
- Build a subclass that reuses a parent's `__init__` via `super()` instead of re-writing its field assignment.
- Explain the difference between *overriding* a method entirely and *extending* it (calling `super()`, then adding to it).
- Explain polymorphism as "the same method name behaves differently depending on the actual object" — without an `isinstance`/`type()` check chain anywhere.
- Choose composition ("has-a") over inheritance ("is-a") for a relationship where composition is the correct fit, and justify why in one sentence.

### Practice framing
Monday built one class, by hand, in isolation. Today is about relationships *between* classes: reusing what a parent already got right instead of copy-pasting it into every subclass, recognizing that the same method name can behave differently depending on which object it's called on, and knowing when a new class should inherit from an existing one versus simply *hold* one as a field.

**Kata set** (work through in order):

1. **Warm-up — recreate `BankAccount` from memory.** No notes: `__init__`, `__repr__`, `__eq__`. If this takes more than a couple of minutes, re-read Monday's lesson before continuing — everything today builds on top of it.

2. **Inherit with `super()`.** Build `SavingsAccount(BankAccount)` that adds an `interest_rate`. Its `__init__` must call `super().__init__(owner, balance)` to set up the parent's fields, then set `self.interest_rate` — it should never reassign `owner`/`balance` itself. This is the same "don't repeat what's already correct" instinct behind last week's decorators and context managers, now applied to classes.

3. **Extend, don't duplicate.** Override `__repr__` in `SavingsAccount` — but instead of rewriting the whole string from scratch, call `super().__repr__()` and append the interest rate to it. This is the concrete difference between *overriding* (replacing a method completely) and *extending* (keeping the parent's behavior and adding to it).

4. **Polymorphism, via a shared method name.** Give both `BankAccount` and `SavingsAccount` a `.summary()` method — the base class's returns a plain owner/balance line; `SavingsAccount`'s also mentions the interest rate. Then write one function, `print_all(accounts)`, that loops over a mixed list of both types and calls `.summary()` on each — **no `isinstance` or `type()` check anywhere in it.** The same line of code produces different output depending on the actual object, purely through Python's normal method lookup. That *is* polymorphism — not a keyword, not a special case, just what already happens when two classes share a method name.

5. **Composition, not inheritance.** Build a `Bank` class that *holds* a list of accounts — a "has-a" relationship, not an "is-a" one. Give it a `.total_assets()` method that sums the balance across everything it holds. Then write, in one sentence, why `Bank` should **not** inherit from `BankAccount`. (If you're tempted to make `Bank` a subclass of `BankAccount` "for convenience," that's the trap this kata is built to catch.)

### Resources
- [Real Python — Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
- [Real Python — Supercharge Your Classes With Python `super()`](https://realpython.com/python-super/)
- [Real Python — Polymorphism (Glossary)](https://realpython.com/ref/glossary/polymorphism/)

### Today's tasks
- [ ] Warm-up: `BankAccount` recreated from memory
- [ ] `SavingsAccount(BankAccount)` built via `super().__init__()`, not re-assignment
- [ ] `__repr__` extended via `super().__repr__()`, not rewritten from scratch
- [ ] `print_all(accounts)` polymorphism kata — no `isinstance`/`type()` anywhere
- [ ] `Bank` composition kata — `total_assets()` works, one-sentence justification for not inheriting


