Flipper Zero has its own command line interface, which might be useful for automated testing or remote control.

## Connection

Connect your Flipper Zero to the PC over USB. Your host will detect a virtual COM-port:

![](../../assets/firmware/vcp.png)

This COM-port does not require a special driver and is accessible on most modern operating systems.

You will need any terminal client to open the port: `screen`, `minicom`, etc. No additional setup required except choosing the right port.

For example, the port name in macOS starts with `/dev/tty.usbmodem`:

![](../../assets/firmware/vcp-usbmodem.png)

It is `/dev/tty.usbmodem2069315E544E1` in our case.

To connect to the CLI using `screen` substitute your port name and enter this command in the shell:
```sh
screen /dev/tty.usbmodem2069315E544E1
```

You will see command prompt and firmware build information:

![](../../assets/firmware/cli-prompt.png)

## Commands

### Basic

| Command | Description |
| ------: | :------- |
| `?` or `help` | Outputs all available commands |
| `!` or `version` | Outputs firmware build information  |
| `uid` | Outputs unique device identificator |
| `log` | Redirects stdout to the port |
| `date` |  Outputs current real time clock value |

### Power and Boot

| Command | Description |
| ------: | :------- |
| `poweroff` | Turns off the device |
| `reset` | Reboots the device |
| `dfu` | Reboots the device to [DFU-mode](../../usage/general/flashing-firmware.md) |
| `power_otg_on` | Turns on periphery power |
| `power_otg_off` | Turns off periphery power |
| `power_test` | Outputs battery and charging info |

### User Interface

| Command | Parameters | Description |
| ------: | :-------- | :------- |
| `input_send` | `<key_name> <event_type>` | Emulates button presses.<br/>Available buttons: `up`, `down`, `left`, `right`, `ok`, `back`.<br/>Available events: `press`, `release`, `short`, `long`. |
| `led` | `<led_name> <value>` | Controls the LED and display backlight.<br/>Available channels: `r`, `g`, `b`, `bl`.<br/>Value range: `[0-255]` |
| `vibro` | `<value>` | Turns on (`1`) or turns off (`0`) the vibration motor |
| `screen_stream ` | | Outputs the display framebuffer to the port. Used for screen streaming and gets called automatically |

### GPIO

| Command | Parameters | Description |
| ------: | :-------- | :------- |
| `gpio_set` | `<pin_name> <value>` | Controls GPIO in push-pull output mode |

### SD Card

| Command | Description |
| ------: | :------- |
| `sd_info` | Outputs the SD Card info |
| `sd_status` | Outputs the SD Card status |
| `sd_format` | Formats SD Card **without confirmation** |

### NFC

| Command | Description |
| ------: | :------- |
| `nfc_detect` | Starts reading NFC tags |

### Bluetooth

| Command | Description |
| ------: | :------- |
| `bt_info` | Outputs Bluetooth adapter info |

### Applications Launcher

Any app could be launched using a command prefixed with `app_`, for example `app_iButton`.

See more in the `help` command output.