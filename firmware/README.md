# NEXUS firmware

This is a CircuitPython starting firmware for the Orpheus Pico 2 and the routed NEXUS 2x3 matrix.

Copy `code.py` to the board after installing CircuitPython and the Adafruit HID library. The matrix assignment is:

- rows: GP6, GP7
- columns: GP8, GP9, GP10
- OLED: GP4 SDA, GP5 SCL, 3V3, GND

The six default actions are temporary placeholders: three desktop shortcuts followed by previous/play-next media controls. Edit `KEYMAP` after deciding the final macros.

Flashing still requires a USB data cable and the physical Orpheus Pico 2. Test one switch at a time after copying the file.
