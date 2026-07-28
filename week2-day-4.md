# Week 02 · Thu · Review
## Concurrency — Threading, Multiprocessing & asyncio

### Learning objectives
By the end of today, you should be able to:
- Explain the difference between concurrency and parallelism, and which of `threading`, `multiprocessing`, and `asyncio` actually gives you each.
- Explain what the GIL is, and why it means threading speeds up I/O-bound code but not CPU-bound code.
- Use `concurrent.futures.ThreadPoolExecutor` to run several I/O-bound tasks concurrently.
- Use `concurrent.futures.ProcessPoolExecutor` to actually parallelize CPU-bound work.
- Write a basic `async def`/`await` coroutine, and explain why it needs a cooperative `await` point rather than relying on the OS to interrupt it.
- Make a real HTTP request with `requests`; self-review this week's toolkit PR and respond to every review comment.

### Lesson

**1. Concurrency vs. parallelism — the distinction everything today depends on**
**Concurrency** means dealing with multiple things at once — interleaving them so progress happens on several fronts, without necessarily running at the exact same instant. **Parallelism** means literally executing multiple things at the same instant, which requires multiple CPU cores actually doing work simultaneously. `threading` and `asyncio` give you concurrency; only `multiprocessing` gives you true parallelism in Python. This one distinction decides which tool is even a candidate for a given problem.

**2. The GIL, in one paragraph**
CPython's Global Interpreter Lock allows only one thread to execute Python bytecode at any given moment — even on a machine with 16 cores. This sounds like it makes threading useless, but it doesn't: a thread that's *waiting* on something outside Python (a network response, a disk read) releases the GIL while it waits, letting another thread run. So threading genuinely helps **I/O-bound** work (waiting is most of what happens), but does nothing for **CPU-bound** work (a thread doing pure computation never releases the GIL, so threads just take turns — no faster than doing it one at a time, sometimes slightly slower).

**3. `threading` — concurrency for I/O-bound work**
`concurrent.futures.ThreadPoolExecutor` manages a pool of threads for you — hand it a function and a list of inputs via `.map()` or `.submit()`, and it runs them concurrently instead of one at a time. This is the right tool exactly when the work spends most of its time *waiting* (a slow API call, a file download) rather than computing.

**4. `multiprocessing` — real parallelism for CPU-bound work**
`concurrent.futures.ProcessPoolExecutor` runs your function in separate **OS processes**, each with its own Python interpreter and its own GIL — so they genuinely execute at the same time on separate cores. The cost: processes don't share memory by default, so data passed in and results passed back are copied, not shared. That overhead only pays for itself when the work itself is CPU-heavy enough to be worth it — for a fast function, spinning up processes can be slower than just running it directly.

**5. `asyncio` — cooperative concurrency, single-threaded**
`asyncio` gets concurrency a third way: a **single thread** runs many `async def` coroutines, and each one voluntarily hands control back at every `await` point instead of the OS interrupting it. This is *cooperative* multitasking, not preemptive — which is exactly why a coroutine that never `await`s (e.g. does a long CPU computation inline) blocks everything else running on that event loop, unlike a thread. The payoff: thousands of concurrent I/O-bound tasks cost far less overhead than one OS thread per task would.

**6. `requests` — the concrete I/O-bound example tying it together**
`requests.get(url)` is a synchronous, blocking HTTP call — and it's *the* canonical I/O-bound operation every example above has been pointing at. One important catch worth knowing before today's async kata: `requests` itself is blocking and doesn't cooperate with `asyncio`'s `await` mechanism — dropping a `requests.get()` call inside an `async def` function blocks the whole event loop exactly like a CPU-bound task would. A real async HTTP client (like `httpx` or `aiohttp`) is what a production async scraper would actually use; today's kata isolates the `asyncio` mechanism itself using `asyncio.sleep` as a stand-in for "waiting on the network," so the concept lands before the extra dependency does.

**7. Process, unchanged from last week: self-review before anyone else looks at it**
Same discipline as Week 1 Thursday, now applied to this week's toolkit: run your own self-review checklist before requesting review, and when feedback comes back, respond to *every* comment — either fix it, or explain your reasoning if you disagree. This doesn't get easier just because the code got more advanced; if anything, concurrency bugs are exactly the kind of thing a second reader catches that you won't.

### Resources
- [Real Python — Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
- [Real Python — An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
- [Real Python — `multiprocessing`](https://realpython.com/ref/stdlib/multiprocessing/)
- [Real Python — Python's `asyncio`: A Hands-On Walkthrough](https://realpython.com/async-io-python/)
- [Real Python — Python's Requests Library (Guide)](https://realpython.com/python-requests/)

**Review resource:** [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/) *(same as last week — worth a second read now that the code under review is more advanced)*

### Kata set
1. **Concept check, out loud.** One sentence each: what's the difference between concurrency and parallelism, and which of `threading`, `multiprocessing`, `asyncio` gives you which?
2. **Threaded, I/O-bound.** Using `ThreadPoolExecutor`, run 5 slow tasks concurrently (real `requests.get()` calls to a public API, or `time.sleep(1)` stand-ins if you'd rather isolate the mechanism first). Time it against running the same 5 tasks one at a time in a plain loop.
3. **The CPU-bound proof.** Write a genuinely CPU-heavy function (e.g. summing the squares of the first 20 million integers). Run it several times via `ThreadPoolExecutor`, then via `ProcessPoolExecutor`, timing both against a plain sequential loop. Confirm for yourself: threads don't meaningfully help here, processes do.
4. **Async, the mechanism in isolation.** Rewrite Kata 2 using `async def` functions, `await asyncio.sleep(1)` as the stand-in for network waiting, and `asyncio.gather()` to run them concurrently. Confirm the total time looks like the threaded version's, not the sequential one's.
5. **A real request.** Make one real `requests.get()` call to a public API of your choice, check `.status_code`, parse the JSON response, and print one specific field from it — this is Wednesday's `json` lesson, now hitting a real network response instead of a local file.
6. **Self-review, then real review.** Run your own self-review checklist on this week's toolkit PR before asking anyone to look at it. Once you get feedback, respond to every comment.

### Today's tasks
- [ ] Concurrency-vs-parallelism concept check, stated out loud
- [ ] Threaded I/O-bound kata done, timed against sequential
- [ ] CPU-bound kata done — threads vs. processes, both timed
- [ ] Async kata done using `asyncio.gather`
- [ ] Real `requests` call made, JSON parsed, one field printed
- [ ] Self-review completed before requesting review; every review comment addressed


