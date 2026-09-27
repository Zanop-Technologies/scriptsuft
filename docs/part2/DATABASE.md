# Database

Scripsuft supports these databases, such as **json**, only JSON is supported, other languages will be added  soon, they have their own `!indef` declarations. 

## Json Declaration

You can only declare json as `!indef json`, json has some sublibraries and 2 functions, it is listed here below:

`!indef json` — Main declaration

`!indef func(data)` — Use json as a database

`!indef func(mod)` — Modify the json (has to be used with `!indef func(data)` )

### Sublibraries

`!indef is jscre` — Create a JSON file for a purpose

`!indef is jsdel` — Delete a JSON file for a purpose

`!indef is jsmod` — Edit or write a existing JSON file for a purpose

#### Samples

Using json for a game database (eg: database for a basketball game)

**`data/basketball.json`** 
---

```json
{}
```

**`main.srp`**
---

```text
!indef system
!indef json
!indef func(data)
!indef func(mod)
!indef is jsmod & jsdel
!indef is def & var
!indef is dyn & opt
!indef is random
!indef is console

class Basketball:
  if class(Basketball) is receiving from subclass(UserInput):
    random will generate:
      speak("You shot a ring!")
    else:
      speak("You didnt shoot a ring...")
  then subclass UserInput {
              table [
                  tc(
                      input type("text") name("Name")\nl
                      input type("option") opt("Shoot")\nl
                  )
              ]
  }
  confirm()

class jsmod {
    src("data/basketball.json")
    modify if UserInput receives(=)
}

compile()
```

**Explanation**

`!indef is random` — The sublibrary randoms `!indef is`, see the dictionary

`recieve` — Receive the input, see the dictionary

`subclass` — A classes sub-class, see the dictionary

`generate` — Can only be used in `!indef is random`, see the dictionary

`confirm()` — Confirm the action, see the dictionary

`src()` — Source of the file, see the dictionary

`modify` — Modify the file

