# Macropad

> **Author:** Abhay P.  
> **Description:** A personal macropad which features 9 keys with per-key underglow LEDs, a 128×32 SSD1306 OLED display, a rotary encoder, and is powered by a Seeed Studio XIAO RP2040 microcontroller.  
> **Created On:** 05/30/26

---

## Project Specifications

| Component | Description |
|------------|------------|
| Microcontroller | Seeed Studio XIAO RP2040 |
| Keys | 9 Mechanical Keys |
| Display | SSD1306 128×32 OLED |
| Lighting | Per-Key Underglow LEDs |
| Input | Rotary Encoder |
| Enclosure | Custom 3D Printed Case |
| Firmware | KMK |

---

# 1. Schematic Design

> ⏱️ **Time Logged:** 2 Hours

I worked on creating the schematic for my macroboard. I had some challenges in getting everything to work and to not get any erros in ERC. However, in the end, I got it done and I am happy with the end result.

<img width="1115" height="770" alt="Screenshot 2026-05-30 at 1 39 43 PM" src="https://github.com/user-attachments/assets/057b5387-2e15-43a1-b89a-73adc54ac3ea" />

---

# 2. PCB Layout & Routing

> ⏱️ **Time Logged:** 2.5 Hours

I worked on properly laying out all the components of my macroboard and routing them properly. I had some challenges with routing as there were lots of ratsnest lines with limited space. I made the pcb include m2 mounting holes so that it would remain stable in the case. Making the routing compact and away from the mounting holes became imperative so as to not damage the routes when screwing it in. I tried making it as compact as I could. Overall, I am happy with the end result.

### PCB Images

<img width="1115" height="770" alt="Screenshot 2026-05-30 at 1 41 28 PM" src="https://github.com/user-attachments/assets/43865aa9-e266-4683-b039-1f46649f0e77" />
<img width="1115" height="770" alt="Screenshot 2026-05-30 at 1 41 31 PM" src="https://github.com/user-attachments/assets/2c57156d-2c99-4d79-b3ec-af3e2f382b64" />
<img width="1115" height="770" alt="Screenshot 2026-05-30 at 1 40 27 PM" src="https://github.com/user-attachments/assets/b671468e-4ef9-4f86-9d57-ae9ef6a8d11e" />
<img width="1115" height="770" alt="Screenshot 2026-05-30 at 1 40 18 PM" src="https://github.com/user-attachments/assets/58e27dcb-39e8-4b39-bf4f-95c525f106ac" />


---

# 3. Bottom Case Design

> ⏱️ **Time Logged:** 1.75 Hours

I created a 3D model for the bottom case which will house my PCB. It was easy but I just had to get the measurements for the standoffs, inner case, and outter case just right so that all the components would fit and not cause any probelms; I had to account for the inaccuracies of 3D printing and allowed for some clearence. Overall, I am happy with the end result.

<img width="1175" height="756" alt="Screenshot 2026-05-30 at 1 46 41 PM" src="https://github.com/user-attachments/assets/36aedfa1-04c8-4e18-9619-a1cd2556525d" />

---

# 4. Top Case Design

> ⏱️ **Time Logged:** 1 Hour

I created the top case for my macrobaord. This was relatively easy as the outer measurements were based off of the bottom case and the only work I had download the plate for 9 keys and create cut outs for them.

<img width="1175" height="756" alt="Screenshot 2026-05-30 at 1 43 57 PM" src="https://github.com/user-attachments/assets/fc95e0a3-50cf-4b03-8639-a70dd5975e9b" />

---

# 5. Assembly Creation

> ⏱️ **Time Logged:** 45 Minutes

I created the assembly file for my macroboard.

This was not as painstaking because all I had to do was combine the different 3D files, whether it be the case or components, and combine them to create the final assembly.

<img width="1175" height="756" alt="Screenshot 2026-05-30 at 1 44 16 PM" src="https://github.com/user-attachments/assets/4adc9961-c534-4002-bbe7-cba21bf73aa5" />

---

# 6. Firmware Development

> ⏱️ **Time Logged:** 1.5 Hours

I coded the firmware for my macroboard. I knew python so knowing what I was doing was not a problem. However, I was completely new to the KMK software and had to read a couple of articles and watch some videos to understand it. It was really easy and simple afterwards and I got it done. I am happy with the quality of my code.

![Screenshot 2026-05-22 at 12.54.42 PM](https://stasis.hackclub-assets.com/images/1779472469415-7lx7gg.png)

---

# 7. Parts Sourcing

> ⏱️ **Time Logged:** 2.5 Hours

I sourced the parts for my macroboard. I thought this was going to be a relatively easy task but I quickly found out that its easier said than done. Finding quality components for a reduced price was a bit of challenge, but in the end, I got it done.

![Screenshot 2026-05-22 at 12.37.48 PM](https://stasis.hackclub-assets.com/images/1779471453919-b9soa0.png)

---

# 8. GitHub Repository & Documentation

> ⏱️ **Time Logged:** 30 Minutes

I uploaded all of my files to my github repo and created README for final submission.

![Screenshot 2026-05-22 at 12.42.39 PM](https://stasis.hackclub-assets.com/images/1779471744590-grjdku.png)

---

# Project Statistics

| Category | Time Logged |
|----------|------------:|
| Schematic Design | 2 hrs |
| PCB Layout & Routing | 2.5 hrs |
| Bottom Case Design | 1.75 hrs |
| Top Case Design | 1 hr |
| Assembly Creation | 45 min |
| Firmware Development | 1.5 hrs |
| Parts Sourcing | 2.5 hrs |
| GitHub & Documentation | 30 min |
| **Total Time** | **12.5 hrs** |

---

# Reflection

I am immensly grateful for the opportunity to develop a hardware project with integration of software. I started this because I wanted to create something meaningfull for myself that I would use. I learned how to use applicatoins that are used widely in the electronic devleopment industry. The knowledge that I have gained throughout this project will be invaluable and allowed me to create a tangible project that I am be proud of.
