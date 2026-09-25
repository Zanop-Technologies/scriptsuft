# Conditional Logic (Decision Making)

This lesson teaches you `if/else` statements, comparison and logical operators, switch/case statements.

## If Samples

`If` is a programming construct that used to make decisions in code, which tells the computer to run a specific block of code if a certain condition is true.

For this example, we will be using a game style life monitor to detect that if you have no lives left, you are eliminated.

```text
!indef system
!indef func(print)
!indef func(var)
!indef is print
!indef is def & int 
!indef is res
!indef is console

def(static) var{"life"} intres{0}  

# Checks the condition
if target is life(=) but 0 {
    speak("You Died!")
}
compile()
```

**Explanation**

`if` — Conditions, see the dictionary

`target` — The targeted variable, see the dictionary

`is` — The variable to be targeted, see the dictionary

`but` — Says that if this variables integer or status (text) hits a limit, it will say something, see the dictionary

### If + Else Sample

If + Else is like opening an umbrella gives you something and if you dont open it, you wont receive something. 

Here is a sample that is based of a simple age check to tell wheter the user is 18 above or below.

```text
!indef system
!indef func(print)
!indef func(var)
!indef is print
!indef is def & opt // Opt is short for option
!indef is int & res // Int is short for integer
!indef is console

def(static) var{"age"} intres{18}

if age is 18(=){
    speak("You are allowed")
}

opt else is not intres "18"(+){
    speak("You arent allowed")
}
compile()
```

**Explanation**

`intres` — Combination of `int` and `res`, see the dictionary

`int` — Integer, see the dictionary

`opt` — Option, see the dictionary

`is not` — The function is not the specified variable, see the dictionary

`else` — Opposite of if (Note: This might be inaccurate), see the dictionary

## Logical Operators

A logical operator is a symbol or word that combines or compares statements to produce a true/false result.

### Symbols

`(=)` — Allowed

`(+)` — Not allowed

`&` or `and` — Both must be true

`&&` or `or` — Atleast one must be true

`!!` or `not` — Reverse the true value

## Switch/Case Statements

Switch/Case is a control structure that checks one value against several possible cases.

```text
!indef system
!indef func(print)
!indef func(case)
!indef is print
!indef is console

case class {
    switch class("Day1") [
        case(=) create-msg("Monday")
    ]
    switch class("Day2") [
        case(=) create-msg("Tuesday")
    ]
}
compile()
```

**Explanation**

`case` — Compares to a specific action, see the dictionary

`class` — Similar to *HTML* `class` thing, see the dictionary

`switch` — Looks at the value, see the dictionary

`create-msg()` — Create a message