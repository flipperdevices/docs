# Developer board with ST-Link V3

![Flipper Zero Devboard with ST-Link V3](https://cdn.flipperzero.one/devboard-stlinkv3.png)

This is a devboard for advanced developers, who need in-circuit debug. It is based on [ST-Link V3 Mini](https://www.st.com/en/development-tools/stlink-v3mini.html), and **differs only in form factor** and ease of connection. Some unused ST-Link and Flipper Zero pins are broken out additionally.

!!! warning "You do not need this board to update Flipper Zero"
    You can update the firmware, develop and upload your own firmware to Flipper Zero via USB without this devboard! It is only needed for in-circuit debug while firmware is running using GDB/OpenOCD/etc. If you don't know exactly how to use it, you don't need this board.

## Specifications

* ST-Link V3 Mini for firmware flashing and in-circuit debug
* Built-in UART to USB, connected to Flipper Zero's UART (GPIO 13, 14)
* Unused Flipper Zero pins are broken out for debug and prototyping

## Schematic and BOM

{{ altium("0ec64b13-433d-419c-8d70-d2e84bef7532") }}

## Altium Designer project sources

[github.com/Flipper-Zero/flipperzero-devboard-stlinkv3](https://github.com/Flipper-Zero/flipperzero-devboard-stlinkv3)  
