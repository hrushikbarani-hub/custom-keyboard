import time
import board
import busio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# NEXUS 2x3 COL2ROW matrix, matching the KiCad pinout.
ROWS = (board.GP6, board.GP7)
COLS = (board.GP8, board.GP9, board.GP10)

row_pins = []
for pin in ROWS:
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.OUTPUT
    io.value = True
    row_pins.append(io)

col_pins = []
for pin in COLS:
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    col_pins.append(io)

keyboard = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)

# Replace these actions with the user's final macro choices.
KEYMAP = (
    (("key", (Keycode.CONTROL, Keycode.ALT, Keycode.T)),),
    (("key", (Keycode.CONTROL, Keycode.ALT, Keycode.N)),),
    (("key", (Keycode.CONTROL, Keycode.ALT, Keycode.M)),),
    (("consumer", ConsumerControlCode.PREVIOUS_TRACK),),
    (("consumer", ConsumerControlCode.PLAY_PAUSE),),
    (("consumer", ConsumerControlCode.NEXT_TRACK),),
)

last = [False] * 6

def press_action(index):
    kind, action = KEYMAP[index][0]
    if kind == "consumer":
        consumer.send(action)
        return
    for key in action:
        keyboard.press(key)
    keyboard.release_all()

while True:
    for r, row in enumerate(row_pins):
        row.value = False
        time.sleep(0.0005)
        for c, col in enumerate(col_pins):
            index = r * len(col_pins) + c
            down = not col.value
            if down and not last[index]:
                press_action(index)
            last[index] = down
        row.value = True
    time.sleep(0.001)
