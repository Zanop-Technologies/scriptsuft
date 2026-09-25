# Basics of Scriptsuft

Welcome to the Basics of Scriptsuft, today, you will be learning your very first app in Scriptsuft.

## Hello World

To create a program in Scriptsuft, download the latest release in our website, then create a file called `main.srp`.

Then type this on the file:
```text
!indef system
!indef func(print)
!indef is print
!indef is console

speak("Hello World")
compile()
```

**Explanation**:

`!indef` — Importing a libarary, see [docs/dictionary/1.md](docs/dictionary/1.md)

`!indef is` — Importing a sub-library, see [docs/dictionary/1.md](docs/dictionary/1.md)

`speak()` — Print text, see [docs/dictionary/1.md](docs/dictionary/1.md)

`compile()` — Compiling the main.srp file, see [docs/dictionary/1.md](docs/dictionary/1.md)

## Basic Variables

Now taking a step up, you can declare variables in two ways, these are:

1. Live Variables
2. Static Variables

But for the basics, we are going to use Static Variables, which are declared using `def(static) var{"name"} res{"John"}`.

Using a variable (static):

```text
!indef system
!indef func(print)
!indef func(var)
!indef is print
!indef is def & res
!indef is console

def(static) var{"name"} res{"John"}

speak var(name)
compile()
```

**Explanation**

`def` — Define, see [docs/dictionary/1.md](docs/dictionary/1.md)

`var` — The name of the static variable, see [docs/dictionary/1.md](docs/dictionary/1.md)

`res` — Response of the variable, see [docs/dictionary/1.md](docs/dictionary/1.md)

`speak var()` — Print the static variable, see [docs/dictionary/1.md](docs/dictionary/1.md)

## Basic Loops

To do Loops in Scriptsuft, you need to use the `while` loop function. You can do this using these:

1. Controlled Loops
2. Uncontrolled Loops (Be careful!)

But for basics, we have to use controlled loops as uncontrolled loops may crash your system.

Then enter this:

```text
!indef system
!indef loop
!indef func(print)
!indef is print
!indef is loop-limit
!indef is console

loop-limit(5)

while loop is running:
  if loop is limit to 5:
    then loop speak("Hello World")
```

**Explanation**

`loop-limit()` — The number of loops that are needed until it stops, see [docs/dictionary/1.md](docs/dictionary/1.md)

