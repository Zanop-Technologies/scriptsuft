# User Input & Dynamic Variables

User Input is the process of getting input from the program, it stops before continuing, dynamic variables are different from static variables as they can change information.

## User Input with Dynamic Variables Sample

```text
!indef system
!indef func(print)
!indef func(live)
!indef is print
!indef is def & var
!indef is form
!indef is dyn
!indef is console

if (function=live) is !declared(=) {
    __live__ can change if user_input is recorded [
        deflive[
            name{"username", dyn var}
            res{change, dyn}
        ]
    ]
}

class UserInput {
    table [
        tc(
            input type("text") name("username")
        )
    ]
}
```

**Explanation**

The explanantion can be found in the dictionary as the explanation for this is really long.