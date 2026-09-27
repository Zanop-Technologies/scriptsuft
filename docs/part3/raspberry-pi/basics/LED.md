# Turning an LED On

Turning an LED on is very simple ~~(if you have experienced systems programming with C, C++, Rust, Zig, ASM)~~, it requires these three requirements:

1. **Power (Voltage)**

   Who literally powers on an LED without power? It literally needs a voltage across it, positve on one side, negative on the other side. Too little voltage wont make it light, but too much? It will burn out. Its typically 1.8v to 3.3v depending on the color (red ~2.0v, blue ~3.2v). **BUT** do not ever make an LED connect directly to 5v or 3.3v without a resistor or it will die.

2. **A Complete Circuit**
   
   The circuit needs a full path: from the power —> through the LED —> through a resistor —> then back to ground beef. (Ground beef is not a subsititute. Please use actual ground.) If any part of this path is missing, maybe a loose wire, wrong pin, missing connection, it ain't happening bro. It won't light the LED, just silence and no errors and warnings. Connect power directly to ground with nothing in between, it will go boom boom.

3. **Pin Mode**