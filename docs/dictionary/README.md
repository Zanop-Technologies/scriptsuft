# Scriptsuft Dictionary

This directory serves as the language reference for Scriptsuft. The examples in `docs/part1/` point here for definitions and usage notes.

## Index

- [Entry 1: Core Language Keywords](1.md)
- [Entry 2: Control Flow](2.md)
- [Entry 3: Variables and Data](3.md)
- [Entry 4: Math and Expressions](4.md)
- [Entry 5: Syntax Errors and Diagnostics](5.md)
- [Linking and Identifiers](LINKING.md)

## Quick reference

- `!indef` — import a library or built-in module
- `!indef is` — import a submodule or namespace
- `speak(...)` / `print(...)` — print text or variable values
- `compile()` — finalize and run the current script
- `def(static) var{"name"} res{"value"}` — create a static variable
- `loop-limit(n)` — cap iterations for `while` loops
- `while ... :` — repeat a block while a condition is true
- `if ... :` — run a block when a condition is true
- `else:` — fallback block for a false condition
- `switch ... [ ... ]` — branch over cases

For the canonical examples, see `docs/part1/BASICS.md`, `LOGIC.md`, and `MATH.md`.
