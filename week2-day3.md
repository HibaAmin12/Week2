# Week 02 · Wed · Build
## Type Hints, Logging & the Standard Library You'll Use Every Day

### Learning objectives
By the end of today, you should be able to:
- Add type hints to a function's signature, and explain what they do (help tools and readers) versus what they don't do (nothing at runtime).
- Replace `print()`-based debugging with the `logging` module, at the right severity level.
- Use `pathlib.Path` for file paths instead of manually joining strings.
- Use `datetime` objects for real date/time values instead of formatted strings.
- Read and write structured data with `json`, and reach for the right `collections` type (`defaultdict`, `Counter`) instead of a plain dict doing extra work.
- Split a script that's grown too large into a small, sensibly organized project instead of one file.

### Lesson

**1. Type hints — documentation Python doesn't enforce**
`def deposit(self, amount: float) -> None:` tells a reader (and your editor, and tools like `mypy`) what's expected in and out — but Python itself does **nothing** with it at runtime. Call `deposit("fifty")` on a hint of `amount: float` and it runs exactly as far as the un-hinted version would; Python never checks. Hints are for humans and static-analysis tools, not the interpreter. You've actually been writing type hints since last Thursday without the name attached to them: every `@dataclass` field (`amount: float`, `category: str`) is a type hint — dataclasses just happen to be one of the few places Python *does* read the annotation, to know what `__init__` should accept.

**2. Logging — the professional replacement for scattered `print()`s**
Tuesday of last week you learned to reach for `breakpoint()` instead of `print()` for *temporary, interactive* investigation. `logging` solves a different, permanent problem: visibility into what a running program did, long after it's finished, without editing code to add or remove prints. `logger = logging.getLogger(__name__)` gets you a logger; five levels — `DEBUG < INFO < WARNING < ERROR < CRITICAL` — let you record everything but only *show* what matters right now, controlled by one config line instead of by deleting print statements. `print()` has no severity, no timestamp, no easy way to send output to a file instead of (or as well as) the console — `logging` does all three by default.

**3. `pathlib` — paths as objects, not strings you concatenate**
Building a path with `folder + "/" + filename` breaks the moment you're on a different OS or the folder has a trailing slash or not. `pathlib.Path` fixes this by making a path an object: `Path("data") / "transactions.json"` is correct everywhere, and the result has methods — `.exists()`, `.read_text()`, `.glob("*.json")` — instead of you calling separate `os.path` functions on a plain string. `.read_text()`/`.write_text()` also handle the open/close for you internally — the same guarantee Monday's `with open(...)` gives you explicitly, now wrapped for the common case.

**4. `datetime` — real date/time values, not formatted strings**
A timestamp should be a `datetime` object, not a string like `"2026-07-22"` — a string can't be compared, sorted numerically, or have three days added to it without re-parsing. `datetime.now()` gives you the current moment; `timedelta` lets you do arithmetic (`now() - timedelta(days=7)`); `.strftime()` turns a `datetime` *into* a display string only at the point you actually need to show it to a human, and `.isoformat()`/`datetime.fromisoformat()` is the safe way to serialize one to/from JSON (JSON itself has no native date type).

**5. `json` and `collections` — structured data, and the right container for the job**
`json.dump(data, f)` / `json.load(f)` convert between Python objects and JSON text — the same format last week's `load_expenses_from_file` bug was already using, now used correctly. Pair this with the right `collections` type instead of a plain `dict`/`list` doing extra work by hand: `collections.defaultdict(list)` removes the "if key not in dict: dict[key] = []" boilerplate you'd otherwise write before every append; `collections.Counter(items)` tallies occurrences in one call instead of a manual loop with a running dict. Neither is a new concept — they're `dict` and `list` with one specific annoyance pre-solved.

**6. Project structure — when one file stops being enough**
A script that started as one file (like this week's `expense_tracker.py`) eventually needs splitting: group code by responsibility, not by "when I happened to write it" — a `models.py` for your classes, a `main.py` (or `__main__.py`) for the code that actually runs something. Imports should flow one direction only (`main.py` imports from `models.py`, never the reverse) — if two files need things from each other, that's a sign they should be one file, or a third module should hold the shared piece. This is the same `__init__.py`-marks-a-package mechanism from last Friday, now used deliberately from the start of a project instead of retrofitted at the end.

### Resources
- [Real Python — Python Type Checking (Guide)](https://realpython.com/python-type-checking/)
- [Real Python — Logging in Python](https://realpython.com/python-logging/)
- [Real Python — Python's `pathlib` Module: Taming the File System](https://realpython.com/python-pathlib/)
- [Real Python — Using Python `datetime` to Work With Dates and Times](https://realpython.com/python-datetime/)
- [Real Python — Working With JSON Data in Python](https://realpython.com/python-json/)
- [Real Python — Python's `collections`: A Buffet of Specialized Data Types](https://realpython.com/python-collections-module/)

### Build tasks today
Today is independent build time — apply this lesson directly to Monday/Tuesday's `BankAccount`/`SavingsAccount`/`Bank` classes rather than a disconnected exercise:

1. **Type hints.** Add type hints to every method on `BankAccount` and `Bank`, including return types (`-> None`, `-> float`, etc). Then deliberately call one method with the wrong type (e.g. `deposit("fifty")`) and confirm Python runs it anyway — proving hints aren't enforced.
2. **Logging, not `print`.** Replace any `print()` calls in your account code with `logging` calls at the right level — `INFO` for a normal deposit, `WARNING` for a failed withdrawal attempt, `ERROR` when `InsufficientFundsError` is actually raised. Configure logging once so it writes to both the console and a file.
3. **`pathlib` + `json`.** Write `save_transactions(path, transactions)` and `load_transactions(path)` functions that write/read a list of transaction dicts as JSON, building the path with `pathlib.Path`, not string concatenation.
4. **`datetime`.** Give every transaction a real `datetime` object (not a string) for when it happened. Write `transactions_today(transactions)` that filters to only today's, using actual `datetime` comparison — not string matching.
5. **`collections`.** Use `Counter` to tally how many transactions happened per category, and `defaultdict(list)` to group transaction amounts by category — without a manual `if category not in totals:` check anywhere.
6. **Project structure.** Split today's code into at least two files — `models.py` for the classes, `main.py` for the code that actually runs a demo — with imports flowing one direction only. Confirm it still runs correctly after the split.

## Target deliverable
Unit-tested Python Utility Toolkit, GitHub repo — today's work (typed, logged, JSON-backed account classes, properly split into modules) is the core of it.


