import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.neopixel import NeoPixel
from kmk.extensions.oled import Oled

from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# ============================================================
# MATRIX (3x3)
# ============================================================

keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
)

keyboard.row_pins = (
    board.GP4,
    board.GP2,
    board.GP1,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ============================================================
# OLED
# ============================================================

oled = Oled(
    sda=board.GP6,
    scl=board.GP7,
    i2c_addr=0x3C,
    width=128,
    height=32,
)

keyboard.extensions.append(oled)

# ============================================================
# RGB LEDs (9 LEDs @ 50% brightness)
# ============================================================

rgb = NeoPixel(
    pin=board.GP3,
    num_pixels=9,
    brightness=0.5,
    auto_write=True,
)

keyboard.extensions.append(rgb)

# White LEDs
rgb.fill((255, 255, 255))

# ============================================================
# ROTARY ENCODER
# ============================================================

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.GP29, board.GP0, None),
)

# Counter-clockwise = screen brightness down
# Clockwise = screen brightness up
encoder_handler.map = [
    (
        (KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.NO),
    ),
]

# ============================================================
# KEYMAP
# ============================================================

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
    ]
]

# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    keyboard.go()
