# Abhay’s Macropad Firmware Documentation

## Overview

This firmware runs a 9-key macropad built on a Seeed Studio XIAO RP2040 using KMK firmware.

It controls:

* 9 macro keys
* SSD1306 128×32 OLED display
* 9 NeoPixel RGB LEDs (daisy-chained)
* Rotary encoder for volume control

All components work together to handle input, visual output, and system control.

---

## Hardware

### Microcontroller

* Seeed Studio XIAO RP2040

### Display

* SSD1306 OLED (128×32, I2C)
* Address: 0x3C
* Custom lightweight driver (no external libraries)

### Input

* 3×3 key matrix (9 keys total)
* Rotary encoder (volume control)

### Output

* 9 NeoPixel LEDs (single daisy-chained strip)

---

## Pin Mapping

### Key Matrix

* Columns: GP26, GP27, GP28
* Rows: GP4, GP2, GP1
* Diode orientation: COL2ROW

### OLED (I2C)

* SDA: GP6
* SCL: GP7
* 400kHz I2C speed

### Encoder

* A: GP29
* B: GP0

### NeoPixel

* Data: GP3
* 9 LEDs in a single chain

---

## Key System

Each key has:

* A label
* A macro or shortcut
* A color
* An index mapping to a bitmap and LED position

### Key actions include:

* Screenshot tools
* Chrome launcher
* Tab recovery
* Force quit
* Lock screen
* Full screenshot
* Spotify launch
* Play/pause
* Spotlight search

---

## Key Press Behavior

When a key is pressed:

1. OLED animation starts
2. The corresponding LED turns on with its assigned color
3. The macro or shortcut is executed
4. The OLED displays the matching bitmap

When the key is released:

* All LEDs are turned off

---

## OLED System

The OLED uses a framebuffer-based driver.

### Features:

* Text rendering
* Bitmap rendering (128×32 raw images)
* Direct I2C updates

---

## OLED Animation States

### IDLE

* Shows current time in HH:MM format
* Shows date below the time
* Subtle movement in text position

### IN (slide-in)

* Bitmap slides in from the right side
* Fast transition into view

### HOLD

* Bitmap remains fully visible
* Displayed for approximately 9–10 seconds

### OUT (fade-out)

* Bitmap is cleared using a pixel wipe effect
* Returns to idle state

---

## LED SYSTEM

The LED system controls 9 NeoPixel LEDs in a single chain.

### Behavior:

* All LEDs are off when idle
* Only one LED is active at a time
* Each key has a fixed RGB color

### Operation:

1. All LEDs are cleared
2. One LED is set to the active key color
3. LED state is written to the strip

---

## Rotary Encoder

Controls system volume:

* Rotate left → volume down
* Rotate right → volume up

---

## Macros

Some keys execute multi-step macros instead of single shortcuts.

### Example: Spotify

* Opens system search (Spotlight)
* Types "spotify"
* Launches the application

### Example: Chrome

* Opens Spotlight
* Launches Chrome
* Selects a profile (school or personal)

---

## Performance Design

### OLED

* Updates are timed to avoid unnecessary refreshes
* Animation states control rendering frequency

### LEDs

* LED state is managed through a controlled update cycle
* Prevents inconsistent LED output across keys

---

## System Flow

1. Key press is detected
2. Macro or shortcut is executed
3. OLED animation is triggered
4. LED state is updated
5. Encoder operates independently for volume control

---

## Summary

This firmware runs a fully integrated macropad system:

* 9 programmable keys
* OLED display with animations
* RGB LED feedback per key
* Rotary encoder for volume control

All components are synchronized to respond to user input in real time.
