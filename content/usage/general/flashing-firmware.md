## Installing dfu-util

`dfu-util` is currently required to flash Flipper Zero firmware via USB-C port.

You can skip this part if you have `dfu-util` installed.

### Windows

_TODO_

### macOS

Install [Homebrew](https://brew.sh) if you don't have it:
``` sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install `dfu-util`:
``` sh
brew install dfu-util
```

### Linux

Choose your distro to install from package manager or [build from sources](http://dfu-util.sourceforge.net/build.html).

=== "Ubuntu/Debian"
    ``` sh
    sudo apt-get install dfu-util
    ```
=== "Fedora"
    ``` sh
    sudo yum install dfu-util
    ```
=== "Arch"
    ``` sh
    sudo pacman -Sy dfu-util
    ```

## Flashing firmware

### Preparations

1. Click the image to download latest build of full firmware:
[![](https://update.flipperzero.one/latest-firmware-banner.png){: width="400"}](https://update.flipperzero.one/full_firmware_latest.bin)
2. Connect your Flipper Zero to the PC over USB
3. [Enter DFU Mode](switching-modes.md#dfu-mode) and check that the LED is blue

### Uploading firmware

Run this command in the terminal to upload new firmware:
``` sh
dfu-util -a 0 -s 0x08000000 -D full_firmware_latest.bin
```

!!! warning
    If you download the firmware from the link above, you will get a bundled binary, which consists of bootloader and firmware itself.

    However, if you're trying to flash the firmware **without bootloader**, you must use `0x08008000` in `-s` parameter of `dfu-util`.

### Booting back

After flashing the firmware, [reboot](switching-modes.md#reboot) to exit DFU mode.

USB cable can be unplugged before or after rebooting.