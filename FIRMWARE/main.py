import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder A (Pin 1/GP26), Encoder B (Pin 2/GP27)
encoder_handler.pins = ((board.GP26, board.GP27, None, False),)
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

# LED DIN (Pin 7/GP0)
rgb = RGB(pixel_pin=board.GP0, num_pixels=1, hue_default=0, sat_default=255, val_default=100)
keyboard.extensions.append(rgb)

# Display I2C (SDA=Pin 5/GP6, SCL=Pin 6/GP7)
i2c_bus = busio.I2C(board.GP7, board.GP6)

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["LAYER"]},
        corner_two={0:OledReactionType.LAYER,1:["1"]},
        corner_three={0:OledReactionType.STATIC,1:["KMK"]},
        corner_four={0:OledReactionType.STATIC,1:["KB"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
    i2c=i2c_bus,
)
keyboard.extensions.append(oled_ext)

# SW1(Pin8/GP1), SW2(Pin9/GP2), SW3(Pin10/GP4), SW4(Pin11/GP3), SW5(Pin4/GP29), EncSW(Pin3/GP28)
PINS = [board.GP1, board.GP2, board.GP4, board.GP3, board.GP29, board.GP28]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.MUTE],
]

if __name__ == '__main__':
    keyboard.go()