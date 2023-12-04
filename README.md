# max7219-matrix-project
The MAX7219 Matrix serves as a common-cathode display driver with serial input/output
capabilities, facilitating the connection of microprocessors to 7-segment numeric LED
displays featuring up to 8 digits, bar-graph displays, or arrays of 64 individual LEDs. Its
on-chip components include a BCD code-B decoder, multiplex scan circuitry, segment
and digit drivers, as well as an 8x8 static RAM responsible for storing each digit.

![image](https://github.com/Danyoh/max7219-matrix-project/assets/56001475/57e6b739-64a2-4574-b55f-a71f62c31d7a)

I wrote a program that displays a user-inputted single character in the middle of the
matrix. This includes any number, letter, or symbol entered from the prompt in the
console. Depending on the type of character entered, a different animation will be shown
around the border of the matrix. There are three animations, one lights up each corner,
another has trailing dots circling around the matrix, and the last one has one single dog
circling the display.
My code also demonstrates how I utilized threading to ensure the user could enter their
inputs while the other functions to display were still running

#Packages/Libraries Needed
https://luma-led-matrix.readthedocs.io/en/latest/index.html
https://docs.python.org/3/library/threading.html
https://docs.python.org/3/library/time.html
