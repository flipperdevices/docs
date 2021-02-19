Flipper Zero has a power management system, which mainly consists of **fuel gauge** and **charger** ICs.

The main goal of the fuel gauge is to monitor the battery charging level. It works by calculating the incoming and spent energy precisely.

Charger IC controls the charging process, which is very important for battery life and user safety.

Power state application obtains information from these ICs and shows it on display. Let's examine each line of that information.

## Review

=== "Not charging"
    {{ screenshot("../../assets/applications/power-charging-off.png") }}
=== "Charging"
    {{ screenshot("../../assets/applications/power-charging-on.png") }}

### Current

The first value is current, reported by fuel gauge (consumed by the battery). While Flipper is not charging, the value is negative and shows current consumption.

The second value is the charging current, reported by the charger IC. It goes up as the charging starts.

### Voltage

This line shows current voltage levels: from the fuel gauge and from the charger respectively.

!!! warning
    Voltage level given by the charger is correct only during the charging process.

### Charge

The current battery level is shown on this line in percentage.

It's calculated by the fuel gauge using the value of energy consumed by the battery during charging, and spent during the device usage.

### Capacity

First value on this line shows energy left in the battery, and the second one shows its full capacity.

Remaining energy can be calculated correctly only if the installed battery has the same full capacity value that was set during fuel gauge calibration.

!!! warning
    As seen on the screenshot above, some testing units might report that the full capacity is 3000 mAh, which is wrong and leads to battery level miscalculations. The real capacity is 2000 mAh.

### Temperature

Last line shows the fuel gauge and the battery Celsius temperatures respectively.

The battery temperature is measured using NTC thermistor, which is placed on the battery and connected to the charger IC. It changes its resistance depending on the temperature.