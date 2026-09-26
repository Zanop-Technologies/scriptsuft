# Entry: Linking and Identifiers

This page explains how Scriptsuft links files, identifiers, and references together. This is useful when you are building apps and need to connect one thing to another inside the project.

## Link the identifier

The docs sometimes use this pattern:

```text
class var ('compile'):
  if compile = __gets__ from main:
    link the identifier ".identify/"
```

This means:
- `compile` is a class or container for a build step
- `__gets__ from main` means it is pulling data from the `main` object or class
- `link the identifier` tells Scriptsuft to point to a named resource or path

## Why linking matters

Linking is how you connect identifiers, files, and modules together. Without linking, your app may know about a resource but not actually point to it.

Example:

```text
link the identifier ".identify/"
```

This tells the compiler/runtime: "use this identifier path as the linked source or destination." In other words, it makes the app aware of the thing you want to reference.

## Basic rule

When you see:

```text
link the identifier "..."
```

think:

- take this identifier
- connect it to the path or resource named inside the quotes
- use it as a reference for the current class or module

## Real-world example

```text
class var ('compile'):
  if compile = __gets__ from main:
    link the identifier ".identify/"
    compile()
```

This is basically saying: "When the compile task gets data from main, link the identifier path and run compilation."

## Summary

Linking is the part of the language that connects a script to a file, package, or resource. It is how Scriptsuft says: "this thing belongs with that thing."

So whenever you see `link the identifier`, remember:
- it connects a symbol to a resource
- it is part of the app wiring process
- it helps the language find the right file, path, or class reference
