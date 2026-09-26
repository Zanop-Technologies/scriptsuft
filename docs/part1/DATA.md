# Data — simple and friendly

Hello fellow programmer! This page explains how data works in Scriptsuft in the same relaxed way the rest of the docs teach things: example first, then short explanation.

## What kinds of values can you use?

Scriptsuft keeps things simple. You’ll use:

- strings: "Hello World"
- integers: 0, 1, 42
- booleans / toggles: `on`, `off`, `true`, `false`
- empty/null: `null` or `none`

That’s it — nothing fancy, just useful building blocks.

## Static variables (the ones you define once)

Static variables are for values that don’t change unless your program changes them explicitly. Use `def(static)` to create them.

Example:

```text
!indef system
!indef func(print)
!indef is print
!indef is console

def(static) var{"name"} res{"John"}
def(static) var{"age"} intres{18}

speak var(name)
speak(age)
compile()
```

Quick notes:
- `def(static)` declares a static variable.
- `var{"name"}` names it.
- `res{"..."}` holds strings; `intres{...}` holds integers.
- `speak var(name)` prints the stored value.

## Dynamic values (input or state that changes)

Dynamic values are values that can change at runtime — for example when the user types something in, or when a live function updates a value.

Example (concept):

```text
!indef func(live)

if (function=live) is !declared(=) {
    __live__ can change if user_input is recorded [
        deflive[
            name{"username", dyn var}
            res{change, dyn}
        ]
    ]
}
```

You don’t need to master this right now — think of dynamic variables as "mutable" data coming from input or running processes.

## Collections and structured data (forms, tables, classes)

Scriptsuft examples sometimes show class/table-like structures for UI or records. The basic runtime treats these as higher-level descriptions rather than strict typed objects.

Example:

```text
class UserInput {
    table [
        tc(
            input type("text") name("username")
        )
    ]
}
```

This reads like a form definition: `UserInput` contains a table with an input field named `username`.

## Comparisons and logic — how decisions are made

Conditions use friendly words:

- `is` means equals (e.g. `age is 18`)
- `is not` means not-equals
- `and`, `or`, `not` for logic
- `(=)` and `(+)` appear in docs as symbolic forms (runtime translates these to normal comparisons)

Example:

```text
if age is 18:
    speak("You are allowed")
else:
    speak("You are not allowed")
```

## Short recipes you’ll use often

- Print a value: `speak("text")` or `speak var(name)`
- Make a static variable: `def(static) var{"k"} res{"v"}`
- Loop safety: use `loop-limit(n)` with `while ...` to avoid runaway loops

## Summary — keep it simple

Scriptsuft uses straightforward, human-friendly data:

- strings, numbers, booleans, and null values
- static variables (with `def(static)`) for simple storage
- dynamic variables when you need user input or live updates
- lightweight class/table examples for structured data

For the precise meanings and extra examples, see the dictionary: `docs/dictionary/1.md` and the other HOWTO pages in `docs/part1/`.
