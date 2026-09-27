# Turning an LED On

Turning an LED on is very simple ~~(if you have experienced systems programming with C, C++, Rust, Zig, ASM)~~, it requires these three requirements:

1. **Power (Voltage)**

   Who literally powers on an LED without power? It literally needs a voltage across it, positve on one side, negative on the other side. Too little voltage wont make it light, but too much? It will burn out. Its typically 1.8v to 3.3v depending on the color (red ~2.0v, blue ~3.2v). **BUT** do not ever make an LED connect directly to 5v or 3.3v without a resistor or it will die.

2. **A Complete Circuit**
   
   The circuit needs a full path: from the power —> through the LED —> through a resistor —> then back to ground beef. (Ground beef is not a subsititute. Please use actual ground.) If any part of this path is missing, maybe a loose wire, wrong pin, missing connection, it ain't happening bro. It won't light the LED, just silence and no errors and warnings. Connect power directly to ground with nothing in between, it will go boom boom.

3. **Pin Mode**
   
   All the 40 pins **are not the same**, it's like hedgehogs with spikes that dont look the same, power pins are always on, you can't control them, ground pins are all the same, just pick the closest one, the GPIO pins are the ones you can control like your remot control.


**In Short**: Current kills a LED, not voltage, which is why the resistor matters.

## Materials You Need

- Raspberry Pi — any model with the GPIO pins, dont matter, just make sure it has the 40-pin header bro

- MicroSD Card — The SD Card has to be **8GB Minimum**, this is the Pi's hard drive, it won't boot without it.

- Power supply

- USB Cable

- Breadboard

- Jumper wires

- LED

- Resistor

- Keyboard and mouse

- Monitor

- HDMI Cable

Assuming that you have these materials, we will start building.

## 220Ω Method

**The Formula**

```text
R = (V_source - V_led) / I_LED
```

**Definition**

- R = Resistor value (in ohms not volts or watts)

- V_source = The GPIO pin voltage (3.3V on a raspberry pi)

- V_LED = The foward voltage of your LED (may depend on the color)

**Actual numbers**

- V_source = 3.3V

- V_LED = 2.0v (red LED) or ~3.2v (blue LED)

- I_LED = 0.015A (15mA, safe for both the LED and the GPIO pin)

**For a red LED**

```text
R = (3.3 - 2.0) / 0.0015
R = 1.3 / 0.015
R = 86.6Ω
```

**Why 220Ω?**

It's because 86.6Ω is the minimum safe value. But the LED doesn't need to be maximum brightness, by using a higher resistor:

- Uses less current

- Dims the LED safely

- Provides a safety margin


**In short**:

> *220Ω is the standard resistor for an LED on a Raspberry Pi. The actual math gives you about 87Ω for a red LED, but 220Ω works for every color and keeps the current safely low, and don't use no resistor or a tiny one, just use the 220Ω.*

### Instructions

Now, assuming you have those, follow these instructions:

1. Power off the Pi

Unplug the Pi, not just shutting it down, **unplugged**, you are about to touch wires and pins, fellow lad.

2. Place the LED

Look at the LED legs, the long leg is positive while the short leg is negative, like a camel with one long leg and one short leg. If they are already cut, the flat edge on the plastic is the negative side.

3. Place the resistor

Take your 220Ω resistor, direction don't matter if you're black or white, resistors ain't directional lad.

4. Wire it up!

- Long leg of LED -> GPIO 17 (Pin 11)

- Short leg of LED -> 220Ω resistor

- Other end of resistor -> Ground (Pin 9)

That's the circuit me boy! Power from Pin 11 through the LED, through the resistor, back to the ground on pin 9.

5. Write the code

Create a Scriptsuft project, assuming you created one, make a file named `main.srp`.

```text
!indef system
!indef hardware
!indef func(communicator)
!indef func(print)
!indef is pin
!indef is console

<!-- Hardware Device -->
fetch device is:("raspberry-pi")
  // Pin
  pin int(17) mode("output")
  confirm()

loop-limit(10):
  while loop is running:
    write on the pin int(17) state("high")
    wait time(1000ms) int(1000)
    write on the pin int(17) state("low")
    wait time(1000ms) int(1000)

then pin if done:
  close pin(=)

speak("LED blinked. Lucky you survived this round.")

compile()
```

**Result (if ran)**
---

```text
PROCCESS DONE (*)
Communication to Pi has succeded.
LED blinked. Lucky you survived this round.
```

6. Run

The command for running this is: `scriptsuft --communicator -active main.srp`.

YOU HAVE PASSED THE ROUND!