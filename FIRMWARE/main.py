import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.peg_oled_display import PegOLEDDisplay, OledDisplayMode

keyboard = KMKKeyboard()

i2c_bus = busio.I2C(board.D5, board.D4)

oled = PegOLEDDisplay(
    i2c=i2c_bus,
    device_address=0x3C,
    width=128,
    height=64,
)
keyboard.extensions.append(oled)

rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=2,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    animation_mode=AnimationModes.STATIC,
)
keyboard.extensions.append(rgb)

macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.A0, board.A1, None, False),)

PINS = [
    board.D7,
    board.D8,
    board.D10,
    board.D9,
    board.A2
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.MACRO("Hi"),
        KC.MUTE,
    ]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]

if __name__ == '__main__':
    keyboard.go()