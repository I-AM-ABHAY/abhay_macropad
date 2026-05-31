# ============================================================
# BITMAPS (UNCHANGED - keep your full dataset here)
# ============================================================
# ALL_BITMAPS = [...]
# (KEEP YOUR ORIGINAL BITMAP SECTION EXACTLY THE SAME)

ALL_BITMAPS = ALL_BITMAPS  # placeholder if already defined above


# ============================================================
# IMPORTS
# ============================================================

import board
import busio
import framebuf
import time
import supervisor
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.extensions.neopixel import NeoPixel
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Tap, Delay


# ============================================================
# OLED DRIVER (same, slightly cleaned)
# ============================================================

class SSD1306:
    def __init__(self, i2c, addr=0x3C):
        self.i2c = i2c
        self.addr = addr
        self.buf = bytearray(128 * 32 // 8)
        self.fb = framebuf.FrameBuffer(self.buf, 128, 32, framebuf.MONO_HLSB)
        self.init()

    def init(self):
        for c in (
            0xAE, 0xD5, 0x80, 0xA8, 0x1F, 0xD3, 0x00,
            0x40, 0x8D, 0x14, 0x20, 0x00, 0xA1, 0xC8,
            0xDA, 0x02, 0x81, 0xCF, 0xD9, 0xF1, 0xDB,
            0x40, 0xA4, 0xA6, 0xAF
        ):
            self.i2c.writeto(self.addr, bytes([0x00, c]))

    def show(self):
        self.i2c.writeto(self.addr, b"\x40" + self.buf)

    def fill(self, v):
        self.fb.fill(v)

    def blit_bitmap(self, bmp):
        self.buf[:] = bmp

    def text(self, s, x, y):
        self.fb.text(s, x, y, 1)


# ============================================================
# OLED ANIMATOR (UPGRADED)
# ============================================================

class OledAnimator:
    def __init__(self, oled):
        self.oled = oled
        self.state = "IDLE"
        self.key = 0
        self.frame = 0
        self.last = supervisor.ticks_ms()

    def trigger(self, k):
        self.state = "IN"
        self.key = k
        self.frame = 0

    def tick(self):
        now = supervisor.ticks_ms()
        if now - self.last < 35:
            return
        self.last = now

        if self.state == "IDLE":
            self.draw_idle()

        elif self.state == "IN":
            self.draw_in()
            self.frame += 1
            if self.frame > 6:
                self.state = "HOLD"
                self.hold_start = now

        elif self.state == "HOLD":
            self.draw_hold()
            if now - self.hold_start > 9000:
                self.state = "OUT"
                self.frame = 0

        elif self.state == "OUT":
            self.draw_out()
            self.frame += 1
            if self.frame > 6:
                self.state = "IDLE"

        self.oled.show()

    def draw_idle(self):
        self.oled.fill(0)
        t = time.localtime()

        # subtle moving clock shift
        shift = (t.tm_sec % 2)

        self.oled.text(f"{t.tm_hour:02d}:{t.tm_min:02d}", 40 + shift, 2)
        self.oled.text(f"{t.tm_mon}/{t.tm_mday}", 48, 18)

    def draw_in(self):
        bmp = ALL_BITMAPS[self.key]
        fb = framebuf.FrameBuffer(bytearray(bmp), 128, 32, framebuf.MONO_HLSB)

        self.oled.fill(0)
        offset = 128 - (self.frame * 20)
        if offset < 0:
            offset = 0
        self.oled.fb.blit(fb, offset, 0)

    def draw_hold(self):
        self.oled.blit_bitmap(ALL_BITMAPS[self.key])

    def draw_out(self):
        bmp = bytearray(ALL_BITMAPS[self.key])
        fb = framebuf.FrameBuffer(bmp, 128, 32, framebuf.MONO_HLSB)

        # fast wipe effect
        for i in range(self.frame * 20):
            x = i % 128
            y = (i * 3) % 32
            fb.pixel(x, y, 0)

        self.oled.blit_bitmap(bmp)


# ============================================================
# KEYBOARD
# ============================================================

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP4, board.GP2, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

i2c = busio.I2C(board.GP7, board.GP6)
oled = SSD1306(i2c)
anim = OledAnimator(oled)

# ============================================================
# LED SYSTEM (IMPROVED - smooth behavior)
# ============================================================

rgb = NeoPixel(board.GP3, 9, brightness=0.4, auto_write=False)

led_state = [(0,0,0)] * 9
active = -1

def set_led(i, color):
    global active
    active = i

    for j in range(9):
        led_state[j] = (0,0,0)

    led_state[i] = color

def update_leds():
    for i in range(9):
        rgb[i] = led_state[i]
    rgb.write()


# ============================================================
# ENCODER
# ============================================================

encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((board.GP29, board.GP0, None),)
encoder.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]


# ============================================================
# MACROS
# ============================================================

OPEN_SPOTIFY = KC.MACRO(Tap(KC.LGUI, KC.SPACE), Delay(200), "spotify", Tap(KC.ENTER))


KEY_DEFS = [
    ("SS", KC.LGUI(KC.LSHIFT(KC.N4)), (255,80,0)),
    ("CH", KC.LGUI(KC.SPACE), (0,120,255)),
    ("TAB", KC.LGUI(KC.LSHIFT(KC.T)), (0,255,200)),
    ("KILL", KC.LGUI(KC.LALT(KC.ESC)), (255,0,0)),
    ("LOCK", KC.LCTRL(KC.LGUI(KC.Q)), (180,0,255)),
    ("FULL", KC.LGUI(KC.LSHIFT(KC.N3)), (255,140,0)),
    ("SPOT", OPEN_SPOTIFY, (0,255,80)),
    ("PLAY", KC.MPLY, (200,200,200)),
    ("SPOTL", KC.LGUI(KC.SPACE), (255,220,0)),
]


# ============================================================
# KEY WRAPPER
# ============================================================

def mk(i):
    name, action, color = KEY_DEFS[i]

    def press(k, keyboard, *a):
        anim.trigger(i)
        set_led(i, color)
        update_leds()
        keyboard.tap_key(action)

    def release(k, keyboard, *a):
        set_led(-1, (0,0,0))
        update_leds()

    return make_key(names=(name,), on_press=press, on_release=release)


AK = [mk(i) for i in range(9)]

keyboard.keymap = [[AK[i] for i in range(9)]]


# ============================================================
# OLED HOOK
# ============================================================

class OLEDHook:
    def before_hid_send(self, keyboard):
        anim.tick()

keyboard.extensions.append(OLEDHook())


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    keyboard.go()
